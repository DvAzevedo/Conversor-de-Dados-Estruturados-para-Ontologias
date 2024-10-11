import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans



def infer_mapping(data):
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(data)

    # Transformar todas as colunas em string
    data = data.astype(str)

    # Transformar colunas categóricas em números
    data_encoded = data.apply(LabelEncoder().fit_transform)

    model = KMeans(n_clusters=3)
    model.fit(data_encoded.T)

    mappings = {}

    if len(model.labels_) == len(data.columns):
        mappings['classes'] = data.columns[model.labels_ == 0].tolist()
        mappings['properties'] = data.columns[model.labels_ == 1].tolist()
        mappings['relations'] = data.columns[model.labels_ == 2].tolist()
    else:
        raise ValueError(f"Tamanho de labels ({len(model.labels_)}) não corresponde ao número de colunas ({len(data.columns)})")

    return mappings



