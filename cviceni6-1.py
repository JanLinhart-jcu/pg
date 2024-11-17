import sys
import requests
from lxml import html

def stahni_url_a_vrat_elementy(url, tagy):
    elementy_text = []

    # Získání HTML obsahu stránky
    response = requests.get(url)
    
    # Kontrola, zda je odpověď úspěšná
    if response.status_code != 200:
        print('Chyba při načítání stránky')
        return []

    # Zpracování HTML obsahu
    tree = html.fromstring(response.content)

    # Hledání a přidání textového obsahu všech vybraných tagů
    for tag in tagy:
        elementy_text.extend(tree.xpath(f'//{tag}/text()'))

    return elementy_text

if __name__ == "__main__":
    # Přečtení URL z argumentů příkazové řádky
    if len(sys.argv) != 3:
        print("Použití: python script.py <url> <tag1,tag2,...>")
        sys.exit(1)

    url = sys.argv[1]
    tagy = sys.argv[2].split(",")  # Předpokládáme, že tagy budou oddělené čárkami (např. h1,a,p)

    elementy_text = stahni_url_a_vrat_elementy(url, tagy)

    # Výpis nalezených textů z elementů
    if elementy_text:
        for text in elementy_text:
            print(text.strip())
    else:
        print(f"Žádné texty z tagů {', '.join(tagy)} nenalezeny.")
