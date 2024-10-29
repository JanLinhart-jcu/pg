def jaccardova_vzdalenost_mnozin(mnozina1, mnozina2):
    """
    Jaccardova vzdalenost říká, jak jsou dvě množiny rozdílné 0 znamená, že jsou stejné, 1 znamená, že jsou zcela rozdílné
    """
    mnozina1 = set(mnozina1)
    mnozina2 = set(mnozina2)
    intersection = mnozina1.intersection(mnozina2)
    union = mnozina1.union(mnozina2)
    jaccarduv_index = len(intersection) / len(union)
    jaccardova_vzdalenost = 1 - jaccarduv_index
    return jaccardova_vzdalenost


if __name__ == "__main__":
    serp1 = ["https://www.seznam.cz", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz", "https://www.google.com"]
    serp2 = ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    serp3 = ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]

    print(jaccardova_vzdalenost_mnozin(serp1, serp2))
    print(jaccardova_vzdalenost_mnozin(serp2, serp3))
    print(jaccardova_vzdalenost_mnozin(serp1, serp3))