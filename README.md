# 📊 Pipeline de Big Data & Dashboard IoT — UniFECAF

Projeto de Engenharia e Análise de Dados desenvolvido para a UniFECAF, focado na ingestão, processamento relacional e visualização interativa de um dataset de telemetria de sensores IoT (~97 mil registros).

---

## 🚀 Sobre o Projeto
O objetivo principal deste projeto é demonstrar um pipeline de Big Data de ponta a ponta:
1. **Infraestrutura em Contêineres:** Banco de dados PostgreSQL gerenciado via Docker / Docker Compose.
2. **Camada de Processamento Analítico:** Modelação e consolidação de métricas através de **Views SQL** otimizadas.
3. **Visualização de Dados (BI):** Dashboard interativo construído com **Streamlit** e gráficos dinâmicos em **Plotly**.

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python (Pandas, Plotly, SQLAlchemy)
* **Banco de Dados:** PostgreSQL
* **Infraestrutura:** Docker & Docker Compose
* **Visualização:** Streamlit
* **Controle de Versão:** Git & GitHub

---

## ⚙️ Arquitetura do Banco de Dados (Views SQL)
Para otimizar as consultas e garantir alta performance na renderização dos painéis, foram implementadas 4 Views analíticas no PostgreSQL:

1. `temp_por_ambiente`: Comparativo da temperatura média entre ambientes internos e externos (`In` vs `Out`).
2. `leituras_por_hora`: Agregação temporal da volumetria de leituras ao longo das 24 horas do dia.
3. `temp_max_min_por_dia`: Registro das variações térmicas extremas (máximas e mínimas) por data.
4. `avg_temp_por_dispositivo`: Média de temperatura consolidada por dispositivo/sensor IoT.

---

## 📈 Dashboard Interativo (Streamlit)
O painel apresenta 4 visualizações analíticas em tempo real:
* 🌡️ **Média por Ambiente** (Gráfico de Barras)
* ⏰ **Volume de Leituras por Hora** (Gráfico de Linhas)
* 📈 **Temperaturas Máximas e Mínimas Diárias** (Gráfico Múltiplo)
* 📊 **Média de Temperatura por Dispositivo** (Gráfico de Barras)

---

## 💻 Como Executar o Projeto

1. **Subir a Infraestrutura (PostgreSQL no Docker):**
   ```bash
   docker compose up -d