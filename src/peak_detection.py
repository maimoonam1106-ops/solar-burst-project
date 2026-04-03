from scipy.signal import find_peaks

def detect_peaks(df, threshold):
    peaks, _ = find_peaks(df['smooth_flux'], height=threshold)
    return peaks
