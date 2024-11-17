import sys
import requests
import re

def download_url_and_get_all_hrefs(url):
    """
    Funkce stáhne obsah stránky na dané URL a vrátí seznam všech odkazů na stránce.
    """
    try:
        # Stáhnout obsah stránky
        response = requests.get(url)
        
        # Zkontrolovat návratový kód
        if response.status_code != 200:
            raise Exception(f"Chyba při stahování URL: {url}, kód: {response.status_code}")
        
        # Extrahovat odkazy pomocí regulárního výrazu
        content = response.text
        hrefs = re.findall(r'href="(https?://[^"]+)"', content)
        
        return hrefs
    except requests.RequestException as e:
        raise Exception(f"Chyba při připojování k URL: {e}")
    except Exception as e:
        raise Exception(f"Obecná chyba: {e}")

if __name__ == "__main__":
    try:
        # Načíst URL ze vstupních argumentů
        url = sys.argv[1]
        
        # Zavolat funkci a vytisknout výsledky
        all_hrefs = download_url_and_get_all_hrefs(url)
        print(all_hrefs)
    except Exception as e:
        print(f"Program skončil chybou: {e}")

###### Pro spuštění: python sixth.py [url] (např. https://www.jcu.cz) ######