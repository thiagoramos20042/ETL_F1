import pandas as pd

# Carregar os dados extraídos dos arquivos CSV
df_race_results = pd.read_csv('race_results.csv')
df_driver_standings = pd.read_csv('driver_standings.csv')
df_constructor_standings = pd.read_csv('constructor_standings.csv')

# Realizar a junção das tabelas
df_combined = df_race_results.merge(df_driver_standings, on=['year', 'driver', 'constructor', 'driver_nationality'], how='left')
df_combined = df_combined.merge(df_constructor_standings, on=['year', 'constructor', 'constructor_nationality'], how='left')

# Salvar o DataFrame combinado em um arquivo CSV para ser carregado posteriormente
df_combined.to_csv('combined_f1_data.csv', index=False)
print("Dados transformados com sucesso.")
