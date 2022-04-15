from matplotlib.pyplot import draw
import pandas as pd
import plotly.express as px
import streamlit as st
import math #netreba
from plotly import graph_objects


# 
st.set_page_config(page_title="Budget vizualizacia",
                   page_icon=":euro:",
                   layout="wide")

data_f = pd.read_csv("budgettest.csv", encoding="latin1", sep=";")
data_f["In"] = data_f["In"].astype(int)  #konvertujem data z pandas dataframe zo stringu na int lebo boli ako text 
data_f["Out"] = data_f["Out"].astype(int)

``
# bocna lista
st.sidebar.header("Filter") #nazov lavej strany

typ_vydavky = st.sidebar.multiselect(
    "Zvol druh vydavkov: ", options=data_f["Category"].unique(), default=data_f["Category"].unique()) #filter na streamlite co ti spravi filter element na strane a napoji s pandas na to co ma ukazovat v kategoriach


df_selection = data_f.query("Category == @typ_vydavky") #prepaja filter s pandas

# hlavny page

st.title("Budget vizualizacia")
st.markdown("##") #pouziva markdown symboly a language na jednoduche editovanie vzhladu


# hodnoty
# metoda sum na dataframe, spocita vsetko vo vybratych columns
total_vydavky = df_selection["Out"].astype(int).sum()
total_prijmy = df_selection["In"].sum() #nepouzil som nakoniec
# pocita priemer metodou pandas --> mean
priemernyv_zaden = round(df_selection["Out"].astype(int).mean(), 1)
priemernyz_zaden = round(df_selection["In"].astype(int).mean(), 1)

l_stlpec, s_stlpec, p_stlpec = st.columns(3)

with l_stlpec:  # ukazuje data hore, su napojene na filter
    st.subheader("Celkove vydavky:")
    st.subheader(f"EUR {total_vydavky}")
with s_stlpec:
    st.subheader("Priemerne prijmy:")
    st.subheader(f"EUR {priemernyz_zaden}")
with p_stlpec:
    st.subheader("Priemerne vydavky:")
    st.subheader(f"EUR {priemernyv_zaden}")

st.markdown('---')


# plotly
# data_f['Date'] = pd.to_datetime(data_f['Date'].dt.strftime('%m-%d-%Y'))

vydavky_graf1 = px.bar(data_frame=data_f,

                       x="Date",
                       y="Out",
                       orientation="v",
                       title="<b>Vydavky</b>",
                       color="Out",
                       template="ggplot2",
                       )
vydavky_graf1.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


st.markdown('#')  # formatuje vzhlad elementu
# z dokumentacie streamlit, vytvori jeden elemnt na celu width stranky
column_1 = st.container()
# metoda plotly_chart pouzije v streamlite kontainery graf z plotly
column_1.plotly_chart(vydavky_graf1, use_container_width=True)

st.markdown('#')