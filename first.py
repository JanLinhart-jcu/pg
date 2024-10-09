### Úkol 1 ###

# Definice funkce sudy_nebo_lichy 
def sudy_nebo_lichy(cislo):
    if cislo % 2 == 0:
        print(f"Číslo {cislo} je sudé")
    else:
        print(f"Číslo {cislo} je liché")

# Volání funkce s hodnotami 5 a 1000000
sudy_nebo_lichy(5)
sudy_nebo_lichy(1000000)