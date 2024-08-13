import pandas as pd
import numpy as np

def get_population_data(countries: list[str]) -> dict[str, int]:
    # Fetch population data from Wikipedia
    dfc = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)')[0]
    dfc = dfc.set_index('Country')
    dfc.index = dfc.index.str.split('[').str[0]

    # Map country names
    olympics2wikipedia = {
        'Cabo Verde': 'Cape Verde',
        'Chinese Taipei': 'Taiwan',
        'DPR Korea': 'North Korea',
        'Great Britain': 'United Kingdom',
        'Hong Kong, China': 'Hong Kong (China)',
        'IR Iran': 'Iran',
        'Korea': 'South Korea',
        'Republic of Moldova': 'Moldova',
        'Türkiye': 'Turkey',
        'Puerto Rico': 'Puerto Rico (United States)',
        "Côte d'Ivoire": 'Ivory Coast'
    }

    unmatched_country_names = set(countries) - set(dfc.index.unique().tolist()) - set(olympics2wikipedia.keys())
    print(f"{unmatched_country_names=}")

    # Ensure that we have a mapping for all unmatched country names
    assert len(unmatched_country_names) == 0

    results = {}
    for country in countries:
        if country in olympics2wikipedia:
            wikipedia_country = olympics2wikipedia[country]
            results[country] = dfc.loc[wikipedia_country, 'Population(1 July 2023)']
        else:
            results[country] = dfc.loc[country, 'Population(1 July 2023)']

    return results

def get_gdp_data(countries: list[str]) -> dict[str, float]:
    # Fetch gdp data from Wikipedia
    dfg = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)')[2]
    # Remove multi-index columns
    dfg.columns = dfg.columns.droplevel()

    dfg = dfg.set_index('Country/Territory')

    # Map country names
    olympics2wikipedia = {
        'Cabo Verde': 'Cape Verde',
        'Chinese Taipei': 'Taiwan',
        'DPR Korea': 'North Korea',
        'Great Britain': 'United Kingdom',
        'Hong Kong, China': 'Hong Kong',
        'IR Iran': 'Iran',
        'Korea': 'South Korea',
        'Republic of Moldova': 'Moldova',
        'Türkiye': 'Turkey',
        'Czechia': 'Czech Republic',
        "Côte d'Ivoire": 'Ivory Coast'
    }

    unmatched_country_names = set(countries) - set(dfg.index.unique().tolist()) - set(olympics2wikipedia.keys())
    print(f"{unmatched_country_names=}")

    # Ensure that we have a mapping for all unmatched country names
    assert len(unmatched_country_names) == 0

    results = {}
    for country in countries:
        if country in olympics2wikipedia:
            wikipedia_country = olympics2wikipedia[country]
            results[country] = dfg.loc[wikipedia_country, 'Forecast']
        else:
            results[country] = dfg.loc[country, 'Forecast']
    
    # Manually add missing countries
    results['Cuba'] = 633.4 * 1000
    results['DPR Korea'] = np.nan

    return results