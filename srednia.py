#!/usr/bin/python3
print("program srednia")

liczby = []

liczba = "..."

while liczba:
	liczba = input("podaj liczbe ")
	if liczba.isdigit():
		liczby.append(int(liczba))
	elif liczba: print(liczba,"to nie jest liczba")
	
suma = sum(liczby)
print("suma =",suma)
print("srednia =",suma/len(liczby))