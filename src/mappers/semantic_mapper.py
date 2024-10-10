from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import pandas as pd

# def infer_mapping(data):
#     mappings = {}

#     transposed_data = data.T
#     transposed_data = transposed_data.astype(str)

#     # Transformar colunas de texto em números (necessário para clustering)
#     column_features = transposed_data.apply(LabelEncoder().fit_transform).T

#     # Usar KMeans para identificar clusters nos dados
#     model = KMeans(n_clusters=3)
#     model.fit(column_features)

#     # Inferir mapeamentos com base nos clusters
#     mappings['classes'] = data.columns[model.labels_ == 0]
#     mappings['properties'] = data.columns[model.labels_ == 1]
#     mappings['relations'] = data.columns[model.labels_ == 2]
    
#     return mappings


def infer_mapping(data):
    mappings = {}

    # Transformar todas as colunas em string para evitar erros de tipo
    data = data.astype(str)

    # Transformar as colunas categóricas em números (necessário para clustering)
    data_encoded = data.apply(LabelEncoder().fit_transform)

    # Aplicar KMeans diretamente nos dados codificados
    model = KMeans(n_clusters=3)
    model.fit(data_encoded.T)  # Transpor aqui para aplicar nas colunas

    # Verificar se o número de rótulos corresponde ao número de colunas
    if len(model.labels_) == len(data.columns):
        # Inferir mapeamentos com base nos clusters
        mappings['classes'] = data.columns[model.labels_ == 0]
        mappings['properties'] = data.columns[model.labels_ == 1]
        mappings['relations'] = data.columns[model.labels_ == 2]
    else:
        raise ValueError(f"Tamanho de labels ({len(model.labels_)}) não corresponde ao número de colunas ({len(data.columns)})")
    
    return mappings