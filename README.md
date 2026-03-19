# 🌍 ClimateScope: Global Weather Analytics Dashboard

**Developed by:** Mudragada Swapna (Swapna-M)  
**Project Status:** ⚡ Final Submission (Milestones 1-3 Combined)
**Live Demo Link:** [Click here to view Dashboard](https://climatescopeweatherproject-cynfw8qijku9zvgcy7mrip.streamlit.app/)
---

## 🚀 Project Overview
ClimateScope is a high-performance interactive dashboard built with **Streamlit** to analyze global climate patterns. Using the **Global Weather Repository**, this application provides a centralized platform to monitor temperatures, humidity, and wind speeds across continents with real-time filtering capabilities.

---

## 🛠️ Tech Stack & Software Requirements

### 💻 Development Environment
* **Language:** Python 3.9+
* **Framework:** Streamlit (Web Interface)
* **IDE:** Visual Studio Code (VS Code)

### 📦 Key Libraries Used
* `pandas` — For Data Manipulation & Cleaning
* `plotly` — For Interactive Geo-spatial & Statistical Charts
* `streamlit` — For App Deployment & Sidebar UI

---

## 📋 Milestone Deliverables & Analysis Logic

### 🔹 Milestones 1 & 2: Statistical Foundation
* **📊 Global Metrics:** Automated calculation of Average Temperature, Humidity, and Pressure.
* **🍕 Weather Mix (Pie Chart):** Visualized the distribution of weather conditions (Sunny, Cloudy, etc.).
* **📉 Correlation Analysis:** Logic to study the relationship between Temperature and Humidity.
* **☀️ Regional Hierarchy:** Sunburst charts to drill down from Countries to Cities.

### 🔹 Milestone 3: Advanced Interactivity (Final Update)
1. **🌡️ Dynamic Temperature Slider:** * **Logic:** Side-bar range slider to filter data between specific climate windows.
   * **Impact:** Instant UI synchronization across all 7 charts.
2. **🔥 Automated "Hottest Spot" Detection:**
   * **Logic:** Used `.idxmax()` programming logic to scan filtered data and call out the extreme values in real-time.
3. **🗺️ Global Heatmap:**
   * **Logic:** Choropleth world map color-coded by real-time temperature values for spatial analysis.
4. **📥 Data Action Center:**
   * **Feature:** Added a specialized CSV download button to export filtered reports for offline study.

---

## 🔐 Access Credentials
To access the dashboard, use the following credentials:
* **👤 Username:** Swapna
* **🔑 Password:** 123

---

## 🏃 How to Run Locally
1. Clone the repository to your local machine.
2. Install requirements: `pip install -r requirements.txt`
3. Run the application: `streamlit run src/app.py`
  
