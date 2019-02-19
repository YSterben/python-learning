#!/usr/bin/python3

def f1(f, str):
	f(str)


def wywolaj(lista_funkcji, ktora):
	lista_funkcji[ktora]("kkk")

wywolaj([print],0)

lista = [
	("1. print", print),
	("2. input", input)
	]

lista[1][1]()