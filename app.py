import streamlit as st

from src.data_loader import load_data
from src.smoothing import apply_smoothing
from src.peak_detection import detect_peaks
from src.segmentation import segment_bursts
from src.feature_extraction import extract_features
from src.classification import classify_dataframe
from src.plotter import create_plot

# -----------------------------
# TITLE
# -----------------------------
st.title("🌞 Solar X-ray Burst Detection System")

# -----------------------------
# LOAD DATA
# -----------------------------
df = load_data()

# -----------------------------
# PREPROCESS
# -----------------------------
window = st.slider("Smoothing Window", 5, 21, 11)
df = apply_smoothing(df, window)

# -----------------------------
# SETTINGS
# -----------------------------
threshold = st.slider("Detection Threshold", 1e-8, 1e-4, 1e-6, format="%.1e")

# -----------------------------
# DETECTION
# -----------------------------
peaks = detect_peaks(df, threshold)
bursts = segment_bursts(df, peaks, threshold)

# -----------------------------
# FEATURES + CLASSIFICATION
# -----------------------------
feature_df = extract_features(df, bursts)
feature_df = classify_dataframe(feature_df)

# -----------------------------
# VISUALIZATION
# -----------------------------
fig = create_plot(df, peaks, bursts)
st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# RESULTS
# -----------------------------
st.subheader("📊 Summary")
st.write("Peaks:", len(peaks))
st.write("Bursts:", len(bursts))

# -----------------------------
# TABLE
# -----------------------------
st.subheader("📐 Features")
st.dataframe(feature_df)

# -----------------------------
# ALERTS
# -----------------------------
st.subheader("🚨 Alerts")

for i, row in feature_df.iterrows():
    if row["Class"] == "X":
        st.error(f"🚨 X-Class Flare (Burst {i+1})")
    elif row["Class"] == "M":
        st.warning(f"⚠️ M-Class Flare (Burst {i+1})")
    elif row["Class"] == "C":
        st.info(f"ℹ️ C-Class Flare (Burst {i+1})")

# -----------------------------
# DOWNLOAD
# -----------------------------
csv = feature_df.to_csv(index=False).encode('utf-8')

st.download_button(
    "Download Results",
    csv,
    "results.csv",
    "text/csv"
)
