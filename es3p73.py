
from shutil import register_unpack_format


def somma(num1, num2):
    return num1 + num2

def differenza(num1, num2):
    return num1 - num2

def prodotto(num1, num2):
    return num1 * num2

def quoziente(num1, num2):
    if num2 != 0:
        return num1 / num2 
    else:
        print("operazione non possibile") 


operazione = input("quale operazione vuoi eseguire?")
operatori = {"piu":"+", "meno":"-", "per":"*", "diviso":"/"}

num1 = int(input("inserire il primo numero: "))
num2 = int(input("inserire il secondo numero: "))

if operazione == operatori["piu"]:
    risultato = somma(num1, num2)
    print(risultato)
elif operazione == operatori["meno"]:
    risultato = differenza(num1, num2)
    print(risultato) 
elif operazione == operatori["per"]:
    risultato = prodotto(num1, num2)
    print(risultato)
elif operazione == operatori["diviso"]:
    risultato = quoziente(num1, num2)
    print(risultato) 


