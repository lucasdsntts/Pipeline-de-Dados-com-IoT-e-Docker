import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Configuração da conexão com o PostgreSQL no Docker
engine = create_engine('postgresql://postgres:sua_senha@localhost:5432/postgres')

# Função para carregar dados de uma view
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Título do dashboard
st.title('Dashboard de Temperaturas IoT')
st.markdown('Monitorização de leituras de temperatura de dispositivos IoT processadas via PostgreSQL e Docker.')

# Gráfico 1: Média de temperatura por dispositivo
st.header('Média de Temperatura por Dispositivo')
try:
    df_avg_temp = load_data('avg_temp_por_dispositivo')
    fig1 = px.bar(df_avg_temp, x='device_id', y='avg_temp', labels={'device_id': 'Dispositivo/Sala', 'avg_temp': 'Temperatura Média'})
    st.plotly_chart(fig1, use_container_width=True)
except Exception as e:
    st.error(f"Erro ao carregar os dados da view avg_temp_por_dispositivo: {e}")

# Gráfico 2: Contagem de leituras por hora
st.header('Leituras por Hora do Dia')
try:
    df_leituras_hora = load_data('leituras_por_hora')
    fig2 = px.line(df_leituras_hora, x='hora', y='contagem', markers=True, labels={'hora': 'Hora do Dia', 'contagem': 'Número de Leituras'})
    st.plotly_chart(fig2, use_container_width=True)
except Exception as e:
    st.error(f"Erro ao carregar os dados da view leituras_por_hora: {e}")

# Gráfico 3: Temperaturas máximas e mínimas por dia
st.header('Temperaturas Máximas e Mínimas por Dia')
try:
    df_temp_max_min = load_data('temp_max_min_por_dia')
    fig3 = px.line(df_temp_max_min, x='data', y=['temp_max', 'temp_min'], markers=True, labels={'data': 'Data', 'value': 'Temperatura', 'variable': 'Métrica'})
    st.plotly_chart(fig3, use_container_width=True)
except Exception as e:
    st.error(f"Erro ao carregar os dados da view temp_max_min_por_dia: {e}")