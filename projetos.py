import pandas as pd  
import matplotlib.pyplot as plt
import streamlit as st
import ipeadatapy as ip

st.set_page_config(

page_title="ListaEx4",
page_icon="👺", 
)

st.header("Exercícios")

st.write("Projetos Ex 1")

arquivo = "https://raw.githubusercontent.com/pedrohpaa/Exe4/main/projetos-1.csv" 
df = pd.read_csv(arquivo, sep=';') 
st.dataframe(df.head(23))

st.write("Projetos Ex 2")

df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
st.dataframe(df.tail())

st.write("Projetos Ex 3")

colunas = ['Projeto1', 'Projeto2', 'Projeto3', 'Projeto4', 'Projeto5']
st.dataframe(df.groupby('ano')[colunas].sum())

st.write("Projetos Ex 4")

fig, ax = plt.subplots()
df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', color='darkgreen', marker='*', ax=ax)
st.pyplot(fig)

st.write("Projetos Ex 5")

fig, ax = plt.subplots()
df["Projeto1"].plot(kind = 'hist')
df["Projeto4"].plot(kind = 'hist')
st.pyplot(fig)

st.write("IPEADATA Ex 1")

selic = ip.metadata(name="Taxa de juros - Over / Selic - acumulada no mês")
selic

st.write("IPEADATA Ex 2")

selic2 = ip.timeseries('BM12_TJOVER12', yearGreaterThan=2021, yearSmallerThan=2024)
selic2

st.write("IPEADATA Ex 3")

fig, ax = plt.subplots()
ip.timeseries('BM12_TJOVER12', year=2021).plot("MONTH", "VALUE ((% a.m.))")
ip.timeseries('BM12_TJOVER12', year=2022).plot("MONTH", "VALUE ((% a.m.))")
st.pyplot(fig)
