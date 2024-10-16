# Testovací funkce hello world
def hello_world():
    print('Hello world')


# Definice tří čísel
a = 1
b = 2
c = 3

# Definice funkce max_number
def max_number():
    nejvetsi = max(a, b, c)
    print("Největší číslo je: {nejvetsi}")

# Volání funkce max_number
max_number()

############# Stejná funkce bez použití "max" #############

# Definice tří čísel
a = 1
b = 2
c = 3

# Definice funkce max_number
def max_number2():
    nejvetsi = a  # Předpokládáme, že a je největší
    if b > nejvetsi:
        nejvetsi = b
    if c > nejvetsi:
        nejvetsi = c
    print(f"Největší číslo je: {nejvetsi}")

# Volání funkce max_number
max_number2()
