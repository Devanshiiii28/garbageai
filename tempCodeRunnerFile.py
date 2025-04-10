import streamlit as st
import pickle
import os
from PIL import Image

# Load the model
model_path = "C:/Users/Devanshi Bansal/Desktop/garbage ai/greenai_garbage_model.pkl"
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

if model:
    features = [[landfills, disposals, recyclings, baskets, wastewater]]
    prediction = model.predict(features)[0]
    st.success(f"🧮 Predicted Garbage Ratio: {prediction:.4f}")
else:
    st.error("❌ Model file not found. Please train and export the model as greenai_garbage_model.pkl")

st.markdown("---")
st.header("🗺️ Visual Garbage Maps")

# Display available map images in grid layout
image_files = [f for f in os.listdir(".") if f.startswith("garbage_map_") and f.endswith(".png")]

if image_files:
    cols = st.columns(3)
    for i, img_file in enumerate(sorted(image_files)):
        with cols[i % 3]:
            st.image(Image.open(img_file), caption=img_file.replace("garbage_map_", "").replace("_", " ").replace(".png", ""), use_column_width=True)
else:
    st.info("No map images found. Ensure they are saved in the same directory as the Streamlit app.")
