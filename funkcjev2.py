#!/usr/bin/python3
import sys

def dodawanie(a,b):
	c = a + b
	return c 

def odejmowanie(a,b):
	c = a - b
	return c 

def mnozenie(a,b):
	c = a * b 
	return c 

def dzielenie(a,b):
	c = a / b
	return c 

def zlyWybor():
	print("Dokonales zlego wyboru!")
	sys.exit()

while(True):
	a = int(input("Podaj pierwsza liczbe: "))
	b = int(input("Podaj druga liczbe: " ))
	c = input("wybierz rodzaj dzialania 1 - dodawanie, 2 - odejmowanie, 3 - mnozenie, 4 - dzielenie ")

	if(c == '1'):
		wynik = dodawanie(a,b)
	elif(c == '2'):
		wynik = odejmowanie(a,b)
	elif(c == '3'):
		wynik = mnozenie(a,b)
	elif(c == '4'):
		wynik = dzielenie(a,b)
	else:
		zlyWybor()
		
	print("wynik dzialania to: ", wynik)