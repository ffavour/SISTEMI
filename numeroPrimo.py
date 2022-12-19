"""
scrivi un programma che calcoli se un numero è primo
"""

from pickletools import read_uint1
from re import T
from tkinter import Y


def primo(x):
    cont = 0
    for i in range(2, int(x**0.5)+1):
        y = x % i 
        if y == 0:
           cont+=1
        if cont == 0:
            return True
        else:
            return False

def primo1(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

num = int (input("inserisci un numero: "))

if primo(num) == True:
    print("il numero è primo.")
else:
    print("il numero non è primo.")

