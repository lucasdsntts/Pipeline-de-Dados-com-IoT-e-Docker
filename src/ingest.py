import pandas as pd
from sqlalchemy import create_engine

# 1. Configurar a conexão com o PostgreSQL no Docker (com a senha 'sua_senha')
engine = create_engine('postgresql://postgres:sua_senha@localhost:5432/postgres')

# 2. Carregar o arquivo CSV correto usando o nome exato da sua estrutura: IOT-temp.csv
print("Lendo o arquivo CSV...")
df = pd.read_csv('data/IOT-temp.csv')

# Exibir as primeiras linhas para verificar se leu certo
print("Dados carregados com sucesso! Primeiras linhas:")
print(df.head())

# 3. Inserir os dados na tabela do banco de dados PostgreSQL
# Vamos nomear a tabela de destino como 'temperature_readings'
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("Dados inseridos com sucesso na tabela 'temperature_readings' do PostgreSQL!")