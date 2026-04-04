# 🌞 Solar Flare Intelligence System

## 🚀 Overview
The **Solar Flare Intelligence System** is a real-time data-driven web application designed to monitor, detect, analyze, and simulate solar flare activity using live satellite data from NOAA.

This system combines **signal processing**, **data analytics**, and **interactive visualization** to provide insights into solar flare behavior and intensity.

---

## 🌐 Live Application
🔗 https://solar-burst.streamlit.app/ 


---

## 🧠 Problem Statement
Solar flares can significantly impact:
- Satellite operations 📡  
- Communication systems 📶  
- Power grids ⚡  

However, detecting and analyzing these events in real-time requires automated and intelligent systems.

---

## 💡 Our Solution
We developed an end-to-end pipeline that:

- Fetches real-time solar X-ray data  
- Cleans and smooths noisy signals  
- Detects flare peaks using scientific methods  
- Segments complete flare bursts  
- Extracts meaningful features  
- Classifies flare intensity  
- Visualizes results interactively  
- Simulates flare behavior dynamically  

---

## 🎯 Key Features

### 📡 Real-Time Data Integration
- Uses NOAA SWPC API
- Continuously fetches live solar X-ray flux data

### 📈 Signal Processing
- Applies Savitzky-Golay filtering
- Reduces noise and enhances signal clarity

### 🔴 Peak Detection
- Detects solar flare peaks using `scipy.signal.find_peaks`

### 🌟 Burst Segmentation
- Identifies complete flare duration:
  - Start → Peak → End

### 📊 Feature Extraction
For each burst:
- Rise Time  
- Decay Time  
- Duration  
- Peak Flux  

### 🧠 Flare Classification
Based on peak intensity:
- **X-class** → Extreme  
- **M-class** → Moderate  
- **C-class** → Low  

### 🚨 Alert System
- Displays real-time alerts based on flare category

### 🧪 Simulation Module (Unique Feature)
- Allows users to simulate flare behavior  
- Adjust:
  - Peak flux  
  - Rise time  
  - Decay time  
- Instantly predicts flare class  

### 📥 Export Functionality
- Download processed results as CSV  

---

## 🛠️ Tech Stack

| Layer              | Technology |
|-------------------|-----------|
| UI / Frontend     | Streamlit |
| Data Processing   | Pandas, NumPy |
| Signal Processing | SciPy |
| Visualization     | Plotly |
| API Integration   | Requests |

---

## ⚙️ How It Works

1. **Data Fetching**
   - Retrieves live solar data from NOAA API  

2. **Preprocessing**
   - Filters required energy band  
   - Sorts and cleans data  

3. **Smoothing**
   - Applies Savitzky-Golay filter  

4. **Peak Detection**
   - Identifies local maxima above threshold  

5. **Segmentation**
   - Expands peaks into full burst regions  

6. **Feature Extraction**
   - Calculates temporal characteristics  

7. **Classification**
   - Assigns flare class based on intensity  

8. **Visualization**
   - Displays graph with peaks & bursts  

9. **Simulation**
   - Generates synthetic flare curves  

---

## 📂 Project Structure

solar-burst-project/
│
├── app.py
├── requirements.txt
├── README.md
│
└── src/
    ├── __init__.py
    ├── data_loader.py
    ├── smoothing.py
    ├── peak_detection.py
    ├── segmentation.py
    ├── feature_extraction.py
    ├── classification.py

---

## ▶️ Getting Started

### 1️⃣ Clone Repository
git clone https://github.com/maimoonam1106-ops/solar-burst-project.git  
cd solar-burst-project  

### 2️⃣ Install Dependencies
pip install -r requirements.txt  

### 3️⃣ Run Application
streamlit run app.py  

---

## 🧑‍💻 Usage Guide

1. Open the app in browser  
2. Adjust parameters in sidebar:
   - Smoothing window  
   - Detection threshold  
3. View:
   - 📈 Graph (flux vs time)  
   - 📊 Data table  
   - 🚨 Alerts  
4. Use simulation tab to:
   - Test custom flare scenarios  
5. Download results if needed  

---

## 🌍 Deployment

The application is deployed using **Streamlit Cloud**, making it:
- Globally accessible 🌐  
- Easy to share 📤  
- Scalable 🚀  

---

## 💡 Use Cases

- Space weather monitoring  
- Satellite safety analysis  
- Communication system protection  
- Scientific research  
- Educational demonstrations  

---

## 🔮 Future Enhancements

- 🤖 Machine learning-based flare prediction  
- 📲 SMS/Email alert integration  
- 📊 Multi-day trend visualization  
- 🌐 Integration with multiple space datasets  

---

## 👩‍💻 Authors

- Maimoona Anbara M
- Feric

---

## 🙌 Acknowledgements

- NOAA Space Weather Prediction Center (SWPC)  
- GOES Satellite Data  

---

## 📌 Conclusion

This project demonstrates a scalable and intelligent approach to solar flare detection, combining real-time data processing, scientific analysis, and interactive visualization into a unified platform.

---
