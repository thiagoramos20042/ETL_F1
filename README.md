# ETL de Dados de Fórmula 1
Este repositório contém um processo ETL (Extração, Transformação e Carga) para obter dados de resultados de corridas, classificações de pilotos e classificações de construtores da Fórmula 1 a partir da API Ergast, transformar esses dados e carregá-los em um banco de dados SQLite.

# Arquitetura do Processo
# 1. Extração (extraction.py)
O script extraction.py é responsável por extrair dados da API Ergast para os anos de 1950 a 2023. Ele realiza as seguintes etapas:

1- Obter Resultados de Corridas: A função get_race_results(year) faz uma requisição à API Ergast para obter os resultados das corridas de um ano específico.
2- Obter Classificações de Pilotos: A função get_driver_standings(year) faz uma requisição à API Ergast para obter a classificação dos pilotos de um ano específico.
3- Obter Classificações de Construtores: A função get_constructor_standings(year) faz uma requisição à API Ergast para obter a classificação dos construtores de um ano específico.
4- Salvar Dados Extraídos: Os dados extraídos são armazenados em arquivos CSV (race_results.csv, driver_standings.csv e constructor_standings.csv).

# 2. Transformação (transformation.py)
O script transformation.py é responsável por transformar os dados extraídos e combiná-los em um único DataFrame. Ele realiza as seguintes etapas:

1- Carregar Dados Extraídos: Os dados são carregados dos arquivos CSV gerados na etapa de extração.
2- Combinar Dados: Os DataFrames são combinados usando junções (merge) para formar um DataFrame único que contém todas as informações relevantes.
3- Salvar Dados Transformados: O DataFrame combinado é salvo em um arquivo CSV (combined_f1_data.csv).

# 3. Carga (load.py)

O script load.py é responsável por carregar os dados transformados no banco de dados SQLite. Ele realiza as seguintes etapas:

1- Carregar Dados Transformados: Os dados são carregados do arquivo CSV gerado na etapa de transformação.
2- Conectar ao Banco de Dados: Conecta ou cria um banco de dados SQLite (f1_data.db).
3- Criar Tabela: Cria uma tabela no banco de dados para armazenar os dados transformados.
4- Inserir Dados na Tabela: Os dados são inseridos na tabela criada.
5- Confirmar e Fechar Conexão: As alterações são confirmadas e a conexão com o banco de dados é fechada.

# Execução do Processo
1- Execute extraction.py para extrair os dados e salvá-los em arquivos CSV:
'''python
python extraction.py

Agora, execute o próximo script para processar os dados:





