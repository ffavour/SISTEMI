"""
Scrivi un programma in Python che, assegnata una pa-
rola di almeno 8 lettere a una variabile stringa, stampi
tutta la parola con un carattere? al posto della terza
lettera.
"""
parola = input("inserire una parola: ") #stringhe sono immutabili
s1 = parola[0]+"?"+ parola[2:]
print(s1)
