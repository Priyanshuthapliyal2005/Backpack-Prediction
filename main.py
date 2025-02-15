import streamlit as st
import pandas as pd
from xgboost import XGBRegressor
from sklearn.preprocessing import LabelEncoder

st.title("Backpack Price Prediction App")

# Load the saved model
@st.cache_resource
def load_model():
    model = XGBRegressor()
    model.load_model('xgboost_model.json')
    return model
    
model = load_model()

# Create input fields for all the required features
st.subheader("Enter Backpack Features:")

# Define categorical feature encodings
brand_options = ['Brand A', 'Brand B', 'Brand C']
material_options = ['Nylon', 'Polyester', 'Canvas', 'Leather']
size_options = ['Small', 'Medium', 'Large']
style_options = ['Casual', 'Business', 'Travel', 'Sports']
color_options = ['Black', 'Blue', 'Gray', 'Red']

# User selections
brand = st.selectbox("Brand", brand_options)
material = st.selectbox("Material", material_options)
size = st.selectbox("Size", size_options)
style = st.selectbox("Style", style_options)
color = st.selectbox("Color", color_options)
compartments = st.number_input("Number of Compartments", min_value=1, max_value=10, value=3)
laptop_compartment = 1 if st.checkbox("Has Laptop Compartment") else 0
waterproof = 1 if st.checkbox("Is Waterproof") else 0
weight_capacity = st.slider("Weight Capacity (kg)", min_value=0.0, max_value=30.0, value=15.0, step=0.5)

# Encode categorical features
def encode_feature(value, options):
    return options.index(value)  # Convert category to numerical index

encoded_features = {
    'Brand': encode_feature(brand, brand_options),
    'Material': encode_feature(material, material_options),
    'Size': encode_feature(size, size_options),
    'Compartments': compartments,
    'Laptop Compartment': laptop_compartment,
    'Waterproof': waterproof,
    'Style': encode_feature(style, style_options),
    'Color': encode_feature(color, color_options),
    'Weight Capacity (kg)': weight_capacity
}

# Optional: Let user enter an ID
item_id = st.text_input("Item ID (optional)", value="")

# Predict Price
if st.button("Predict Price"):
    input_data = pd.DataFrame([encoded_features])  # Convert dictionary to DataFrame
    predicted_price = model.predict(input_data)[0]  # Get prediction

    # Display result
    st.success(f"The predicted price is: ${predicted_price:.2f}")

    # If Item ID is provided, format and allow download
    if item_id:
        result = f"{item_id},{predicted_price:.2f}"
        st.code(result, language="text")
        st.download_button(
            label="Download Prediction",
            data=result,
            file_name="prediction.csv",
            mime="text/csv"
        )
