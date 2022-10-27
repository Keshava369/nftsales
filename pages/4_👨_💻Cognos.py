import streamlit as st 
from st_fn import st_button, load_css

st.set_page_config(page_title="COGNOS",page_icon=":bar_chart:",layout="wide")

load_css()

icon_size = 20

st.title(":cyclone: Analyse more on COGNOS")

st_button('IBM', 'https://keshava369.github.io/demodash/','cognos analytics', icon_size)

st.info('Login or sign up to explore more on cognos')

hide = """
      <style>
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
      header {visibility: hidden;}
      </style>
      """
st.markdown(hide,unsafe_allow_html=True)
