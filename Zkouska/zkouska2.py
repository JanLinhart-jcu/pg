# Příklad 2: Práce s externími daty a výpočty
# Zadání:
# Napište funkci `fetch_weather_data`, která:
# 1. Přijme jako parametr město (`city`), s tímto městem a klíčem `api_key` získejte aktuální teplotu z url `http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}`.
# 2. Teplota je uložená v slovníku `main` pod klíčem `temp` v Kelvinech.
# 3. Funkce vrátí teplotu v °C zaokrouhlenou na dvě desetinná místa (273.15 °K = 0 °C).

import requests, unittest # knihovna pro odesílání HTTP požadavků.

# API klíč pro OpenWeatherMap
api_key = 'a023a3be26e530f37924110734b494b1'

def fetch_weather_data(city, api_key): # Funkce sestaví URL pro požadavek na API, kde city je město zadané uživatelem a api_key slouží k autorizaci.
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url) # Odešle GET požadavek přes requests.get()
    if response.ok:
        data = response.json()  # Data se zpracují pomocí response.json() do formátu slovníku.
        kelvin_temp = data['main']['temp'] # Teplota v Kelvinech (data['main']['temp']) se převede na Celsia (kelvin_temp - 273.15).
        celsius_temp = round(kelvin_temp - 273.15, 2) # Výsledek se zaokrouhlí na dvě desetinná místa a vrátí.
        return celsius_temp
    else:
        raise ValueError(f"Error fetching data for {city}. Status code: {response.status_code}") # Pokud je odpověď neúspěšná, vyvolá se výjimka ValueError

# Unit testy
from unittest.mock import patch, MagicMock # unittest.mock - nástroj pro simulaci (mockování) odpovědí při testování.

def test_fetch_weather_data(): 
    mock_response = {
        "main": {
            "temp": 293.15  # Teplota v Kelvinech
        }
    }
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, json=MagicMock(return_value=mock_response))
        assert fetch_weather_data("Prague", "test_api_key") == 20.0  # 293.15 K = 20.0 °C

if __name__ == "__main__":
    city = input("Enter city name: ") # uživatel zadá požadované město
    temperature = fetch_weather_data(city, api_key) # proměnná temperature interpretuje informace získané funkcí fetch_weather_data
    print(f"Current temperature in {city}: {temperature} °C")
    