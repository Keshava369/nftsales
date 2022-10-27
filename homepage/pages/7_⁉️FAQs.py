import streamlit as st 
from PIL import Image

st.set_page_config(page_title="FAQs",page_icon=":bar_chart:",layout="wide")

hide = """
      <style>
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
      header {visibility: hidden;}
      </style>
      """
st.markdown(hide,unsafe_allow_html=True)

st.title(body="What is an NFT?")
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

st.title(body="Where NFTs are used?")
with st.container():
    st.success(body="NFTs are used to represent digital and real-world items such as artwork and real estate, allowing these assets to be traded with a slight possibility of fraud")
    st.info(body="In the future, NFT-protected virtual identities will be able to use tokens as digital passports. Unlike their physical counterparts, they cannot be stolen, hacked, or counterfeited.")

st.title(body="Are NFTs a good investment? What is the risk of NFTs?")
with st.container():
    imagez= Image.open("img/wxy.jpg")
    st.image(imagez)
    st.success(body="NFTs can be categorized under the High Risk, High Reward investment type. The NFT market is fueled by scarcity and desirability which explains the craze people have about them.However, pundits warn potential investors — who are over-excited by the unimaginable prices NFTs are being sold — against staking their financial security on NFTs. Same as Initial Coin Offerings, there are high chances you can get scammed in NFTs. You also have to consider the fact that you don’t own the content of the NFTs when investing.Before you attempt to invest in NFTs, invest in knowing what you’re getting into. You need incredible knowledge in the cryptocurrency industry if you’re ever going to have a bleak chance of success.With NFTs, the philosophy of time and chance is a real thing. They are only worth the amount people are willing to pay for them.")

st.title(body="Where do you buy NFTs?")
with st.container():
    st.info("You must know that NFTs can only be bought with cryptocurrency (mostly with ether or ETH). However, some exchange platforms like Gemini, Kraken, and Coinbase allows user to convert U.S dollars to ether.Some of the best marketplaces where you can buy NFTs include OpenSea, Rarible, Axie Marketplace, and NBA Top Shot Marketplace.")

st.title("What is the future of NFTs?")
with st.container():
    images= Image.open("img/fnft.jpeg")
    st.image(images)
    st.success(body="OpenSea co-founder Alex Atallah said in an email that “the possibilities of NFTs are endless since they can be used to log ownership of any unique asset.” Using NFTs as event tickets, software licenses, fan club memberships, or other interactive experiences is already a common use case for NFTs.")
    st.info(body="There is a lot of potential for NFTs in the $85 billion video game industry. They’re already being tried out by some of the bigger studios. The metaverse, a virtual 3D world proposed by Meta (formerly Facebook) CEO Mark Zuckerberg and other tech industry heavyweights, could make use of NFTs as building blocks for a future digital universe.")
st.title("How many owners can there be for each NFT?")
with st.container():
    st.success("NFTs can have only one owner at a time. NFTs' unique data makes it easy to verify their ownership and transfer tokens between owners.")