import requests
import pandas as pd

def load_data():
    url = "https://services.swpc.noaa.gov/json/goes/primary/xrays-1-day.json"
    data = requests.get(url).json()

    df = pd.DataFrame(data)

    df['time_tag'] = pd.to_datetime(df['time_tag'])
    df = df[df['energy'] == '0.1-0.8nm']
    df = df.sort_values('time_tag')
    df = df.dropna()

    return df