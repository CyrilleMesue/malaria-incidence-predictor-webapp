# import libraries
import streamlit as st
import pandas as pd
import numpy as np
from utils import load_object

# load models
model = load_object("artifacts/Random Forest_model.pkl")
preprocessor = load_object("artifacts/preprocessor.pkl")


if "df" not in st.session_state:
    df = pd.read_csv("data/viz-data.csv")
    countries = df.country.unique()

else:
    countries = st.session_state["df"].country.unique()
# request inputs
col1, col2 = st.columns(2)
country = col1.selectbox("Select Country", countries)
year = col1.number_input("Insert a Year", value=None, placeholder="Type a number. e.g 2024")
longitude = col1.number_input("Insert a Longitude", value=None, placeholder="Type a number. e.g 15.827659")
latitude = col1.number_input("Insert a Latitude", value=None, placeholder="Type a number. e.g -0.228021")
precipitation = col2.number_input("Insert a value for Precipitation", value=None, placeholder="Type a number. e.g 1516.01")
AvMeanSurAirTemp = col2.number_input("Insert a value for Average Mean Surface Air Temperature", value=None, placeholder="Type a number. e.g 24.0")
AvMaxSurAirTemp = col2.number_input("Insert a value for Average Maximum Surface Air Temperature", value=None, placeholder="Type a number. e.g 24.0")
AvMinSurAirTemp = col2.number_input("Insert a value for Average Minimum Surface Air Temperature", value=None, placeholder="Type a number. e.g 24.0")

# arrange data for prediction

X = pd.DataFrame({'year':[year], 
                  'country':[country], 
                  'precipitation':[precipitation], 
                  'AvMeanSurAirTemp':[AvMeanSurAirTemp],
                  'AvMaxSurAirTemp':[AvMaxSurAirTemp], 
                  'AvMinSurAirTemp':[AvMinSurAirTemp], 
                  'longitude':[longitude],
                  'latitude':[latitude],
                 })

st.write(X)

prediction = ""
if st.button("Predict Malaria Incidence"):
    prediction = model.predict(preprocessor.transform(X))[0]

st.write(f"The predicted malaria incidence is: **{prediction}**")

