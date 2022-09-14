from re import S
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", "Climate Score", "Carbon Intensity"],
#         default_index=0)
#     st.write(f"You are now on: {selected}")
#     if selected == "Climate Score":
#         pass

# CSS = """
# .css-1v0mbdj{
#     padding-top: 400px;
# }
# """
# st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)
with st.sidebar.container():
    for i in range(25):
        st.write("")
    st.image("images/green-wagon.png")
st.title("Forecasting carbon emissions to limit global warming")

st.write("Some texts on global warming")

st.write("Some texts on our methodology")

st.write("Some explanation on our model")
