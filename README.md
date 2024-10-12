# Conversor de Banco de Dados para Ontologias Automático (usando Clustering)

## Descrição

O **Conversor de Banco de Dados para Ontologias Automático** é uma ferramenta desenvolvida para converter dados estruturados no formato `.csv` em ontologias OWL. O processo de conversão utiliza técnicas de machine learning, como clustering, para inferir automaticamente as classes, propriedades e relações entre os dados.
Em desenvolvimento.

## Funcionalidades

- **Inferência semântica automática:** identifica automaticamente classes, propriedades e relações com base na estrutura dos dados.
- **Geração de ontologias OWL:** exporta os dados convertidos em um arquivo OWL, que pode ser visualizado em ferramentas como Protégé.
- **Interface gráfica:** permite ao usuário fazer o upload dos arquivos e gerar a ontologia de forma simples e intuitiva.
- **Clusterização para mapeamento semântico:** utiliza algoritmos de clustering, como KMeans, para agrupar e definir classes e propriedades com base nos padrões dos dados.

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/DvAzevedo/Conversor-de-Dados-Estruturados-para-Ontologias.git

2. Crie um ambiente virtual e ative-o:
    ```bash
    python3 -m venv venv_conversor
    source venv_conversor/bin/activate  

3. Instale as dependência:
    ```bash
    python3 setup.py

4. Execute:
    ```bash
    ./run

## Próximos Passos

- Correção de bugs.
- Treinamento contínuo: melhorar a capacidade de inferência semântica usando técnicas de aprendizado de máquina supervisionado.
- Suporte a mais formatos além do CSV.
- Aplicação de testes.
- Documentação.
- Visualização: adicionar uma visualização gráfica da ontologia gerada diretamente na interface.

