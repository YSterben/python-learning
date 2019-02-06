import random

print("Czesc zagraj ze mna w zgadywanke,wymyslilem liczbe od 1 do 10.Zgadnij jaka")
wylosowana_liczba = random.randint(1,11)

zgadles=False
while not zgadles:
    liczba = int(input("wpisz liczbe: "))
    if wylosowana_liczba == liczba:
        print("Zgadles!!!")
        zgadles=True        

    if wylosowana_liczba > liczba:
        print("Nie zgdles,za mala liczba. ")

    if wylosowana_liczba < liczba:
        print("Nie zgdles,za duzo")

    
