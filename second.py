def cislo_text(cislo):
    # Převod čísla z řetězce na celé číslo
    cislo = int(cislo)

    # Slovník pro čísla od 0 do 19
    jednociferny = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět", 
                    "deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", 
                    "sedmnáct", "osmnáct", "devatenáct"]
    
    # Slovník pro desítky
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", 
                "sedmdesát", "osmdesát", "devadesát"]
    
    # Zpracování čísel podle jejich hodnoty
    if 0 <= cislo < 20:
        return jednociferny[cislo]
    elif 20 <= cislo < 100:
        des = desitky[cislo // 10]
        jed = cislo % 10
        if jed > 0:
            return f"{des} {jednociferny[jed]}"
        else:
            return des
    elif cislo == 100:
        return "sto"
    else:
        return "Číslo není v povoleném rozsahu (0-100)."

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)