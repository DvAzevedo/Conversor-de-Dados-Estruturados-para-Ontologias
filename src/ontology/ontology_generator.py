from owlready2 import *

def generate_ontology(data, mappings):
    # Criar a ontologia
    onto = get_ontology("http://example.org/general_ontology.owl")
    
    with onto:
        # Criar classes com base nos mapeamentos inferidos
        for cls in mappings['classes']:
            globals()[cls] = types.new_class(cls, (Thing,))
        
        # Criar propriedades de dados
        for prop in mappings['properties']:
            prop_obj = types.new_class(prop, (DataProperty, FunctionalProperty))
            prop_obj.domain = [globals()[cls] for cls in mappings['classes']]
            prop_obj.range = [str]  # Suponha que todas as propriedades sejam strings (pode ajustar)

        # Criar relações
        for rel in mappings['relations']:
            rel_obj = types.new_class(rel, (ObjectProperty,))
            rel_obj.domain = [globals()[cls] for cls in mappings['classes']]
            rel_obj.range = [globals()[cls] for cls in mappings['classes']]
    
    # Criar instâncias das classes com base nos dados
    for index, row in data.iterrows():
        # Para cada linha, criamos uma instância de cada classe
        for cls in mappings['classes']:
            instance = globals()[cls](row[cls])
            # Atribuir propriedades de dados
            for prop in mappings['properties']:
                setattr(instance, prop, row[prop])
    
    # Salvar a ontologia em um arquivo OWL
    onto.save(file="mental_ontology.owl")
