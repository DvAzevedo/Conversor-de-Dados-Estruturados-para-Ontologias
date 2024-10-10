import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils.data_loader import load_data
from mappers.semantic_mapper import infer_mapping
from ontology.ontology_generator import generate_ontology
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

sourceType = 'csv'
sourcePath = 'data/MentalHealthSurvey.csv'
# sourcePath = 'data/social-media.csv'

def pipeline(source_type, source_path):
    # Carregar os dados
    data = load_data(source_type, source_path)

    # print(data.dtypes)
    # transposed_data = data.T
    # print(transposed_data.dtypes)
    # column_features = transposed_data.apply(LabelEncoder().fit_transform).T
    # print(column_features.dtypes)

    
    # Inferir mapeamentos semânticos
    mappings = infer_mapping(data)
    
    # Gerar ontologia OWL
    generate_ontology(data, mappings)
    
    print("Ontologia gerada com sucesso!")

pipeline(sourceType, sourcePath)