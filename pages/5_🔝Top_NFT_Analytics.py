from typing import Container
import pandas as  pd
import plotly.express as px
import streamlit as st 

st.set_page_config(page_title="Top NFTs",page_icon=":bar_chart:",layout="wide")

df = pd.read_excel("NFT_Top_Collections 1.xlsx")
fig = px.bar(df[0:99],x="Name",y="Volume_USD")
fig2 = px.bar(df[100:199],x="Name",y="Volume_USD")
fig3 = px.bar(df[200:299],x="Name",y="Volume_USD")
fig4 = px.bar(df[300:399],x="Name",y="Volume_USD")
fig5 = px.bar(df[400:499],x="Name",y="Volume_USD")
fig6 = px.bar(df[500:599],x="Name",y="Volume_USD")

st.header(body="Volume_USD vs Name")
c1,c2,c3 = st.columns(3)
with c1:
        st.plotly_chart(fig)
with c2:
        st.plotly_chart(fig2)
with c3:
        st.plotly_chart(fig3)
    
c4,c5,c6 = st.columns(3)
with c4:
        st.plotly_chart(fig4)
with c5:
        st.plotly_chart(fig5)
with c6:
        st.plotly_chart(fig6)

st.info(body="**BasisMarkets** and **Skeleton Crew Skulls** are with higher volume")

st.header(body="FLOOR PRICE_USD vs Name")

fig = px.bar(df[0:99],x="Name",y="Floor_Price_USD")
fig2 = px.bar(df[100:199],x="Name",y="Floor_Price_USD")
fig3 = px.bar(df[200:299],x="Name",y="Floor_Price_USD")
fig4 = px.bar(df[300:399],x="Name",y="Floor_Price_USD")
fig5 = px.bar(df[400:499],x="Name",y="Floor_Price_USD")
fig6 = px.bar(df[500:599],x="Name",y="Floor_Price_USD")

c1,c2,c3 = st.columns(3)
with c1:
        st.plotly_chart(fig)
with c2:
        st.plotly_chart(fig2)
with c3:
        st.plotly_chart(fig3)
    
c4,c5,c6 = st.columns(3)
with c4:
        st.plotly_chart(fig4)
with c5:
        st.plotly_chart(fig5)
with c6:
        st.plotly_chart(fig6)
        
st.info("**FLUFFY HEADERS** and **SUBWAY SKATERS** are with lowest floor price")

st.header(body="AVERAGE PRICE_USD vs NAME")

fig = px.bar(df[0:99],x="Name",y="Average_Price_USD")
fig2 = px.bar(df[100:199],x="Name",y="Average_Price_USD")
fig3 = px.bar(df[200:299],x="Name",y="Average_Price_USD")
fig4 = px.bar(df[300:399],x="Name",y="Average_Price_USD")
fig5 = px.bar(df[400:499],x="Name",y="Average_Price_USD")
fig6 = px.bar(df[500:599],x="Name",y="Average_Price_USD")

c1,c2,c3 = st.columns(3)
with c1:
        st.plotly_chart(fig)
with c2:
        st.plotly_chart(fig2)
with c3:
        st.plotly_chart(fig3)
    
c4,c5,c6 = st.columns(3)
with c4:
        st.plotly_chart(fig4)
with c5:
        st.plotly_chart(fig5)
with c6:
        st.plotly_chart(fig6)
        
st.info("**Stickwives of the StickVerse** is with least Average price")





st.header(body="Market Caps vs Name")

fig = px.bar(df[0:99],x="Name",y="Market_Cap_USD")
fig2 = px.bar(df[100:199],x="Name",y="Market_Cap_USD")
fig3 = px.bar(df[200:299],x="Name",y="Market_Cap_USD")
fig4 = px.bar(df[300:399],x="Name",y="Market_Cap_USD")
fig5 = px.bar(df[400:499],x="Name",y="Market_Cap_USD")
fig6 = px.bar(df[500:599],x="Name",y="Market_Cap_USD")

c1,c2,c3 = st.columns(3)
with c1:
        st.plotly_chart(fig)
with c2:
        st.plotly_chart(fig2)
with c3:
        st.plotly_chart(fig3)
    
c4,c5,c6 = st.columns(3)
with c4:
        st.plotly_chart(fig4)
with c5:
        st.plotly_chart(fig5)
with c6:
        st.plotly_chart(fig6)


st.info(body="**I'M AIKO** and **FLIPPIES** are with highest market caps")

st.header(body="Owners vs Name")

fig = px.line(df[0:99],x="Name",y="Owners")
fig2 = px.line(df[100:199],x="Name",y="Owners")
fig3 = px.line(df[200:299],x="Name",y="Owners")
fig4 = px.line(df[300:399],x="Name",y="Owners")
fig5 = px.line(df[400:499],x="Name",y="Owners")
fig6 = px.line(df[500:599],x="Name",y="Owners")

c1,c2,c3 = st.columns(3)
with c1:
        st.plotly_chart(fig,showgrid=False)
with c2:
        st.plotly_chart(fig2)
with c3:
        st.plotly_chart(fig3)
    
c4,c5,c6 = st.columns(3)
with c4:
        st.plotly_chart(fig4)
with c5:
        st.plotly_chart(fig5)
with c6:
        st.plotly_chart(fig6)

st.info("**SOLAMELEON** has highest number of owners")

st.header("Owner_Asset_Ratio vs NAME")
fig = px.line(df[0:99],x="Name",y="Owner_Asset_Ratio")
fig2 = px.line(df[100:199],x="Name",y="Owner_Asset_Ratio")
fig3 = px.line(df[200:299],x="Name",y="Owner_Asset_Ratio")
fig4 = px.line(df[300:399],x="Name",y="Owner_Asset_Ratio")
fig5 = px.line(df[400:499],x="Name",y="Owner_Asset_Ratio")
fig6 = px.line(df[500:599],x="Name",y="Owner_Asset_Ratio")

c1,c2,c3 = st.columns(3)
with c1:
        st.plotly_chart(fig,showgrid=False)
with c2:
        st.plotly_chart(fig2)
with c3:
        st.plotly_chart(fig3)
    
c4,c5,c6 = st.columns(3)
with c4:
        st.plotly_chart(fig4)
with c5:
        st.plotly_chart(fig5)
with c6:
        st.plotly_chart(fig6)

st.info("**EGO CLASH** is with lowest Owner_Asset_Ratio")

hide = """
      <style>
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
      header {visibility: hidden;}
      </style>
      """
st.markdown(hide,unsafe_allow_html=True)












    
    


