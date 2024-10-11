import pandas as pd
import sqlite3
import json



def load_data(source_type, source_path, table_name=None):
    
    if source_type == '.csv':
        data = pd.read_csv(source_path)
    elif source_type == 'sql':
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect(source_path)

        # Se nenhum nome de tabela for fornecido, listar todas as tabelas
        if table_name is None:
            query = "SELECT name FROM sqlite_master WHERE type='table';"
            tables = pd.read_sql_query(query, conn)
            print(f"Tabelas disponíveis: {tables['name'].tolist()}")
            raise ValueError("Você precisa especificar uma tabela para carregar.")
        else:
            # Carregar a tabela específica
            data = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

        conn.close()  # Fechar a conexão após o uso
    elif source_type == '.json':
        data = pd.read_json(source_path)
    else:
        raise ValueError(f"Unsupported source type: {source_type}")
    
    return data

# Exemplo de uso
# data = load_data('sql', 'caminho_para_seu_database.sqlite', 'nome_da_tabela')
