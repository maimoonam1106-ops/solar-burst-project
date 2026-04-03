from scipy.signal import savgol_filter

def apply_smoothing(df, window=11):
    df['smooth_flux'] = savgol_filter(df['flux'], window, 3)
    return df
