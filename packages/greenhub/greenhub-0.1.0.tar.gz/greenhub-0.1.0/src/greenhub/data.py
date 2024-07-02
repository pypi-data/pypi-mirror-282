import pandas as pd
import requests
from requests.exceptions import HTTPError
from io import StringIO
from tqdm.notebook import tqdm
from typing import Optional

from .initialize import get_fdc, get_user_api_key

DATA_REST_API_URL: str = 'https://us-central1-digitalyieldmonitoringplatform.cloudfunctions.net/getFeatureData'
SPATIAL_RESOLUTIONS: [str] = ['country', 'state', 'municipality']
TIME_RESOLUTIONS: [str] = ['daily', 'monthly', 'weekly']
WARNING_COLOR_PRINT: str = '\033[93m'


def _fetch_data(file_path: str) -> Optional[pd.DataFrame]:
    """
    The greenhub REST API endpoint `getFeatureData` (Google Cloud Function) is queried with the given `file_path`.
    If the request is successful, the retrieved data is returned as a pandas DataFrame,
    if the REST API returns a status code 404 (Not Found), `None` is returned.

    :param file_path: paths to feature date in greenhub Google Cloud Storage `/featureData`
    :returns: dataframe containing the loaded data; None if res status code equals 404
    :raises HTTPError: if response status is not 200 or 404
    """

    # request data
    user_api_key = get_user_api_key()
    params = {
        'featureDataPath': file_path,
        'apiKey': user_api_key
    }
    res = requests.get(DATA_REST_API_URL, params=params)

    # parse data
    if res.status_code == 200:
        csv_content = StringIO(res.text)
        df = pd.read_csv(csv_content)
        return df
    elif res.status_code == 404:
        return None
    else:
        raise HTTPError(f'Fetching feature data from API endpoint failed with status code: {res.status_code}')


def _load_data(feature_files_paths: [str], data_name: str) -> (Optional[pd.DataFrame], [str]):
    """
    For each path in the `feature_files_paths`, it is first checked whether the data is already cached locally.
    If this is not the case, the data is loaded via the greenhub REST API `getFeatureData`.
    All loaded data is concatenated into a single pandas dataframe at the end,
    so it is important that the data referenced by the paths has the same structure (columns).

    :param feature_files_paths: paths to feature files in greenhub Google Cloud Storage `/featureData`
    :param data_name: the name of the data to load, used for logging purposes only
    :returns: dataframe containing the loaded and concatenated data, None if none of the paths worked;
        list of paths for which no data could be loaded by the API
    """

    # fetch data and cache it, if already cached load it
    fdc = get_fdc()
    data = []
    invalid_paths = []
    for f in tqdm(feature_files_paths, desc=f"Loading {data_name}", unit="items"):
        cached_data = fdc.load_feature_data(f)
        if cached_data is None:
            # data not cached -> fetch data
            fetched_data = _fetch_data(f)
            if fetched_data is None:  # check if data was fetches successfully
                invalid_paths.append(f)
            else:
                data.append(fetched_data)
                fdc.save_feature_data(f, fetched_data)
        else:
            # data is cached
            data.append(cached_data)

    # combine all data to one single dataframe
    if not data:
        return None, invalid_paths
    return pd.concat(data, axis=0, ignore_index=True), invalid_paths


