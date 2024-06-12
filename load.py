import sqlite3
import pandas as pd

# Carregar os dados transformados do arquivo CSV
df_combined = pd.read_csv('combined_f1_data.csv')

# Conectar ao banco de dados SQLite (ou criar um novo banco de dados)
conn = sqlite3.connect('f1_data.db')
cursor = conn.cursor()

# Criar a tabela no banco de dados
cursor.execute('''
    CREATE TABLE IF NOT EXISTS f1_data (
        year INTEGER,
        race_name TEXT,
        round INTEGER,
        date TEXT,
        circuit_name TEXT,
        location_locality TEXT,
        location_country TEXT,
        position INTEGER,
        driver TEXT,
        driver_nationality TEXT,
        constructor TEXT,
        constructor_nationality TEXT,
        grid INTEGER,
        laps INTEGER,
        time TEXT,
        status TEXT,
        points REAL,
        fastest_lap_rank INTEGER,
        fastest_lap_time TEXT,
        fastest_lap_avg_speed REAL,
        fastest_lap_avg_speed_units TEXT,
        driver_standing_position INTEGER,
        driver_standing_points REAL,
        driver_wins INTEGER,
        constructor_standing_position INTEGER,
        constructor_standing_points REAL,
        constructor_wins INTEGER
    )
''')

# Inserir os dados na tabela
df_combined.to_sql('f1_data', conn, if_exists='replace', index=False)

# Confirmar as alterações e fechar a conexão
conn.commit()
conn.close()

print("Dados inseridos com sucesso no banco de dados SQLite.")
