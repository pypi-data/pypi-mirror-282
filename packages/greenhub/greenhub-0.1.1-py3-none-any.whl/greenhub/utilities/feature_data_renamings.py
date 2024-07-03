import pandas as pd

"""
TODO
"""


def vi_data_renaming(data: pd.DataFrame) -> pd.DataFrame:

    # columns renaming
    renamings = {
        'Fpar': 'FPAR',
        'NAME': 'Country',
        'GID_0': 'CountryCode',
        'GEOID': 'CountryCode',
    }
    data = data.rename(columns=renamings)

    # the `CountryCode` colum sometimes contains three-digit country codes -> can simply cut to two-digit codes
    data['CountryCode'] = data['CountryCode'].str.slice(0, 2)

    # the US vi data contains an unnecessary column `AFFGEOID`
    data = data.drop(columns=['AFFGEOID'], errors='ignore')

    # remove unnecessary column `COUNTRY`
    data = data.drop(columns=['COUNTRY'], errors='ignore')

    return data


def climate_data_renaming(data: pd.DataFrame) -> pd.DataFrame:

    # columns renaming
    renamings = {
        'Country': 'CountryCode',
        'COUNTRY': 'Country',
        'NAME': 'Country',
        'GID_0': 'CountryCode',
        'GEOID': 'CountryCode',
    }
    data = data.rename(columns=renamings)

    # the climate data contains an unnecessary column `Unnamed: 0`
    data = data.drop(columns=['Unnamed: 0'], errors='ignore')

    return data


def soil_data_renaming(data: pd.DataFrame) -> pd.DataFrame:

    # columns renaming
    renamings = {
        'GID_0': 'CountryCode',
    }
    data = data.rename(columns=renamings)

    # the `CountryCode` colum sometimes contains three-digit country codes -> can simply cut to two-digit codes
    data['CountryCode'] = data['CountryCode'].str.slice(0, 2)

    # remove unnecessary column `COUNTRY`
    data = data.drop(columns=['COUNTRY'], errors='ignore')

    return data