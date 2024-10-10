python3 setup.py
source venv_conversor/bin/activate
./run



/project-root
│
├── /data                     # Diretório para armazenar os dados de entrada (CSV, Excel, etc.)
│   ├── sample_data.csv
│   └── sample_database.sql
│
├── /notebooks                # Notebooks Jupyter para experimentação e prototipagem rápida
│   └── data_analysis.ipynb
│
├── /src                      # Código-fonte do projeto
│   ├── /mappers              # Algoritmos de mapeamento semântico e IA
│   │   └── semantic_mapper.py
│   ├── /ontology             # Geração da ontologia OWL
│   │   └── ontology_generator.py
│   ├── /utils                # Funções utilitárias (leitura de dados, etc.)
│   │   └── data_loader.py
│   └── main.py               # Script principal que orquestra o processo
│
├── /tests                    # Testes automatizados para validar funcionalidades
│   └── test_ontology_generator.py
│
├── /docs                     # Documentação do projeto
│   └── readme.md
│
├── requirements.txt          # Dependências do projeto
├── setup.py                  # Script de configuração (opcional)
└── README.md