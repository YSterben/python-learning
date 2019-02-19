#!/usr/bin/python3
from funkcje import *

print("program lista gosci")
lista_gosci = odczytaj_z_ekranu("podaj imie ")

lista_gosci.sort()
for imie in lista_gosci:
	print(imie.title(), "zapraszam cie na moje urodziny")
