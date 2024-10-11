import os

def treat_path(path):
    name_and_type = os.path.basename(path)  
    name, source_type = os.path.splitext(name_and_type)  
    print(f"Primeiro nome: {name}")
    print(f"Extensão: {source_type}")
    return name, source_type

