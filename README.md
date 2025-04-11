# 🗑️ GreenAI Garbage Ratio Predictor

This Streamlit app predicts **garbage infrastructure impact** using ML and visualizes waste distribution across Indian cities.

## 🌟 Features

- 📌 Predict garbage ratio based on 5 key infrastructure inputs
- 📊 Visuals: bar chart, pie chart, city comparison, trend lines
- 🧾 Export predictions to CSV & PDF
- 🗺️ View local waste zone maps (static images)

## 📁 Files

- `app.py` – Streamlit interface
- `greenai_garbage_model.pkl` – Trained model
- `garbage_map_*.png` – Static garbage zone maps
- `requirements.txt` – App dependencies

## 🧠 Inputs

- Number of landfills
- Waste disposal units
- Recycling centers
- Waste baskets
- Wastewater plants

## 🖼️ Sample Output

- Predicted garbage ratio (e.g., 0.4231)
- Exported report with bar chart
- City map overlays (PNG images)

## 📦 Installation (Local)

```bash
pip install -r requirements.txt
streamlit run app.py
