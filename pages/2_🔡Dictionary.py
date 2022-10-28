import streamlit as st 
from PIL import Image

st.set_page_config(page_title="Dictionary",page_icon=":bar_chart:",layout="wide")

hide = """
      <style>
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
      header {visibility: hidden;}
      </style>
      """

st.title("Terms you need understand")
with st.container():
  c1,c2=st.columns(2)
  with c1:
      with st.container():
          st.header(body="NFT")
          st.info("NFT, known as non-fungible tokens (NFTs), these cryptographic assets are based on blockchain technology and have unique identification codes and metadata that set them apart from each other. Such tokens can be used as placeholders for real-world assets such as artwork and real estate.")
  with c2:
      with st.container():
          st.header(body="Blockchain")
          st.success("Blockchain is a system of recording information in a way that makes it difficult or impossible to change, hack, or cheat the system. A blockchain is essentially a digital ledger of transactions that is duplicated and distributed across the entire network of computer systems on the blockchain.")

with st.container():
    c1,c2=st.columns(2)
    with c1:
        with st.container():
            st.header(body="Floor Price")
            st.success("The easiest way to calculate an NFT floor price is to take the lowest-priced NFT in a collection. For example, on Opensea, the Bored Ape Yacht Club (BAYC) NFT collection has a floor price of 72.69 ETH because that is the lowest listed price for a BAYC NFT on the marketplace")
            st.success("Buying NFTs at their floor price isn't a bad idea as you can obtain them at their lowest possible price and sell them off for a higher price. The downside of this is that the floor price often falls further after an NFT project sells out")
    with c2:
        with st.container():
            st.header("Average Price")
            st.info("NFTs are minted on different blockchains, their prices vary from one to another, and even when on the same blockchain, the cost of one NFT may not exactly be the same as another. This, however, can be attributed to a lot of factors including, quality of project, data size, transaction speed and gas fee, among other things.With respect to price, the average cost of an NFT is further determined by rarity, which means, in addition to the factors that have been mentioned earlier, the price of an NFT can shoot up based on law of scarcity.")
with st.container():
    c1,c2=st.columns(2)
    with c1:
        with st.container():
            st.header("NFT Miniting")
            st.info("For those who are not familiar with the space, NFT minting is the process of converting an art piece or collectable into a unique item. As simple as that, however, there is perhaps more to how that works, which is exactly what we will try to explain after now.")
            st.info("For individual art pieces or collectables to become a unique NFT, it has to first be ‘minted’ which implies it has to undergo a process where it bears a blockchain element.This could also mean that the art piece or collectable has to be hosted on a blockchain whereby it can be encrypted with a unique code that enables personalised ownership.")
    with c2:
        with st.container():
            st.header("Volume")
            st.success("Volume traded” refers to the amount of currency (e.g. ETH) exchanged for that particular collection over the NFT project’s lifetime. Volume traded is a good indicator of the number of people aware of a project as it reveals the money spent on the project. Established collections have high volume traded values")
with st.container():
    c1,c2=st.columns(2)
    with c1:
        with st.container():
            st.header("Market Cap")
            st.success("A high estimated market cap means that there are more owners of the tokens and they may be willing to pay a higher price to acquire the NFT collection from one another. This can be calculated by multiplying its 7-day average price by its total supply.")
    with c2:
        with st.container():
            st.header("Royalty")
            st.info("The way the royalties work in the context of NFTs is that when an artist or a person who's creating the NFT initially sets it up, they could build into the code by way of something called a “smart contract” a method of pushing a portion of the resale proceeds back to the original creator")

