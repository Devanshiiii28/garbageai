import streamlit as st
import pickle
import os
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from io import BytesIO

# Load the model
model_path = "greenai_garbage_model.pkl"
model = None
if os.path.exists(model_path):
    with open(model_path, "rb") as file:
        model = pickle.load(file)

# App configuration
st.set_page_config(page_title="GreenAI: Sustainable Building Tracker", layout="wide")
st.title("🏢 GreenAI: Sustainable Building Garbage Ratio Predictor")
st.markdown("Predict garbage impact and visualize local waste zones across Indian cities.")

st.sidebar.header("📊 Input Parameters")

# Input sliders
landfills = st.sidebar.slider("Number of Landfills", 0, 20, 2)
disposals = st.sidebar.slider("Waste Disposal Units", 0, 30, 3)
recyclings = st.sidebar.slider("Recycling Centers", 0, 30, 5)
baskets = st.sidebar.slider("Waste Baskets", 0, 50, 10)
wastewater = st.sidebar.slider("Wastewater Plants", 0, 10, 1)

# Theme toggle
dark_mode = st.sidebar.checkbox("🌙 Enable Dark Mode")

if dark_mode:
    st.markdown("""
    <style>
    body { background-color: #1E1E1E; color: white; }
    .stButton>button { background-color: #333; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Predict button
if st.button("🔍 Predict Garbage Ratio") and model:
    features = pd.DataFrame([{
        "landfills": landfills,
        "disposals": disposals,
        "recyclings": recyclings,
        "baskets": baskets,
        "wastewater": wastewater
    }])
    prediction = model.predict(features)[0]
    st.success(f"🧮 Predicted Garbage Ratio: {prediction:.4f}")

    # Export buttons
    csv = features.copy()
    csv["Predicted Garbage Ratio"] = prediction
    csv_file = csv.to_csv(index=False).encode()
    st.download_button("⬇️ Download CSV", data=csv_file, file_name="greenai_prediction.csv", mime="text/csv")

    # PDF export (as image-based workaround)
    fig_export, ax_export = plt.subplots()
    labels = ['Landfills', 'Disposals', 'Recyclings', 'Baskets', 'Wastewater']
    values = [landfills, disposals, recyclings, baskets, wastewater]
    ax_export.bar(labels, values, color='green')
    ax_export.set_title("Garbage Infrastructure Breakdown")

    buffer = BytesIO()
    fig_export.savefig(buffer, format="pdf")
    buffer.seek(0)
    st.download_button("🧾 Export PDF Report", buffer, file_name="greenai_report.pdf", mime="application/pdf")

    # Bar chart visualization
    st.subheader("📊 Garbage Infrastructure Breakdown")
    fig_bar, ax_bar = plt.subplots()
    ax_bar.bar(labels, values, color=['#4CAF50', '#2196F3', '#FF9800', '#9C27B0', '#00BCD4'])
    ax_bar.set_ylabel('Count')
    st.pyplot(fig_bar)

    # Pie chart visualization
    st.subheader("🧩 Proportional Distribution of Infrastructure")
    fig_pie, ax_pie = plt.subplots()
    ax_pie.pie(values, labels=labels, autopct='%1.1f%%', colors=['#4CAF50', '#2196F3', '#FF9800', '#9C27B0', '#00BCD4'])
    ax_pie.axis('equal')
    st.pyplot(fig_pie)

    # Comparison with city averages (example values)
    st.subheader("📍 Comparison with City Averages")
    city_avg = np.array([5, 10, 12, 25, 3])
    user_vals = np.array(values)

    fig_cmp, ax_cmp = plt.subplots()
    bar_width = 0.35
    x = np.arange(len(labels))
    ax_cmp.bar(x - bar_width/2, city_avg, width=bar_width, label='City Avg', color='gray')
    ax_cmp.bar(x + bar_width/2, user_vals, width=bar_width, label='Your Input', color='green')
    ax_cmp.set_xticks(x)
    ax_cmp.set_xticklabels(labels)
    ax_cmp.legend()
    ax_cmp.set_ylabel("Count")
    st.pyplot(fig_cmp)

    # Simulated Historical Trends
    st.subheader("📈 Simulated Historical Garbage Trend")
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    garbage_trend = np.random.uniform(0.2, 0.7, size=6)

    fig_hist, ax_hist = plt.subplots()
    ax_hist.plot(months, garbage_trend, marker='o', linestyle='-', color='orange')
    ax_hist.set_ylabel("Garbage Ratio")
    ax_hist.set_xlabel("Month")
    st.pyplot(fig_hist)

elif not model:
    st.error("❌ Model file not found. Please train and export the model as greenai_garbage_model.pkl")

st.markdown("---")
st.header("🗺️ Visual Garbage Maps")

# Display available map images
image_files = [f for f in os.listdir(".") if f.startswith("garbage_map_") and f.endswith(".png")]

if image_files:
    cols = st.columns(3)
    for i, img_file in enumerate(sorted(image_files)):
        with cols[i % 3]:
            st.image(Image.open(img_file), caption=img_file.replace("garbage_map_", "").replace("_", " ").replace(".png", ""), use_column_width=True)
else:
    st.info("No map images found. Ensure they are saved in the same directory as the Streamlit app.")
