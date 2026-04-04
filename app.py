# ==============================
# IMPORTS
# ==============================
import streamlit as st
import numpy as np
import plotly.graph_objects as go

from src.data_loader import load_data
from src.smoothing import apply_smoothing
from src.peak_detection import detect_peaks
from src.segmentation import segment_bursts
from src.feature_extraction import extract_features
from src.classification import classify_dataframe

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(page_title="Solar Flare System", layout="wide")

# ==============================
# CUSTOM STYLING (PRO UI)
# ==============================
st.markdown("""
<style>
/* Background */
.main {
    background-color: #0e1117;
}

/* Title */
h1 {
    color: #00ffe1;
    text-align: center;
}

/* Subtext */
p {
    text-align: center;
    color: gray;
}

/* Metric cards */
[data-testid="metric-container"] {
    background-color: #1c1f26;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0px 0px 10px rgba(0,255,225,0.2);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Buttons */
.stButton>button {
    background-color: #00ffe1;
    color: black;
    border-radius: 8px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# HEADER
# ==============================
st.markdown("""
<h1>🌞 Solar Flare Intelligence System</h1>
<p>Real-time Detection • Classification • Simulation</p>
""", unsafe_allow_html=True)

# ==============================
# SIDEBAR SETTINGS
# ==============================
st.sidebar.header("⚙️ Settings")

window = st.sidebar.slider("Smoothing Window", 5, 21, 11)
threshold = st.sidebar.slider("Detection Threshold", 1e-8, 1e-4, 1e-6, format="%.1e")

# ==============================
# LOAD + PROCESS DATA
# ==============================
df = load_data()
df = apply_smoothing(df, window)

peaks = detect_peaks(df, threshold)
bursts = segment_bursts(df, peaks, threshold)

feature_df = extract_features(df, bursts)
feature_df = classify_dataframe(feature_df)

# ==============================
# METRICS DASHBOARD
# ==============================
col1, col2, col3 = st.columns(3)

col1.metric("📊 Data Points", f"{len(df):,}")
col2.metric("🔴 Peaks Detected", len(peaks))
col3.metric("🌟 Bursts Detected", len(bursts))

# ==============================
# CREATE GRAPH
# ==============================
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['time_tag'],
    y=df['smooth_flux'],
    mode='lines',
    name='Flux'
))

fig.add_trace(go.Scatter(
    x=df['time_tag'].iloc[peaks],
    y=df['smooth_flux'].iloc[peaks],
    mode='markers',
    marker=dict(color='red', size=6),
    name='Peaks'
))

# Highlight bursts
for start, peak, end in bursts:
    fig.add_vrect(
        x0=df['time_tag'].iloc[start],
        x1=df['time_tag'].iloc[end],
        fillcolor="yellow",
        opacity=0.3,
        line_width=0
    )

fig.update_layout(
    template="plotly_dark",
    title="Solar X-ray Flux Over Time",
    xaxis_title="Time",
    yaxis_title="Flux"
)

# ==============================
# TABS
# ==============================
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Visualization",
    "📊 Data",
    "🚨 Alerts",
    "🧪 Simulation"
])

# ==============================
# TAB 1: GRAPH
# ==============================
with tab1:
    st.plotly_chart(fig, use_container_width=True)

# ==============================
# TAB 2: DATA
# ==============================
with tab2:
    st.subheader("Extracted Features")
    st.dataframe(feature_df)

# ==============================
# TAB 3: ALERTS
# ==============================
with tab3:
    st.subheader("🚨 Live Alerts")

    if len(feature_df) == 0:
        st.success("✅ No major solar activity detected")
    else:
        for i, row in feature_df.iterrows():
            if row["Class"] == "X":
                st.error(f"🚨 X-Class Flare Detected (Burst {i+1})")
            elif row["Class"] == "M":
                st.warning(f"⚠️ M-Class Flare Detected (Burst {i+1})")
            else:
                st.info(f"ℹ️ C-Class Flare Detected (Burst {i+1})")

# ==============================
# TAB 4: SIMULATION (🔥)
# ==============================
with tab4:
    st.subheader("🧪 Solar Flare Simulation")

    st.markdown("Adjust parameters to simulate flare behavior")

    sim_flux = st.slider("Peak Flux", 1e-8, 1e-3, 1e-6, format="%.1e")
    sim_rise = st.slider("Rise Time (sec)", 10, 500, 100)
    sim_decay = st.slider("Decay Time (sec)", 10, 500, 200)

    # Classification
    def classify(flux):
        if flux > 1e-4:
            return "X"
        elif flux > 1e-5:
            return "M"
        elif flux > 1e-6:
            return "C"
        else:
            return "B/A"

    sim_class = classify(sim_flux)

    st.markdown(f"### 🔍 Predicted Class: **{sim_class}**")

    # Generate curve
    t = np.linspace(0, sim_rise + sim_decay, 200)

    y = np.piecewise(
        t,
        [t < sim_rise, t >= sim_rise],
        [
            lambda t: (t / sim_rise) * sim_flux,
            lambda t: sim_flux * np.exp(-(t - sim_rise) / sim_decay)
        ]
    )

    fig_sim = go.Figure()
    fig_sim.add_trace(go.Scatter(x=t, y=y, mode='lines', name="Simulated Flare"))

    fig_sim.update_layout(template="plotly_dark")

    st.plotly_chart(fig_sim, use_container_width=True)

# ==============================
# DOWNLOAD
# ==============================
st.subheader("📥 Download Results")

csv = feature_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="solar_bursts.csv",
    mime="text/csv"
)

# ==============================
# FOOTER
# ==============================
st.markdown("""
---
<div style='text-align:center; color:gray'>
🚀 Built for Hackathon | Solar Intelligence System ☀️
</div>
""", unsafe_allow_html=True)