def get_vi_data(
        country: str,
        start_year: int,
        end_year: int = None,
        spatial_resolution: str = 'country',
) -> pd.DataFrame:
    """
    This function returns all available VI feature data on greenhub.ai for a specific `country` (e.g., US, BR)
    and year (`start_year`). By default, only VI data aggregated at the country level is returned,
    but with the `spatial_resolution parameter`, one can choose between 'country', 'state', and 'municipality'.
    Additionally, multiple years can be requested at once by specifying a time period by defining
    `start_year` **and** `end_year`.
    For more information please check out the official greenhub.ai documentation.

    :param country: country for which data is loaded, represented by a two-letter country code (e.g. US)
    :param start_year: year for which data is loaded; if `end_year` is also defined, then `start_year` is the
        first year of the time interval for which data is loaded
    :param end_year: if defined, `end_year` is the last year of the time interval, defined by `start_year` and
        `end_year`, for which data is loaded
    :param spatial_resolution: spatial resolution on which the data is aggregated; set to 'country' by default;
        can be set to 'country', 'state', or 'municipality'
    :returns: dataframe containing the loaded and concatenated data
    """

    # parameter None/default handling and preprocessing
    if end_year is None:
        end_year = start_year
    spatial_resolution = spatial_resolution.lower()
    country = country.upper()

    # check if greenhub api is initialized
    fdc = get_fdc()
    user_api_key = get_user_api_key()
    if fdc is None or user_api_key is None:
        raise Exception('Please use greenhub.initialize() before requesting data.')

    # some obvious/important parameter checks
    if len(country) != 2:
        raise ValueError('The country must be represented by a two-letter country code (e.g. US).')
    if start_year > end_year:
        raise ValueError('The end_year must be greater than or equal to the start_year.')
    if spatial_resolution not in SPATIAL_RESOLUTIONS:
        raise ValueError(f'The given spatial_resolution is not known. '
                         f'These spatial_resolutions are available: {", ".join(SPATIAL_RESOLUTIONS)}.')

    # construct all data files paths needed for the requested vi data
    feature_files_paths = []
    base_path = f'featureData/{country}/vi/{spatial_resolution}'
    for y in range(start_year, end_year + 1):
        for m in range(1, 13):
            feature_files_paths.append(f'{base_path}/{y}-{str(m).zfill(2)}.csv')

    if not feature_files_paths:
        raise ValueError('For the given parameters, no data can be retrieved. '
                         'Please check the parameters and the official greenhub.ai documentation.')

    # load and fetch data as one combined dataframe
    data, invalid_paths = _load_data(feature_files_paths, "VI data")

    # check if data is empty -> meaning that not at least one path worked
    if data is None:
        raise ValueError('For the given parameters, no data can be retrieved. '
                         'Please check the parameters and the official greenhub.ai documentation.')

    # inform user about missing years
    fetched_years = set(data['Year'].to_list())
    expected_years = set(range(start_year, end_year + 1))
    missing_years = expected_years - fetched_years
    if missing_years:
        print(f"Attention: no VI data found for {', '.join([str(i) for i in missing_years])} {WARNING_COLOR_PRINT}")

    return data


def get_climate_data(
        country: str,
        start_year: int,
        end_year: int = None,
        spatial_resolution: str = 'country',
        time_resolution: str = 'monthly',
) -> pd.DataFrame:
    """
    This function returns all available climate feature data on greenhub.ai for a specific `country` (e.g., US, BR)
    and year (`start_year`). By default, the climate data is aggregated at the country level and on a monthly basis,
    but with the `spatial_resolution parameter`, one can choose between 'country', 'state', and 'municipality'
    and the `time_resolution` parameter can be set to 'monthly', 'weekly', or 'daily'.
    Additionally, multiple years can be requested at once by specifying a time period by defining
    `start_year` **and** `end_year`.
    For more information please check out the official greenhub.ai documentation.

    :param country: country for which data is loaded, represented by a two-letter country code (e.g. US)
    :param start_year: year for which data is loaded; if `end_year` is also defined, then `start_year` is the
        first year of the time interval for which data is loaded
    :param end_year: if defined, `end_year` is the last year of the time interval, defined by `start_year` and
        `end_year`, for which data is loaded
    :param spatial_resolution: spatial resolution on which the data is aggregated; set to 'country' by default;
        can be set to 'country', 'state', or 'municipality'
    :param time_resolution: time resolution on which the data is aggregated; set to 'monthly' by default;
        can be set to 'monthly', 'weekly', or 'daily'
    :returns: dataframe containing the loaded and concatenated data
    """

    # parameter None/default handling and preprocessing
    if end_year is None:
        end_year = start_year
    spatial_resolution = spatial_resolution.lower()

    # check if greenhub api is initialized
    fdc = get_fdc()
    user_api_key = get_user_api_key()
    if fdc is None or user_api_key is None:
        raise Exception('Please use greenhub.initialize() before requesting data.')

    # some obvious/important parameter checks
    if len(country) != 2:
        raise ValueError('The country must be represented by a two-letter country code (e.g. US).')
    if start_year > end_year:
        raise ValueError('The end_year must be greater than or equal to the start_year.')
    if spatial_resolution not in SPATIAL_RESOLUTIONS:
        raise ValueError(f'The given spatial_resolution is not known. '
                         f'These spatial_resolutions are available: {", ".join(SPATIAL_RESOLUTIONS)}.')
    if time_resolution not in TIME_RESOLUTIONS:
        raise ValueError(f'The given time_resolution is not known. '
                         f'These time_resolution are available: {", ".join(TIME_RESOLUTIONS)}.')

    # construct all data files paths needed for the requested vi data
    feature_files_paths = []
    base_path = f'featureData/{country.upper()}/cds/{spatial_resolution}/{time_resolution}'
    for y in range(start_year, end_year + 1):
        if time_resolution in ['monthly', 'daily']:
            for m in range(1, 13):
                feature_files_paths.append(f'{base_path}/{y}-{str(m).zfill(2)}.csv')
        if time_resolution == 'weekly':
            for w in range(1, 54):
                feature_files_paths.append(f'{base_path}/{y}-week-{str(w).zfill(2)}.csv')

    if not feature_files_paths:
        raise ValueError('For the given parameters, no data can be retrieved. '
                         'Please check the parameters and the official greenhub.ai documentation.')

    # load and fetch data as one combined dataframe
    data, invalid_paths = _load_data(feature_files_paths, "Climate data")

    # check if data is empty -> meaning that not at least one path worked
    if data is None:
        raise ValueError('For the given parameters, no data can be retrieved. '
                         'Please check the parameters and the official greenhub.ai documentation.')

    # inform user about missing years
    fetched_years = set(data['Year'].to_list())
    expected_years = set(range(start_year, end_year + 1))
    missing_years = expected_years - fetched_years
    if missing_years:
        print(f"Attention: no Climate data found for {', '.join([str(i) for i in missing_years])} {WARNING_COLOR_PRINT}")

    return data


