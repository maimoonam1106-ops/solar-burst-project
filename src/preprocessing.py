def clean_data(df):
    df = df.dropna()
    df = df.sort_values('time_tag')
    return df
