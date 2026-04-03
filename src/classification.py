def classify_flux(flux):
    if flux > 1e-4:
        return "X"
    elif flux > 1e-5:
        return "M"
    elif flux > 1e-6:
        return "C"
    else:
        return "B/A"

def classify_dataframe(df):
    df["Class"] = df["Peak Flux"].apply(classify_flux)
    return df
