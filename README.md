# Pipeline de Dados com IoT, Docker e Streamlit

Projeto desenvolvido para a disciplina de **Disruptive Architectures: IoT, Big Data e IA** da UniFECAF.

## 📋 Sobre o Projeto
Este projeto consiste na criação de um pipeline de dados completo para processar leituras de temperatura de dispositivos IoT. O fluxo abrange desde a ingestão dos dados brutos de um arquivo CSV (obtido no Kaggle), passando pelo armazenamento em um banco de dados relacional **PostgreSQL** executado via **Docker**, estruturação de **Views SQL** analíticas, até a visualização interativa em um dashboard desenvolvido com **Streamlit** e **Plotly**.

## 🛠️ Tecnologias Utilizadas
- **Python** (Pandas, SQLAlchemy, Psycopg)
- **Docker** & **PostgreSQL**
- **DBeaver** (Gerenciamento de banco de dados e criação de Views)
- **Streamlit** & **Plotly** (Dashboard interativo)
- **Git** & **GitHub**

## 📂 Estrutura do Projeto
```text
TRABALHO-DISRUPCTIVE/
│
├── data/
│   └── IOT-temp.csv              # Base de dados original (Kaggle)
├── src/
│   ├── ingest.py                 # Script Python de ingestão para o PostgreSQL
│   └── dashboard.py              # Aplicação web com Streamlit
├── sql/
│   └── views.sql                 # Scripts de criação das 3 Views SQL
└── README.md                     # Documentação do projeto