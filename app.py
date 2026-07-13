import os

import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# ----------------------------
# Load Model & Dataset
# ----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
DATA_PATH = os.path.join(BASE_DIR, "..", "House price ai.csv")

model = joblib.load(MODEL_PATH)

df = pd.read_csv(DATA_PATH)

# ----------------------------
# App Config
# ----------------------------

st.set_page_config(
    page_title="AI House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 AI House Price Prediction System")

st.markdown("Predict house prices using Machine Learning")

# ----------------------------
# Sidebar Inputs
# ----------------------------

st.sidebar.header("Enter Property Details")

area = st.sidebar.slider(
    "Area (sq.ft)",
    1000,
    10000,
    3000
)

bedrooms = st.sidebar.selectbox(
    "Bedrooms",
    [1,2,3,4,5,6]
)

bathrooms = st.sidebar.selectbox(
    "Bathrooms",
    [1,2,3,4]
)

stories = st.sidebar.selectbox(
    "Stories",
    [1,2,3,4]
)

parking = st.sidebar.selectbox(
    "Parking",
    [0,1,2,3]
)

# ----------------------------
# Prediction
# ----------------------------

if st.sidebar.button("Predict Price"):

    sample = [[
        area,
        bedrooms,
        bathrooms,
        stories,
        1,
        0,
        0,
        0,
        1,
        parking,
        0,
        1
    ]]

    prediction = model.predict(sample)

    st.success(
        f"🏷 Estimated House Price: ₹ {prediction[0]:,.0f}"
    )

    # AI Insight

    st.subheader("🤖 AI Insights")

    if area > 4000:
        st.info("Large property area increases value.")

    if parking >= 2:
        st.info("Extra parking positively impacts price.")

    if bedrooms >= 4:
        st.info("More bedrooms increase demand and price.")

# ----------------------------
# Dashboard Metrics
# ----------------------------

col1,col2,col3 = st.columns(3)

col1.metric(
    "Total Houses",
    len(df)
)

col2.metric(
    "Average Price",
    f"₹ {int(df['price'].mean()):,}"
)

col3.metric(
    "Average Area",
    f"{int(df['area'].mean())} sq.ft"
)

# ----------------------------
# Charts
# ----------------------------

st.subheader("📊 Market Insights")

fig1 = px.histogram(
    df,
    x="price",
    title="House Price Distribution"
)

st.plotly_chart(fig1, width='stretch')

fig2 = px.scatter(
    df,
    x="area",
    y="price",
    title="Area vs Price"
)

st.plotly_chart(fig2, width='stretch')

# ----------------------------
# Similar Houses
# ----------------------------

st.subheader("🏘 Sample Properties")

st.dataframe(
    df[['price','area','bedrooms','bathrooms']].head(10)
)