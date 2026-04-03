import pandas as pd

def extract_features(df, bursts):
    features = []

    for start, peak, end in bursts:
        rise = (df['time_tag'].iloc[peak] - df['time_tag'].iloc[start]).total_seconds()
        decay = (df['time_tag'].iloc[end] - df['time_tag'].iloc[peak]).total_seconds()
        duration = (df['time_tag'].iloc[end] - df['time_tag'].iloc[start]).total_seconds()
        peak_flux = df['smooth_flux'].iloc[peak]

        features.append([rise, decay, duration, peak_flux])

    return pd.DataFrame(features, columns=["Rise", "Decay", "Duration", "Peak Flux"])
