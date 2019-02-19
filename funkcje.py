def odczytaj_z_ekranu(teskt_zachety):
	
	lista = []

	linia ="..."

	while linia:
		linia = input(teskt_zachety)
		if linia: lista.append(linia)

	return lista

