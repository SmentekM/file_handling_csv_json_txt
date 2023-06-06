import csv
import sys
dane_wejsciowe = sys.argv[1]

plik_wyjsciowy = "out.csv"
if plik_wyjsciowy not in sys.argv:
    print('Nie podano pliku wyjsciowego "out.csv" w argumentach ')
    exit()
dane_wyjsciowe = sys.argv[2]

dane = []

with open(dane_wejsciowe, "r", newline="") as f:
    reader = csv.reader(f)
    for line in reader:
        # print(line)
        dane.append(line)
# print(dane)
for zmiana in sys.argv[3:]:
    if "," not in zmiana:
        print('Podano nieprawidłowe separotory w argumentach zmian. Zmiany muszą być oddzielone ","')
        exit()
    # print(zmiana)

    x = list(zmiana.split(","))
    # print(x)
    kolumna = int(x[0])
    wiersz = int(x[1])
    wartosc = x[2]
    # print(f'kolumna: {kolumna}\n wiersz: {wiersz}\n wartośc: {wartosc}')
    wybrany_wiersz = dane[wiersz]
    # print(wybrany_wiersz)
    wybrany_wiersz[kolumna] = wartosc
    # print(wybrany_wiersz[kolumna])

with open(dane_wyjsciowe, "w", newline="") as f:
    writer = csv.writer(f)
    for row in dane:
        writer.writerow(row)
