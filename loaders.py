import pandas as pd
from ast import literal_eval

def load_countries():
    df = pd.read_csv('data/countries.csv')
    df = df.set_index('country_id')
    return df

def load_disciplines():
    df = pd.read_csv('data/disciplines.csv')
    df = df.set_index('discipline_id')
    df['eventList'] = df['eventList'].apply(literal_eval)

    return df

def load_events():
    df = pd.read_csv('data/events.csv')
    df = df.set_index('event_id')

    return df

def load_athletes():
    df = pd.read_csv('data/athletes.csv')
    df = df.set_index('athlete_id')
    df['dob'] = pd.to_datetime(df['dob'])
    df['eventList'] = df['eventList'].apply(literal_eval)
    df['disciplineList'] = df['disciplineList'].apply(literal_eval)

    return df

def load_medallists():
    df = pd.read_csv('data/medallists.csv')
    return df

def load_medal_table():
    df = pd.read_csv('data/medal_table.csv')
    return df