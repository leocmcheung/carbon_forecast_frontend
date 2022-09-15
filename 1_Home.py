from re import S
import streamlit as st
# from streamlit_option_menu import option_menu

st.set_page_config(page_title="GreenWagon: Tackling Global Warming Step by Step", page_icon="images/green-wagon.png", layout="wide", initial_sidebar_state="auto", menu_items=None)
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", "Climate Score", "Carbon Intensity"],
#         default_index=0)
#     st.write(f"You are now on: {selected}")
#     if selected == "Climate Score":
#         pass

CSS = """

.css-1uii870 p{
    font-size:24px;
}


"""


st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

with st.sidebar.container():
    for i in range(25):
        st.write("")
    st.image("images/green-wagon.png")
st.title("GreenWagon - Estimating Company Carbon Emissions")
st.markdown("***")
for i in range(4):
    st.text("")
st.write("To start reducing carbon emissions, it is essential to understand how much we are emitting today.")
st.write("Corporate disclosure of greenhouse gas emissions is increasing but remain uncommon in all but a few sectors.")
for i in range(5):
    st.text("")
st.markdown("With our carbon estimator, you can calculate the **total emissions** and **emission intensity** (tonnes of carbon divided by revenue) of any company.")


for i in range(5):
    st.text("")
st.write("This carbon estimator is built from a machine learning model (XGBoost): using features such as revenue, number of employees,\
   percentage revenue from different activities, and other financial metrics, the model predicts the carbon intensity of the company.")
