# Příklad 1: Práce s podmínkami a řetězci
# Zadání:
# Napište funkci `find_divisible`, která přijme číslo max_number a dělitel divisor. 
# Funkce vrátí seznam všech čísel menších nebo rovno max_number, která jsou dělitelná beze zbytku dělitelem divisor.
# Příklad: find_divisible(5, 2) vrátí [2, 4].

import unittest

def find_divisible(max_number, divisor): # definuje funkci, která příjmá dva parametry
    return [num for num in range(1, max_number + 1) if num % divisor == 0] # range(1, max_number + 1) generuje postupně všechna čísla od 1 do max_number (včetně) 
                                                                        # num % divisor == 0 ověřuje, zda je číslo num dělitelné beze zbytku dělitelem divisor
                                                                        # pokud ano, číslo se přidá do seznamu (list comprehension)

# Unit testy
class TestFindDivisible(unittest.TestCase):

    def test_divisible_by_5(self):
        self.assertEqual(find_divisible(25, 5), [5, 10, 15, 20, 25])

    def test_divisible_by_3(self):
        self.assertEqual(find_divisible(9, 3), [3, 6, 9])

    def test_divisible_by_2(self):
        self.assertEqual(find_divisible(13, 2), [2, 4, 6, 8, 10, 12])

    def test_no_divisible(self):
        self.assertEqual(find_divisible(5, 10), [])  # žádná čísla nejsou dělitelná

if __name__ == "__main__":
    max_number = 100
    divisor = int(input("Enter divisor: "))
    result = find_divisible(max_number, divisor)
    print(f'Čísla dělitelná číslem {divisor} menší než nebo rovna číslu {max_number}: {result}')
