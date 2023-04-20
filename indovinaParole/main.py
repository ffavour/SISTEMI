import socket as sck
import random


def sorteggiaParola(lista):
    pos = random.randrange(0, len(lista))
    parolaEstratta = lista[pos]
    return parolaEstratta


def creaLista(parola):
    lista = []
    for lettera in parola:
        lista.append(lettera)
    return lista


def creaParola(lista):
    parola = ""
    for lettera in lista:
        parola += lettera
    return parola


def confrontaParole(parolaUtente, parolaSorteggiata):
    listaParolaFinale = []

    # lunghezza max
    if len(parolaUtente) > len(parolaSorteggiata):
        lunghezzaParolaFinale = len(parolaUtente)
    else:
        lunghezzaParolaFinale = len(parolaSorteggiata)

    # crea la parola con le lettere indovinate
    for k in range(0, lunghezzaParolaFinale):
        # controllo di non uscire dalla lista
        if k >= len(parolaUtente) or k >= len(parolaSorteggiata):
            break

        if parolaSorteggiata[k] == parolaUtente[k]:
            listaParolaFinale.append(parolaSorteggiata[k])
        else:
            listaParolaFinale.append("_")

    # controlla che la lunghezza della parola finale sia = a parola sorteggiata
    if len(listaParolaFinale) < len(parolaSorteggiata):
        for i in range(0, (len(parolaSorteggiata) - len(listaParolaFinale))):
            listaParolaFinale.append("_")

    parolaFinale = creaParola(listaParolaFinale)

    return parolaFinale


def controlloVittoria(parolaUtente, parola):
    if parolaUtente == parola:
        print(f"hai vinto!")
        return True
    else:
        return False


def gioco():
    pass


def main():
    server = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    myAddress = ("127.0.0.1", 8000)
    server.bind(myAddress)

    client = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    serverAddress = ("127.0.0.1", 8000)

    listaParole = ["scuola", "gioco", "alfabeto", "penna", "pugno", "cane"]
    parolaSort = sorteggiaParola(listaParole)
    # print(parolaSort)

    nTentativi = 5  # numero di tentativi per indovinare la parola

    while True:
        parolaInserita = input("inserisci una parola: ")
        output = confrontaParole(parolaInserita, parolaSort)
        print(output)
        nTentativi -= 1
        if controlloVittoria(parolaInserita, output) or nTentativi <= 0:
            if nTentativi <= 0:
                print(f"hai perso\n la parola era: {parolaSort}")
            break


if __name__ == "__main__":
    main()
