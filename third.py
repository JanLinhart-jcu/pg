def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False.
    """
    if cislo <= 1:
        return False
    for i in range(2, int(cislo**0.5) + 1):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """
    return [cislo for cislo in range(2, maximum + 1) if je_prvocislo(cislo)]

if __name__ == "__main__":
    # Zadej číslo pro ověření, zda je prvočíslo
    cislo = int(input("Zadej číslo pro ověření, zda je prvočíslo: "))
    print(f"Je číslo {cislo} prvočíslo? {je_prvocislo(cislo)}")

    # Zadej maximum pro vypsání prvočísel
    maximum = int(input("Zadej maximum pro vypis vsech prvocisel: "))
    prvocisla = vrat_prvocisla(maximum)
    print(f"Prvočísla v rozsahu 1 až {maximum}: {prvocisla}")

