import pandas as pd
import sqlite3
# import numpy as np
# import matplotlib.pyplot as plt

def load_data(source_type, source_path):
    if source_type == 'csv':
        data = pd.read_csv(source_path)
    elif source_type == 'sql':
        conn = sqlite3.connect(source_path)
        data = pd.read_sql_query("SELECT * FROM my_table", conn)
    elif source_type == 'json':
        data = pd.read_json(source_path)
    else:
        raise ValueError(f"Unsupported source type: {source_type}")
    
    return data

# colunas_numericas = data.select_dtypes(include=['number']).columns
# colunas_textuais = data.select_dtypes(include=['object']).columns

# 1. Carregar os CSVs
# data2 = pd.read_csv('data/gym_members_exercise_tracking.csv')
# data1 = pd.read_csv('data/MentalHealthSurvey.csv')
# data = pd.read_csv('data/social-media.csv')
# data3 = pd.read_csv('data/covid-19 sp.csv')

# 2. Separar colunas numéricas e textuais


# print("Colunas numéricas:", colunas_numericas)
# print("Colunas textuais:", colunas_textuais)

# 3. Aplicar One-Hot Encoding às colunas textuais
# data_encoded = pd.get_dummies(data, columns=colunas_textuais)

# # 4. Calcular e exibir a melhor correlação entre todas as colunas numéricas
# resultado_correlacoes = {}

# # 6. Calcular correlação entre todas as colunas (numéricas e codificadas)
# # correlacoes = data_encoded.corr(method="kendall")
# correlacoes = data.select_dtypes(include=['number']).corr(method="kendall")

# # 7. Exibir o gráfico de correlação com os nomes das colunas
# plt.figure(figsize=(30, 24))  # Ajustar o tamanho do gráfico para caber os rótulos
# plt.matshow(correlacoes, fignum=1)  # Usar fignum=1 para integrar ao plt.figure

# # Adicionar rótulos de colunas e linhas
# plt.xticks(ticks=np.arange(correlacoes.shape[1]), labels=correlacoes.columns, rotation=90)
# plt.yticks(ticks=np.arange(correlacoes.shape[0]), labels=correlacoes.index)

# # Exibir barra de cores
# plt.colorbar()

# plt.show()