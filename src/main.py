

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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