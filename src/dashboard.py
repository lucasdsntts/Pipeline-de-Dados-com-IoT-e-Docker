import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Configuração da conexão com o PostgreSQL no Docker
DB_USER = "postgres"
DB_PASS = "sua_senha"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

@st.cache_data
def load_data(view_name):
    query = f"SELECT * FROM {view_name}"
    return pd.read_sql(query, engine)

st.title("📊 Dashboard de Monitoramento IoT - UniFECAF")
st.markdown("Análise de dados de temperatura extraídos de sensores IoT e processados via PostgreSQL e Streamlit.")

# 1. Gráfico: Temperatura Média por Ambiente (Dentro vs Fora)
st.header("🌡️ Temperatura Média: Dentro (In) vs Fora (Out)")
try:
    df_ambiente = load_data("temp_por_ambiente")
    fig_ambiente = px.bar(
        df_ambiente, 
        x="ambiente", 
        y="avg_temp", 
        color="ambiente",
        labels={"ambiente": "Ambiente", "avg_temp": "Temperatura Média (°C)"},
        text_auto=".2f"
    )
    st.plotly_chart(fig_ambiente, use_container_width=True)
except Exception as e:
    st.warning("A view 'temp_por_ambiente' ainda não foi criada no DBeaver.")

# 2. Gráfico: Leituras por Hora
st.header("⏰ Volume de Leituras por Hora do Dia")
try:
    df_horas = load_data("leituras_por_hora")
    fig_horas = px.line(
        df_horas, 
        x="hora", 
        y="total_leituras", 
        markers=True,
        labels={"hora": "Hora do Dia", "total_leituras": "Total de Leituras"}
    )
    st.plotly_chart(fig_horas, use_container_width=True)
except Exception as e:
    st.warning("Erro ao carregar dados de leituras por hora.")

# 3. Gráfico: Temperaturas Máximas e Mínimas por Dia
st.header("📈 Temperaturas Máximas e Mínimas por Dia")
try:
    df_dias = load_data("temp_max_min_por_dia")
    fig_dias = px.line(
        df_dias, 
        x="data", 
        y=["temp_max", "temp_min"], 
        markers=True,
        labels={"value": "Temperatura (°C)", "data": "Data", "variable": "Métrica"}
    )
    st.plotly_chart(fig_dias, use_container_width=True)
except Exception as e:
    st.warning("Erro ao carregar dados diários.")

# 4. Gráfico: Temperatura Média por Dispositivo
st.header("📊 Temperatura Média por Dispositivo")
try:
    df_disp = load_data("avg_temp_por_dispositivo")
    
    # Identifica dinamicamente as colunas de ID e temperatura
    col_id = [c for c in df_disp.columns if c in ['id', 'room_id', 'noted_by', 'dispositivo']][0] if any(c in df_disp.columns for c in ['id', 'room_id', 'noted_by', 'dispositivo']) else df_disp.columns[0]
    col_temp = [c for c in df_disp.columns if 'temp' in c or 'avg' in c][0] if any('temp' in c or 'avg' in c for c in df_disp.columns) else df_disp.columns[1]

    fig_disp = px.bar(
        df_disp, 
        x=col_id, 
        y=col_temp, 
        color=col_id,
        labels={col_id: "Dispositivo / Sensor", col_temp: "Temperatura Média (°C)"},
        text_auto=".2f"
    )
    st.plotly_chart(fig_disp, use_container_width=True)
except Exception as e:
    st.warning(f"Erro ao carregar dados de temperatura por dispositivo: {e}")