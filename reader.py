import csv
import json
import pickle
import sys
import os


class Pliki:

    def __init__(self, dane_wejsciowe=sys.argv[1], dane_wyjsciowe=sys.argv[2]):
        self.dane_wejsciowe = dane_wejsciowe
        self.dane_wyjsciowe = dane_wyjsciowe

    def wprowadznie_zmian(self,dane):
        for zmiana in sys.argv[3:]:
            if "," not in zmiana:
                print('Podano nieprawidłowe separotory w argumentach zmian. Zmiany muszą być oddzielone ","')
                exit()
            # print("zmian",zmiana)
            x = list(zmiana.split(","))
            # print(x)
            kolumna = int(x[0])
            wiersz = int(x[1])
            wartosc = x[2]
            # print(f'kolumna: {kolumna}\n wiersz: {wiersz}\n wartośc: {wartosc}')
            # print(dane)
            wybrany_wiersz = dane[wiersz]
            # print(wybrany_wiersz)
            wybrany_wiersz[kolumna] = wartosc
            # print(wybrany_wiersz[kolumna])
        return dane

    def spr_pliku(self):
        if not os.path.exists(self.dane_wejsciowe):
            print("Plik do odczytu nie istniej")
            return exit()
        elif not os.path.exists(self.dane_wyjsciowe):
            print('Plik do zapisu nie istenie')
            return exit()


class PlikiCsv(Pliki):

    def input_csv(self,dane):
        with open(self.dane_wejsciowe, "r", newline="") as f:
            reader = csv.reader(f)
            for line in reader:
                # print(line)
                dane.append(line)
        return dane

    def output_csv(self, dane, lokalizacja):
        with open(lokalizacja, "w", newline="") as f:
            writer = csv.writer(f)
            for row in dane:
                writer.writerow(row)
        return dane


class PlikiJson(Pliki):

    def input_json(self, dane):
        with open(self.dane_wejsciowe, "r") as f:
            dane.append(json.load(f))
        return dane

    def output_json(self, dane):
        with open(self.dane_wyjsciowe, "w") as f:
            json.dump(dane, f)
        return dane


class PlikiPickle(Pliki):

    def input_pickle(self, dane):
        with open(self.dane_wejsciowe, "rb") as f:
            dane.append(pickle.load(f))
        return dane

    def output_pickle(self, dane):
        with open(self.dane_wyjsciowe, "wb") as f:
            pickle.dump(dane, f)
        return dane


class PlikiTxt(Pliki):

    def input(self, dane):
        with open(self.dane_wejsciowe, "r") as f:
            dane.append(f.readlines())
        return dane

    def output(self, dane):
        with open(self.dane_wyjsciowe, "w") as f:
            for linia in dane:
                f.write(str(linia) + '\n')
        return dane


def spr_typ_pliku_wejscie(nazwa_pliku):
    if nazwa_pliku.endswith(".csv"):
        ob_csv.input_csv(dane=dane)
        ob_csv.wprowadznie_zmian(dane=dane)
    elif nazwa_pliku.endswith(".json"):
        ob_json.input_json(dane=dane)
        ob_json.wprowadznie_zmian(dane=dane)
    elif nazwa_pliku.endswith(".pickle"):
        ob_pickle.input_pickle(dane=dane)
        ob_pickle.wprowadznie_zmian(dane=dane)
    elif nazwa_pliku.endswith(".txt"):
        ob_txt.input(dane=dane)
        ob_txt.wprowadznie_zmian(dane=dane)


def spr_pliku_wyjscia(nazwa_pliku):

    if nazwa_pliku.endswith(".csv"):
        ob_csv.output_csv(dane=dane,lokalizacja=lokalizacja)
    elif nazwa_pliku.endswith(".json"):
        ob_json.output_json(dane=dane)
    elif nazwa_pliku.endswith(".pickle"):
        ob_pickle.output_pickle(dane=dane)
    elif nazwa_pliku.endswith(".txt"):
        ob_txt.output(dane=dane)


dane = []
lokalizacja = input("Podaj lokalizację.Jeżeli nie podasz nic plik zostanie zapisany w bieżacej lokalizacj. :")
if lokalizacja == "":
    lokalizacja = os.path.join(os.getcwd(), str(sys.argv[2]))
    print(lokalizacja)
else:
    lokalizacja= os.path.join(lokalizacja,str(sys.argv[2]))

ob_csv = PlikiCsv()
ob_json = PlikiJson()
ob_pickle = PlikiPickle()
ob_txt = PlikiTxt()

# Pliki().spr_pliku()
spr_typ_pliku_wejscie(Pliki().dane_wejsciowe)
print(dane)
spr_pliku_wyjscia(Pliki().dane_wyjsciowe)

print(os.getcwd())

