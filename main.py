from re import S
import streamlit as st
# from streamlit_option_menu import option_menu

st.set_page_config(page_title="CarbonForecast: Tackling Global Warming Step by Step", page_icon="images/green-wagon.png", layout="wide", initial_sidebar_state="auto", menu_items=None)
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", "Climate Score", "Carbon Intensity"],
#         default_index=0)
#     st.write(f"You are now on: {selected}")
#     if selected == "Climate Score":
#         pass


with st.sidebar.container():
    for i in range(25):
        st.write("")
    st.image("images/green-wagon.png")
st.title("Forecasting carbon emissions to limit global warming")

st.write("Some texts on global warming")

st.write("Some texts on our methodology")

st.write("Some explanation on our model")
