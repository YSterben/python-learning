#!/usr/bin/python3

print("program lista gosci")
lista_gosci = []

imie="..."

while imie:
	imie = input("podaj imie zapraszanej osoby ")
	if imie: lista_gosci.append(imie)

lista_gosci.sort()
for imie in lista_gosci:
	print(imie.title(), "zapraszam cie na moje urodziny")
