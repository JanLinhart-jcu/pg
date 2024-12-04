def bin_to_dec(binarni_cislo):
    
    return int(str(binarni_cislo), 2)  # 2 znamená, že vstup je v binární soustavě

### Verze se zadáním decimálního čísla jako input od uživatele: ###

#binarni_cislo = input("Zadejte binární číslo: ")

#print("Decimální hodnota je:", bin_to_dec(binarni_cislo))

################################################################################

def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128