SOIL_LAYERS: [str] = [f'D{i}' for i in range(1, 8)]

def get_soil_data(
        country: str,
        spatial_resolution: str = 'country',
        layer: str = None
) -> pd.DataFrame:
    """
    This function returns all available soil feature data on greenhub.ai for a specific `country` (e.g., US, BR)
    and year (`start_year`). By default, only VI data aggregated at the country level is returned,
    but with the `spatial_resolution parameter`, one can choose between 'country', 'state', and 'municipality'.
    Further, all 7 layers are returned by default. If one is only interested in one single layer, one can set the
    `layer` parameter to the specific layer, like for example 'D5'.
    For more information please check out the official greenhub.ai documentation.

    :param country: country for which data is loaded, represented by a two-letter country code (e.g. US)
    :param spatial_resolution: spatial resolution on which the data is aggregated; set to 'country' by default;
        can be set to 'country', 'state', or 'municipality'
    :param layer: layer for which data is loaded; can be set to 'D1' up to 'D7'; set to None which loads all layers
    :returns: dataframe containing the loaded and concatenated data
    """

    # parameter None/default handling and preprocessing
    spatial_resolution = spatial_resolution.lower()
    layers = [layer.upper()] if layer is not None else SOIL_LAYERS

    # check if greenhub api is initialized
    fdc = get_fdc()
    user_api_key = get_user_api_key()
    if fdc is None or user_api_key is None:
        raise Exception('Please use greenhub.initialize() before requesting data.')

    # some obvious/important parameter checks
    if len(country) != 2:
        raise ValueError('The country must be represented by a two-letter country code (e.g. US).')
    if any([l not in SOIL_LAYERS for l in layers]):
        raise ValueError("The layer must be None (loading all layers) or set to 'D1' up to 'D7'.")

    # construct all data files paths needed for the requested vi data
    feature_files_paths = []
    base_path = f'featureData/{country.upper()}/soil/{spatial_resolution}'
    for l in layers:
        feature_files_paths.append(f'{base_path}/layer_{l}.csv')

    if not feature_files_paths:
        raise ValueError('For the given parameters, no data can be retrieved. '
                         'Please check the parameters and the official greenhub.ai documentation.')

    # load and fetch data as one combined dataframe
    data, invalid_paths = _load_data(feature_files_paths, "Soil data")

    # TODO add column "Layer"

    # check if data is empty -> meaning that not at least one path worked
    if data is None:
        raise ValueError('For the given parameters, no data can be retrieved. '
                         'Please check the parameters and the official greenhub.ai documentation.')

    return data
