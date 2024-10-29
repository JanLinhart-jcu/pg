from cviceni4_jaccard import jaccardova_vzdalenost_mnozin
from cviceni4_levenstein import levensteinova_vzdalenost


def deduplikace_dotazu(dotazy):
    """
    Tato funkce spocita jaccardovu vzdalenost a levensteinovu vzdalenost
    a vyradi z seznamu dotazy, polozky, ktere budou mit jaccardovu vzdalenost
    mensi nez 0.5 a levensteinovu vzdalenost <= 1.
    """
    unique_dotazy = []

    for i in range(len(dotazy)):
        is_duplicate = False
        for j in range(i):
            jaccard_distance = jaccardova_vzdalenost_mnozin(dotazy[i]['serp'], dotazy[j]['serp'])
            levenstein_distance = levensteinova_vzdalenost(dotazy[i]['dotaz'], dotazy[j]['dotaz'])

            if jaccard_distance < 0.5 and levenstein_distance <= 1:
                is_duplicate = True
                break
        
        if not is_duplicate:
            unique_dotazy.append(dotazy[i])

    return unique_dotazy


if __name__ == "__main__":
    dotaz1 = {
        "dotaz": "seznam",
        "serp": ["https://www.seznam.cz", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz", "https://www.google.com"]
    }
    dotaz2 = {
        "dotaz": "seznamka",
        "serp": ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    }
    dotaz3 = {
        "dotaz": "sesnam",
        "serp": ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]
    }
    dotaz4 = {
        "dotaz": "google",
        "serp": ["https://www.google.com", "https://maps.google.com", "https://www.gmail.com"]
    }
    
    print(deduplikace_dotazu([dotaz1, dotaz2, dotaz3, dotaz4]))

