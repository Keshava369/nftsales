import streamlit as st 
from PIL import Image

st.set_page_config(page_title="Home",page_icon=":bar_chart:",layout="wide")


st.title(":bar_chart:NFT SALES ANALYTICS")

st.header("Best tool for NFT analysis")
st.subheader(":thought_balloon:What you will get in this platform?")

st.info(body="NFT MARKET ANALYTICS",icon="💹")
st.info(body="Top NFTs Analytics",icon="🔝")
st.info(body="Different types of NFT bands",icon="⭐")
st.info(body="Dashboards made through Cognos",icon="📉")


st.header("Want to know about NFT?🤔")

with st.container():
    st.success(body="NFT, known as non-fungible tokens (NFTs), these cryptographic assets are based on blockchain technology and have unique identification codes and metadata that set them apart from each other. Such tokens can be used as placeholders for real-world assets such as artwork and real estate.")
    image1 = Image.open('img/image-8.jpg')
    image2 = Image.open('img/Bored.jpg')
    image3 = Image.open('img/Axie-Infinity.jpeg')
    c1,c2,c3 = st.columns(3)
    with c1:
        st.image(image1,caption="cryptopunk alien")
    with c2:
        st.image(image2,caption="Bored Ape")
    with c3:
        st.image(image3,caption="Axie Infinity")

st.info(body="Go through the FAQs and Dictionary page to understand more about NFT")
        
st.info(body="exprlore all the content through the side bar",icon="👈")

hide = """
      <style>
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
      header {visibility: hidden;}
      </style>
      """
st.markdown(hide,unsafe_allow_html=True)
