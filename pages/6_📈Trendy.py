import streamlit as st 
from PIL import Image

st.set_page_config(page_title="Trend",page_icon=":bar_chart:",layout="wide")

st.title("Top 10 expensive NFTs")

with st.container():
     with st.container():
         c1,c2 = st.columns(2)
     with c1:
        i1 = Image.open("img/Everydays,_the_First_5000_Days.jpg")
        st.image(i1)
        st.info("Everydays: The First 5000 Days")
        st.success("$69.3 million")
        i3=Image.open("img/https___hypebeast.com_image_2021_11_beeple-human-one-christies-auction-1.jpg")
        st.image(i3)
        st.info("Human one")
        st.success("$28.9 million")
        i5 = Image.open("img/cp2.png")
        st.image(i5)
        st.info("CryptoPunk #7253")
        st.success("$11.7 million")
        i7= Image.open("img/ll.png")
        st.image(i7)
        st.info("CryptoPunk #4156")
        st.success("$10.2 million")
        i9=Image.open("img/ll3.jpeg")
        st.image(i9)
        st.info("CryptoPunk #3100")
        st.success("$7.57 million")
     with c2:
        i2 = Image.open("img\download.png")
        st.image(i2)
        st.info("clock")
        st.success("$52.7 million")
        i4=Image.open("img/cypto.png")
        st.image(i4)
        st.info("Crypto Punk #5822")
        st.success("$23.7 million")
        i6=Image.open("img/tp.png")
        st.image(i6)
        st.info("TPunk #3442")
        st.success("$10.5 million")
        i8=Image.open("img/ll2.png")
        st.image(i8)
        st.info("CryptoPunk #5577")
        st.success("$7.7 million")
        i10=Image.open("img/ll5.png")
        st.image(i10)
        st.info("CryptoPunk #7804")
        st.success("$7.56 million")
        
        
