import pickle
import os

def zapiszDane(daneGosci):
    with open("daneGosci", "wb") as plik:
        pickle.dump(daneGosci, plik)

    def odczytajDane():
        daneGosci = {}
        statinfo = os.stat("daneGosci")
        if (statinfo.st_size == 0):
            return  daneGosci
        try:
            with open("daneGosci", "rb") as  plik:
                daneGosci = pickle.load(plik)
        except EOFError:
            print("Plik jest pusty")
            return daneGosci

def dodajGoscia():
    daneGosci = {}
    nazwisko = input("Podaj nazwisko gościa: ")