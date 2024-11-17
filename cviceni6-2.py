import json
import requests

# URL pro vyhledávání značek automobilů podle prefixu
url = "https://db.carnewschina.com/suggest?q="

def download_json_and_parse_brands(prefix):
    # Stáhneme data z URL s připojeným prefixem
    response = requests.get(url + prefix)
    
    # Pokud je odpověď úspěšná
    if response.status_code == 200:
        # Načteme JSON odpověď
        data = response.json()
        
        # Předpokládáme, že data obsahují seznam značek v klíči 'brands'
        result = [brand['name'] for brand in data.get('brands', [])]
        
        return result
    else:
        print("Chyba při načítání dat.")
        return []

if __name__ == "__main__":
    # Získáme prefix od uživatele
    prefix = input("Zadej prefix: ")
    
    # Získáme seznam značek podle zadaného prefixu
    brands = download_json_and_parse_brands(prefix)
    
    # Pokud byly nějaké značky nalezeny, vypíšeme je
    if brands:
        for brand in brands:
            print(brand)
    else:
        print("Žádné značky nenalezeny.")
