def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    start = figurka['pozice']
    typ = figurka['typ']
    
    # Kontrola, zda je cílové pole mimo šachovnici
    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False
    
    # Pěšec
    if typ == 'pěšec':
        if cilova_pozice == (start[0] + 1, start[1]) and cilova_pozice not in obsazene_pozice:
            return True
        if start[0] == 2 and cilova_pozice == (start[0] + 2, start[1]) and (3, start[1]) not in obsazene_pozice:
            return True
    
    # Jezdec
    elif typ == 'jezdec':
        dx = [2, 2, -2, -2, 1, 1, -1, -1]
        dy = [1, -1, 1, -1, 2, -2, 2, -2]
        for i in range(8):
            if cilova_pozice == (start[0] + dx[i], start[1] + dy[i]):
                return True
    
    # Věž
    elif typ == 'věž':
        if start[0] == cilova_pozice[0]:  # Horizontálně
            step = 1 if cilova_pozice[1] > start[1] else -1
            for y in range(start[1] + step, cilova_pozice[1], step):
                if (start[0], y) in obsazene_pozice:
                    return False
            return True
        elif start[1] == cilova_pozice[1]:  # Vertikálně
            step = 1 if cilova_pozice[0] > start[0] else -1
            for x in range(start[0] + step, cilova_pozice[0], step):
                if (x, start[1]) in obsazene_pozice:
                    return False
            return True
    
    # Střelec
    elif typ == 'střelec':
        if abs(start[0] - cilova_pozice[0]) == abs(start[1] - cilova_pozice[1]):  # Diagonálně
            step_x = 1 if cilova_pozice[0] > start[0] else -1
            step_y = 1 if cilova_pozice[1] > start[1] else -1
            x, y = start[0] + step_x, start[1] + step_y
            while (x, y) != cilova_pozice:
                if (x, y) in obsazene_pozice:
                    return False
                x += step_x
                y += step_y
            return True

    # Dáma
    elif typ == 'dáma':
        # Kombinace pohybu věže a střelce
        if start[0] == cilova_pozice[0] or start[1] == cilova_pozice[1]:  # Horizontálně nebo vertikálně
            return je_tah_mozny({'typ': 'věž', 'pozice': start}, cilova_pozice, obsazene_pozice)
        elif abs(start[0] - cilova_pozice[0]) == abs(start[1] - cilova_pozice[1]):  # Diagonálně
            return je_tah_mozny({'typ': 'střelec', 'pozice': start}, cilova_pozice, obsazene_pozice)

    # Král
    elif typ == 'král':
        if abs(start[0] - cilova_pozice[0]) <= 1 and abs(start[1] - cilova_pozice[1]) <= 1:  # Všechny směry
            return cilova_pozice not in obsazene_pozice
    
    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    cilova_pozice = (3, 2)
    figurka = pesec
    vysledek = je_tah_mozny(figurka, cilova_pozice, obsazene_pozice)
    print(f"Je tento tah pro figurku {figurka['typ']} z pozice {figurka['pozice']} na {cilova_pozice} možný? {vysledek}")
