def segment_bursts(df, peaks, threshold):
    bursts = []

    for p in peaks:
        start = p
        while start > 0 and df['smooth_flux'].iloc[start] > threshold:
            start -= 1

        end = p
        while end < len(df) - 1 and df['smooth_flux'].iloc[end] > threshold:
            end += 1

        bursts.append((start, p, end))

    return bursts