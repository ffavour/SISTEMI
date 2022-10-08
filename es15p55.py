"""
Scrivi un programma in Python che permetta all'utente
di inserire il suo nome (tramite input ()) e che stampi
il nome in cui tutti i caratteri tranne il primo sono sosti-
tuiti da un *
"""
nome = input("inserire il nome: ")
a = '*'
print(nome[0] + a * (len(nome)) - 1)
