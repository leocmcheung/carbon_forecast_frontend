from re import S
import streamlit as st

st.set_page_config(layout="wide")

st.title("Estimating company carbon emissions")

st.write("To start reducing carbon emissions, it is essential to understand how much we are emitting today. Corporate disclosure of greenhouse gas emissions is increasing but remain uncommon in all but a few sectors.")

st.write("With our carbon estimator, you can calculate the total emissions and emission intensity (tonnes of carbon divided by revenue) of any company")

st.write("This carbon estimator is built from a machine learning model (XGBoost): using features such as revenue, number of employees,\
   percentage revenue from different activities, and other financial metrics, the model predicts the carbon intensity of the company.")
