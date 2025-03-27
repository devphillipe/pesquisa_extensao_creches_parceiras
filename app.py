import streamlit as st
import pandas as pd
import plotly.express as px

# Definir o caminho do arquivo (suba a planilha para o mesmo repositório do app)
file_path = "pesquisa_extensao_creches_parceiras.xlsx"

# Carregar a planilha Excel
@st.cache_data
def carregar_dados():
    return pd.read_excel(file_path)

df = carregar_dados()

# Contagem e porcentagem das respostas
capacidade_contagem = df['Sua creche tem capacidade para atender crianças até as 17h?'].value_counts()
capacidade_porcentagem = df['Sua creche tem capacidade para atender crianças até as 17h?'].value_counts(normalize=True) * 100

# Criando o gráfico de barras interativo usando Plotly
fig = px.bar(
    x=capacidade_contagem.index,
    y=capacidade_contagem.values,
    labels={'x': 'Resposta', 'y': 'Quantidade'},
    title="Capacidade das Creches para Atender Crianças até as 17h",
    text=capacidade_porcentagem.round(1).astype(str) + '%',
    color=capacidade_contagem.index,
    color_discrete_map={
        'Sim, sem restrições': '#2ECC71',  # Verde
        'Não temos condições no momento': '#E74C3C',  # Vermelho
        'Sim, mas com limitações (descrever abaixo)': '#F1C40F'  # Amarelo
    }
)

# Ajustes no layout do gráfico
fig.update_traces(
    textposition='outside',
    marker=dict(line=dict(color='#FFFFFF', width=1))
)

fig.update_layout(
    template='plotly_dark',
    xaxis_title='Resposta',
    yaxis_title='Quantidade',
    xaxis=dict(
        title_standoff=25,
        tickangle=0,
        automargin=True
    ),
    yaxis=dict(
        automargin=True,
        showgrid=True,
        gridcolor='rgba(255,255,255,0.2)'
    ),
    margin=dict(l=50, r=50, t=50, b=80),
    showlegend=False
)

# Interface do Streamlit
st.set_page_config(page_title="Dashboard das Creches", layout="wide")

# Título
st.title("📊 Dashboard de Capacidades das Creches")

# Exibir gráfico interativo
st.plotly_chart(fig, use_container_width=True)

# Exibir tabela com respostas das creches
st.subheader("📋 Respostas das Creches")
st.dataframe(df)