import requests
import pandas as pd
import streamlit as st

#Item 3
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome'
#identificando as mulheres 
requests.get(url)
response = requests.get(url).json()
dfmulheres = pd.DataFrame(response['dados'])
dfmulheres['sexo'] = 'F'

#identificando os homens
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'
requests.get(url)
response = requests.get(url).json()
dfhomens = pd.DataFrame(response['dados'])
dfhomens['sexo'] = 'M'

#unindo os dataframes 
df = pd.concat([dfmulheres, dfhomens])

#Item 5
opcao = st.selectbox(
    "Qual o sexo?",
    df['sexo'].unique()
)
dffiltrado = df[df['sexo'] == opcao]
st.title('Deputados do sexo' + opcao)

#Item 6
ocorrencias = dffiltrado['siglaUf'].value_counts()
dfestados = pd.DataFrame(ocorrencias)
dfestados.reset_index(inplace=True)
dfestados.columns = ['siglaUf', 'quantidade']
st.bar_chart(dffiltrado['siglaUf'].value_counts(),
             x_label= 'Sigla dos Estados',
             y_label= 'Quantidade de Deputados',
             use_container_width=True
             )

#Item 7
st.write('Total de deputados:', len(df))
st.write('Total de homens:', len(dfhomens))
st.write('Total de mulheres:', len(dfmulheres))
