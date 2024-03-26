# import libraries
import streamlit as st
import pandas as pd
import numpy as np
from utils import load_object

# load models
model = load_object("artifacts/model.pkl")
preprocessor = load_object("artifacts/preprocessor.pkl")

# sidebar
st.sidebar.info("""
**Note:** The latitude and longitude fields are populated by default using coordinates of the chosen country. However, the longitudes and latitudes can be changed manually.
""")

if "df" not in st.session_state:
    df = pd.read_csv("data/viz-data.csv")
    st.session_state["df"] = df
countries = st.session_state["df"].country.unique()

# request inputs
col1, col2 = st.columns(2)
country = col1.selectbox("Select Country", countries)
default_longitude = st.session_state["df"].longitude[list(st.session_state["df"].country).index(country)]
default_latitude = st.session_state["df"].latitude[list(st.session_state["df"].country).index(country)]
year = col1.number_input("Insert a Year", value=None, placeholder="Type a number. e.g 2024")
longitude = col1.number_input("Insert a Longitude", value=default_longitude, placeholder="Type a number. e.g 15.827659")
latitude = col1.number_input("Insert a Latitude", value=default_latitude, placeholder="Type a number. e.g -0.228021")
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

