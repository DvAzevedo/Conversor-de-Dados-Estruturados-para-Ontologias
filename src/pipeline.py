import pandas as pd
import numpy as np
from utils.data_loader import load_data
from utils.treat_path import treat_path
from mappers.semantic_mapper import infer_mapping
from ontology.ontology_generator import generate_ontology

def pipeline(path, table_name=None):
    try:
        name, source_type = treat_path(path)
        print(f"Processando arquivo: {name}, tipo: {source_type}")

        # Carregar os dados
        data = load_data(source_type, path, table_name)
        if data is None:
            raise ValueError("Os dados não foram carregados corretamente.")

        print("Dados carregados com sucesso.")

        # Inferir mapeamentos semânticos
        mappings = infer_mapping(data)
        print("Mapeamentos inferidos com sucesso.")

        # Gerar ontologia OWL
        generate_ontology(data, mappings, name)
        print("Ontologia gerada com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro no pipeline: {e}")
