"""
Scrivi un programma in Python che permetta all'utente
di inserire due numeri. Crea una lista contenente:
> la somma dei quadrati dei due numeri;
> Il quadrato della somma dei numeri;
> la differenza tra i quadrati dei due numeri;
> il quadrato della differenza tra i numeri.
Stampa la lista ottenuta
"""
num = int (input("inserire un numero: "))
num2 = int (input("inserire un altro numero: "))

l = [(num**2 + num2**2), ((num + num2)**2), (num**2 + num2**2), ((num + num2)**2)]
print(l)
