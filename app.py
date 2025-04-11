import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model
model = joblib.load('box_office_pipeline_model.pkl')

st.set_page_config(page_title="🎬 Box Office Revenue Predictor", layout="centered")

st.title("🎬 Movie Box Office Revenue Predictor")
st.markdown("Fill in the movie details to estimate worldwide box office revenue (USD).")

# User Inputs
distributor = st.text_input("Distributor", value="Warner Bros.")
mpaa = st.selectbox("MPAA Rating", ['G', 'PG', 'PG-13', 'R', 'NC-17', 'Not Rated'])
genre = st.text_input("Primary Genre", value="Action")
opening_theaters = st.number_input("Opening Theaters", min_value=1, step=1, value=3500)
release_days = st.number_input("Total Days in Theaters", min_value=1, step=1, value=90)

# Predict button
if st.button("Predict Revenue 💰"):
    # Create DataFrame
    input_df = pd.DataFrame([{
        'distributor': distributor,
        'MPAA': mpaa,
        'genres': genre,
        'opening_theaters': np.log1p(opening_theaters),
        'release_days': np.log1p(release_days)
    }])

    prediction = model.predict(input_df)
    predicted_revenue = np.expm1(prediction[0])

    st.success(f"💵 Predicted Worldwide Box Office Revenue: **${predicted_revenue:,.2f}**")
