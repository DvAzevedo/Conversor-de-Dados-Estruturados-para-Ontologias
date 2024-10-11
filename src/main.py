import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils.data_loader import load_data
from utils.treat_path import treat_path
from mappers.semantic_mapper import infer_mapping
from ontology.ontology_generator import generate_ontology
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

path = 'data/games.csv'


def pipeline(path, table_name=None):
    name, source_type = treat_path(path)

    # Carregar os dados
    data = load_data(source_type, path, table_name)
    
    # Inferir mapeamentos semânticos
    mappings = infer_mapping(data)
    
    # Gerar ontologia OWL
    generate_ontology(data, mappings, name)
    
    print("Ontologia gerada com sucesso!")

pipeline(path)