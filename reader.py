import csv
import sys

dane = []

with open(sys.argv[1], "r", newline="") as f:
    reader = csv.reader(f)
    for line in reader:
        # print(line)
        dane.append(line)
# print(dane)
for zmiana in sys.argv[3:]:
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

with open(sys.argv[2], "w", newline="") as f:
    writer = csv.writer(f)
    for row in dane:
        writer.writerow(row)
