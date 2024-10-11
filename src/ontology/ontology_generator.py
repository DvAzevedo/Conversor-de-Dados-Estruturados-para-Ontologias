from owlready2 import get_ontology, Thing, DataProperty, ObjectProperty, FunctionalProperty
import types
import os

def generate_ontology(data, mappings, name):
    # Criar a ontologia
    onto = get_ontology("http://example.org/general_ontology.owl")
    
    with onto:
        # Criar classes
        class_dict = {}
        for cls in mappings['classes']:
            class_dict[cls] = type(cls, (Thing,), {})

        # Criar propriedades de dados
        for prop in mappings['properties']:
            prop_obj = type(prop, (DataProperty, FunctionalProperty), {})
            prop_obj.domain = [class_dict[cls] for cls in mappings['classes']]
            prop_obj.range = [str]

        # Criar relações
        for rel in mappings['relations']:
            rel_obj = type(rel, (ObjectProperty,), {})
            rel_obj.domain = [class_dict[cls] for cls in mappings['classes']]
            rel_obj.range = [class_dict[cls] for cls in mappings['classes']]
    
    # Criar instâncias das classes com base nos dados
    for index, row in data.iterrows():
        for cls in mappings['classes']:
            if cls in row:
                instance = class_dict[cls](row[cls])
                # Atribuir propriedades de dados
                for prop in mappings['properties']:
                    if prop in row:
                        setattr(instance, prop, row[prop])
    
    # Salvar a ontologia em um arquivo OWL
    filename = f"{name}.owl"
    if os.path.exists(filename):
        os.remove(filename)

    onto.save(file=filename)
    

