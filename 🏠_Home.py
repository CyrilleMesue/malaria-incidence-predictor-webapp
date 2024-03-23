import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time

# set page configurations
st.set_page_config(layout="wide")

# page title
st.title("Welcome to Malaria Incidence Prediction!!!")
st.write("""
In this project, we have implemented various regression models and obtained a Random Forest Model with a correlation score of 96.7% on the test data. The dataset encompasses information from 98 countries, which are highlighted in the map below. Comparing the two maps, it's evident that the model's predictions closely match the actual data, as the maps exhibit remarkable similarity across all years.    

You can choose to visualize a specific year of interest or opt for an animation feature to display the distribution of incidence, one year at a time.   

To make predictions on new data points, navigate to the "Make Predictions" page and follow the provided instructions.
""")

# load data
df = pd.read_csv("data/viz-data.csv")
st.session_state["df"] = df

# function definition
def plot_maps(year, run_annimation = False):
    
    if run_annimation:
        # plot original data
        fig = px.choropleth(df, locations="code",color="incidence", hover_name="country", 
                            color_continuous_scale=px.colors.sequential.Plasma,animation_frame="year",animation_group="code")
        fig.update_layout(
 automargin=True, yref='paper'),title_x=0.3,
            autosize=True,width=1100,height=600,margin=dict(l=10,r=50,b=1,t=1))
        st.plotly_chart(fig, use_container_width = True)


    # if no annimation
    else:
        # plot original data
        fig = px.choropleth(df[df.year == year], locations="code",color="incidence", hover_name="country", 
                            color_continuous_scale=px.colors.sequential.Plasma) 
        fig.update_layout(
            title=dict(text=f"Malaria Incidence in {year}", font=dict(size=30), automargin=True, yref='paper'),
            title_x=0.40, autosize=True,width=1100,height=600, margin=dict( l=10, r=50, b=1, t=1))
        st.plotly_chart(fig, use_container_width = True)
    
        # plot predicted data
        fig = px.choropleth(df[df.year == year], locations="code", color="predicted incidence",
                            hover_name="country", color_continuous_scale=px.colors.sequential.Plasma)
        fig.update_layout(
            title=dict(text=f"Predicted Malaria Incidence in {year}", font=dict(size=30), automargin=True, yref='paper'),
            title_x=0.2, autosize=True,width=1100,height=600,margin=dict(l=10,r=50,b=1,t=1))
        st.plotly_chart(fig, use_container_width = True)

# sidebar
min_year = df.year.min()
max_year = df.year.max()
year = st.sidebar.slider("Select Year", min_value=min_year, max_value=max_year, value=2020)
run_annimation = st.sidebar.button("Run Annimation")

# plot maps
plot_maps(year, run_annimation = run_annimation)
    


