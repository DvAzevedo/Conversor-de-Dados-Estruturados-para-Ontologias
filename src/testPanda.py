

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from utils.correlation_methods import escolher_melhor_correlacao

# 1. Carregar os CSVs
data = pd.read_csv('data/gym_members_exercise_tracking.csv')
data1 = pd.read_csv('data/MentalHealthSurvey.csv')

# 2. Separar colunas numéricas e textuais
colunas_numericas = data.select_dtypes(include=['number']).columns
colunas_textuais = data.select_dtypes(include=['object']).columns

print("Colunas numéricas:", colunas_numericas)
print("Colunas textuais:", colunas_textuais)

# 3. Aplicar One-Hot Encoding às colunas textuais
data_encoded = pd.get_dummies(data, columns=colunas_textuais)

# 4. Calcular e exibir a melhor correlação entre todas as colunas numéricas
resultado_correlacoes = {}

# for i in range(len(colunas_numericas)):
#     for j in range(i + 1, len(colunas_numericas)):
#         col1 = colunas_numericas[i]
#         col2 = colunas_numericas[j]
#         melhor_correlacao = escolher_melhor_correlacao(data_encoded[col1].values, data_encoded[col2].values)
#         print(melhor_correlacao)
#         resultado_correlacoes[(col1, col2)] = melhor_correlacao
# for i in range(len(data_encoded.columns)):
#     for j in range(i + 1, len(data_encoded.columns)):
#         col1 = data_encoded.iloc[:, i]  # Acessa a i-ésima coluna
#         col2 = data_encoded.iloc[:, j]
#         melhor_correlacao = escolher_melhor_correlacao(data_encoded[col1].values, data_encoded[col2].values)
#         print(melhor_correlacao)
#         resultado_correlacoes[(col1, col2)] = melhor_correlacao
        
# 5. Exibir resultados
# for col_pair, metodo in resultado_correlacoes.items():
#     print(f"Correlação entre {col_pair[0]} e {col_pair[1]}: {metodo}")

# 6. Calcular correlação entre todas as colunas (numéricas e codificadas)
correlacoes = data_encoded.corr(method="kendall")

# 7. Exibir o gráfico de correlação com os nomes das colunas
plt.figure(figsize=(30, 24))  # Ajustar o tamanho do gráfico para caber os rótulos
plt.matshow(correlacoes, fignum=1)  # Usar fignum=1 para integrar ao plt.figure

# Adicionar rótulos de colunas e linhas
plt.xticks(ticks=np.arange(correlacoes.shape[1]), labels=correlacoes.columns, rotation=90)
plt.yticks(ticks=np.arange(correlacoes.shape[0]), labels=correlacoes.index)

# Exibir barra de cores
plt.colorbar()

plt.show()

