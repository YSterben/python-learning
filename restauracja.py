#!/usr/bin/python3

NAZWA_RESTAURACJI = "Pod Kamykiem"

def menu(nazwa_modulu, pozycje_menu):
	
	
	print("")
	powitnie = "Aplikacja restauracji '" + NAZWA_RESTAURACJI +"' - " + nazwa_modulu
	print(powitnie)
	print("-" * len(powitnie))
	while True:	
		print("")
		for pozycja in pozycje_menu:
			print(pozycja[0])
		
		print("")
		wybor = input("wybierz opcje ")
		
		if (( not wybor.isdigit() ) or int(wybor) > len(pozycje_menu)):
			print("Nie prawidlowy wybor")
		else: break
	
	pozycje_menu[int(wybor)-1][1]()
	return wybor

def menu_administratora():
	print("ooo")
	menu("menu administratora", [
 		("1. dodawanie produktow", dodawanie_produktow)
 		("2. zapis", zapis_produkty)
 		("3. odczyt", odczyt_produkty)])

def menu_klienta() : pass 

def dodawanie_produktow(): pass

def zapis_produkty(): pass

def odczyt_produkty(): pass

menu1 = [("1. manu administrator", menu_administratora),
		 ("2. menu klienta", menu_klienta)]


c = menu("menu główne", menu1)

# if c == "1":
# 	menu("menu administratora", [
# 		"1. dodawanie produktow",
# 		"2. zapis",
# 		"3. odczyt"]) 
# elif c == "2": menu("menu klienta", [
# 	"1. złóż zamówiwnie"]) 


