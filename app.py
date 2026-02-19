import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("house_rent_model.pkl")

# -----------------------------
# Load Dataset
# -----------------------------
df_data = pd.read_csv("data/data.csv")

# Basic Cleaning (same as training)
df_data = df_data.drop_duplicates()
df_data = df_data[(df_data["rent"] > 0) & (df_data["area"] > 0)]

# Feature Engineering (same as training)
df_data["bhk"] = df_data["house_type"].str.extract(r'(\d+)').astype(float)
df_data["bhk"] = df_data["bhk"].fillna(df_data["beds"])
df_data = df_data.drop(columns=["house_type"])

# -----------------------------
# App Title
# -----------------------------
st.title("🏠 India House Rent Prediction & Recommendation System")

# ======================================================
# 🔵 RENT PREDICTION SECTION
# ======================================================
st.header("🔹 Rent Prediction")

cities = sorted(df_data["city"].unique())
city = st.selectbox("City", cities)

localities = sorted(df_data[df_data["city"] == city]["locality"].unique())
locality = st.selectbox("Locality", localities)

localities=sorted(df_data[df_data['city']==df_data])

area = st.number_input("Area (sqft)", 200, 10000, 800)
beds = st.number_input("Bedrooms", 1, 10, 2)
bathrooms = st.number_input("Bathrooms", 1, 10, 2)
balconies = st.number_input("Balconies", 0, 5, 1)

furnishing = st.selectbox(
    "Furnishing",
    ["Unfurnished", "Semi-Furnished", "Furnished"]
)

area_rate = st.number_input("Area Rate (₹ per sqft)", 5, 500, 25)

if st.button("Predict Rent"):
    input_df = pd.DataFrame([{
        "city": city,
        "locality": locality,
        "area": area,
        "beds": beds,
        "bathrooms": bathrooms,
        "balconies": balconies,
        "furnishing": furnishing,
        "area_rate": area_rate,
        "bhk": beds
    }])

    prediction = model.predict(input_df)[0]
    st.success(f"💰 Predicted Rent: ₹ {round(prediction, 2)}")

# ======================================================
# 🔵 RECOMMENDATION SECTION
# ======================================================
st.header("🏡 House Recommendation System")

budget = st.number_input("Your Budget (₹)", 5000, 200000, 20000)
min_area = st.number_input("Minimum Area (sqft)", 0, 5000, 700)

if st.button("Recommend Houses"):

    # Filter by city
    df_filtered = df_data[df_data["city"] == city]

    # Filter by locality
    df_filtered = df_filtered[df_filtered["locality"] == locality]

    # Filter by bedrooms
    df_filtered = df_filtered[df_filtered["beds"] == beds]

    # Filter by minimum area
    df_filtered = df_filtered[df_filtered["area"] >= min_area]

    # Filter by furnishing
    df_filtered = df_filtered[df_filtered["furnishing"] == furnishing]

    if df_filtered.empty:
        st.warning("No houses found with given preferences.")
    else:
        X_filtered = df_filtered.drop("rent", axis=1)
        df_filtered = df_filtered.copy()
        df_filtered["predicted_rent"] = model.predict(X_filtered)

        # Apply budget filter
        recommendations = df_filtered[
            df_filtered["predicted_rent"] <= budget
        ].sort_values("predicted_rent")

        if recommendations.empty:
            st.warning("No houses under your budget. Showing closest matches.")
            recommendations = df_filtered.sort_values("predicted_rent").head(5)
        else:
            recommendations = recommendations.head(5)

        st.subheader("Top Recommended Houses")
        st.dataframe(
            recommendations[
                ["locality", "area", "beds", "furnishing", "predicted_rent"]
            ]
        )
