import streamlit as st
import pandas as pd
import plotly.express as px

# Importando tabela
tabela = pd.read_csv("vendas.csv")

# Criando a tela do sistema
st.write("# Sistema de Vendas")

# Sidebar
st.sidebar.write("## Cadastrar Vendas")

data = st.sidebar.date_input('Data') # Calendário interativo
vendedor = st.sidebar.selectbox('Vendedor',['Angelo', 'Bernardo', 'Cassio', 'Daniel']) #Lista suspensa com opções limitadas
produto = st.sidebar.selectbox('Produto',['Notebook', 'PS5', 'RTX 5090'])
quantidade = st.sidebar.number_input('Quantidade',step=1) #Campo numérico podendo aumentar ou diminuir de 1 em 1
valor = st.sidebar.number_input('Valor') #Campo numérico comum
botao =st.sidebar.button('Cadastrar venda') #Quando clicado, recebe o valor True

if botao:
    nova_venda = [data, vendedor, produto, quantidade, valor] # Guarda todos os dados preenchidos
    tabela.loc[len(tabela)] = nova_venda #Adiciona a venda na próxima linha disponível. len(tabela) é o índice.
    tabela.to_csv('vendas.csv',index=False) #Salva a tabela atualizada
    st.success('Venda cadastrada!')

# Tabela interativa
st.write('## Vendas cadastradas')
st.dataframe(tabela)

# Dashboard
st.write("## Dashboard")
soma = tabela["valor"].sum() #Soma a coluna 'valor'
st.metric("Faturamento total", f"R${soma}") #Card visual
#Graficos
grafico = px.bar(tabela, x="vendedor", y="valor", color="produto") #Vendas por vendedor
st.plotly_chart(grafico)
grafico2 = px.pie(tabela,names="produto", values="valor")
st.plotly_chart(grafico2) #Participação por produto