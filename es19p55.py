"""
Scrivi un programma in phyton che permetta all'utente
di inserire due numeri qualsiasi. Crea un dizionario in cui 
salvi la media aritmetica e la media geometrica dei due
numeri. Stampa il dizionario
"""

num1 = int(input("inseire primo numero: "))
num2 = int(input("inseire primo numero: "))

mA = (num1 + num2) / 2
mG = (num1 * num2)**0.5

d = {"media aritmetica": mA, "media geometrica":mG}
print(d)