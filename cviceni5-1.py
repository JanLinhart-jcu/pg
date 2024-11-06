import csv
import sys

def nacti_csv(soubor):
    data = []
    return


def spoj_data(*data):
    pass


def zapis_csv(soubor, data):
    pass


if __name__ == "__main__":
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        vysledna_data = spoj_data(csv_data1, csv_data2)
        zapis_csv(vysledna_data)
    except Exception as SyntaxError:
        pass