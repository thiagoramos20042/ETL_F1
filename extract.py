import requests
import pandas as pd

# Função para obter resultados de corridas de um ano específico
def get_race_results(year):
    race_results_url = f"https://ergast.com/api/f1/{year}/results.json?limit=1000"
    race_response = requests.get(race_results_url)
    race_data = race_response.json()
    
    races = race_data['MRData']['RaceTable']['Races']
    race_results = []

    for race in races:
        race_name = race['raceName']
        round_number = race['round']
        date = race['date']
        circuit_name = race['Circuit']['circuitName']
        location = race['Circuit']['Location']
        
        for result in race['Results']:
            driver = result['Driver']
            constructor = result['Constructor']
            fastest_lap = result['FastestLap'] if 'FastestLap' in result else None
            
            race_results.append({
                'year': year,
                'race_name': race_name,
                'round': round_number,
                'date': date,
                'circuit_name': circuit_name,
                'location_locality': location['locality'],
                'location_country': location['country'],
                'position': result['position'],
                'driver': f"{driver['givenName']} {driver['familyName']}",
                'driver_nationality': driver['nationality'],
                'constructor': constructor['name'],
                'constructor_nationality': constructor['nationality'],
                'grid': result['grid'],
                'laps': result['laps'],
                'time': result['Time']['time'] if 'Time' in result else None,
                'status': result['status'],
                'points': result['points'],
                'fastest_lap_rank': fastest_lap['rank'] if fastest_lap else None,
                'fastest_lap_time': fastest_lap['Time']['time'] if fastest_lap else None,
                'fastest_lap_avg_speed': fastest_lap['AverageSpeed']['speed'] if fastest_lap else None,
                'fastest_lap_avg_speed_units': fastest_lap['AverageSpeed']['units'] if fastest_lap else None
            })
    return race_results

# Função para obter a classificação de pilotos de um ano específico
def get_driver_standings(year):
    driver_standings_url = f"https://ergast.com/api/f1/{year}/driverStandings.json"
    driver_standings_response = requests.get(driver_standings_url)
    driver_standings_data = driver_standings_response.json()
    
    if not driver_standings_data['MRData']['StandingsTable']['StandingsLists']:
        return []

    driver_standings = driver_standings_data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
    driver_standings_results = []

    for standing in driver_standings:
        driver = standing['Driver']
        constructor = standing['Constructors'][0]
        driver_standings_results.append({
            'year': year,
            'driver': f"{driver['givenName']} {driver['familyName']}",
            'driver_standing_position': standing['position'],
            'driver_standing_points': standing['points'],
            'driver_wins': standing['wins'],
            'driver_nationality': driver['nationality'],
            'constructor': constructor['name'],
        })
    return driver_standings_results

# Função para obter a classificação de construtores de um ano específico
def get_constructor_standings(year):
    constructor_standings_url = f"https://ergast.com/api/f1/{year}/constructorStandings.json"
    constructor_standings_response = requests.get(constructor_standings_url)
    constructor_standings_data = constructor_standings_response.json()
    
    if not constructor_standings_data['MRData']['StandingsTable']['StandingsLists']:
        return []

    constructor_standings = constructor_standings_data['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']
    constructor_standings_results = []

    for standing in constructor_standings:
        constructor = standing['Constructor']
        constructor_standings_results.append({
            'year': year,
            'constructor': constructor['name'],
            'constructor_standing_position': standing['position'],
            'constructor_standing_points': standing['points'],
            'constructor_wins': standing['wins'],
            'constructor_nationality': constructor['nationality'],
        })
    return constructor_standings_results

# Inicializando listas para armazenar todos os dados
all_race_results = []
all_driver_standings = []
all_constructor_standings = []

# Iterando sobre os anos de 1950 até 2023
for year in range(1950, 2023 + 1):
    print(f"Processando ano {year}")
    all_race_results.extend(get_race_results(year))
    all_driver_standings.extend(get_driver_standings(year))
    all_constructor_standings.extend(get_constructor_standings(year))

# Salvar os dados extraídos em arquivos CSV
pd.DataFrame(all_race_results).to_csv('race_results.csv', index=False)
pd.DataFrame(all_driver_standings).to_csv('driver_standings.csv', index=False)
pd.DataFrame(all_constructor_standings).to_csv('constructor_standings.csv', index=False)

print("Dados extraídos com sucesso.")
