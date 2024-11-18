import streamlit as st
import pandas as pd

st.title('Localização das comunidades quilombolas (2022)')
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')
#df.head()
#retirar a coluna unnamed
#converter as informações de localização geográficas para variáveis numéricas
df.drop(columns=['Unnamed: 0'], inplace=True)
list = ['Lat_d', 'Long_d']
#converter as informações de localização geográficas para variáveis numéricas
df[list] = df[list].apply(pd.to_numeric, errors='coerce')
estados = df['NM_UF'].unique()
estadoFiltro = st.selectbox(
    'Qual estado selecionar?',
     options=['Selecione o Estado'] + estados)
dadosFiltrados = df[df['NM_UF'] == estadoFiltro]
if st.checkbox('Mostrar tabela'):
  st.write(dadosFiltrados)
st.map(dadosFiltrados, latitude="Lat_d", longitude="Long_d")

#Estatística descritiva
qtdeMunicipios = len(df['NM_MUNIC'].unique())
#st.write("A quantidade de municípios brasileiros com localização quilombola é " + str(qtdeMunicipios))
st.metric('# Municípios', len(df['NM_MUNIC'].unique()))

qtdeComunidades = len(df['NM_AGLOM'].unique())
#st.write("A quantidade de comunidades quilombolas no Brasil é " + str(qtdeComunidades))
st.metric('# Comunidades', len(df['NM_AGLOM'].unique()))

