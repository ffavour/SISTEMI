import socket as sck
import random


def sorteggiaParola(lista):
    pos = random.randrange(0, len(lista))
    parolaEstratta = lista[pos]
    return parolaEstratta


def creaParola(lista):
    parola = ""
    for lettera in lista:
        if lettera != "]" and lettera != "[" and lettera != "'":
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


def gioco(nTentativi, parolaSort):  # gioco senza socket
    while True:
        parolaInserita = input("inserisci una parola: ")
        output = confrontaParole(parolaInserita, parolaSort)
        print(output)
        nTentativi -= 1
        if not controlloVittoria(parolaInserita, output) and nTentativi < 1:
            print(f"hai perso\nla parola era: {parolaSort}")
            break
        elif controlloVittoria(parolaInserita, output):
            break


def leggiFile():
    listaParole = []

    file = open("./listaParole.txt")
    listaParoleTemp = file.readlines()
    file.close()

    # print(listaParoleTemp)

    for riga in listaParoleTemp:
        riga_senza_linefeed = riga[:-1]  # senza messa a capo
        listaCampi = riga_senza_linefeed.split(",")  # fa lavoro strtok in
        listaParole.append(listaCampi[0])
        #creaParola(listaCampi)
        #print(listaCampi[0])
    #print(listaParole)

    return listaParole

def creaListaPerLivello(livello, lunghezzaParole, listaParole):
    l = []
    if livello == 1:
        for parola in listaParole:
            if len(parola) <= lunghezzaParole[0]:
                l.append(parola)
    elif livello == 2:
        for parola in listaParole:
            if lunghezzaParole[0] < len(parola) < lunghezzaParole[1]:
                l.append(parola)
    elif livello == 3:
        for parola in listaParole:
            if len(parola) >= lunghezzaParole[1]:
                l.append(parola)
    return l

def ricercaParolaNellaLista(parolaRicercata, listaLivello):
    trovato = False
    parola = ""
    k = 0
    while k < len(listaLivello) and trovato == False:
        if parolaRicercata == listaLivello[k]:
            trovato = True
            break
        k += 1

    if trovato == False:
        parola = sorteggiaParola(listaLivello)
    else:
        parola = parolaRicercata

    return parola




def main():
    server = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    myAddress = ("127.0.0.1", 8000)  # ip server
    server.bind(myAddress)

    # non serve è di prova
    listaParole2 = ["scuola", "gioco", "alfabeto", "penna", "pugno", "cane"]
    parolaSort2 = sorteggiaParola(listaParole2)

    listaParole = leggiFile()
    parolaSort = sorteggiaParola(listaParole)
    # print(listaParole)

    print(parolaSort)  # la parola sorteggiata

    nTentativi = 3  # numero di tentativi per indovinare la parola
    # gioco(nTentativi, parolaSort)

    listaLughezze = [4, 7]  # lista per le lunghezze dei vari livelli
    # print(f"{listaLughezze[0]}  {listaLughezze[1]}")

    listaLivello1 = creaListaPerLivello(1, listaLughezze, listaParole)
    #print(f"livello 1: {listaLivello1}")
    listaLivello2 = creaListaPerLivello(2, listaLughezze, listaParole)
    #print(f"livello 2: {listaLivello2}")
    listaLivello3 = creaListaPerLivello(3, listaLughezze, listaParole)
    #print(f"livello 3: {listaLivello3}")

    while nTentativi > 0:
        livelloClient, address = server.recvfrom(4096)  # riceve livello da client
        print(f"livello: {int(livelloClient)} del client{address}")

        # controlla lunghezza parola in base al livello
        listaLivelloSel = []
        if int(livelloClient) == 1:
            parolaSort = ricercaParolaNellaLista(parolaSort, listaLivello1)
        elif int(livelloClient) == 2:
            parolaSort = ricercaParolaNellaLista(parolaSort, listaLivello2)
        elif int(livelloClient) == 3:
            parolaSort = ricercaParolaNellaLista(parolaSort, listaLivello3)
        # print(parolaSort)


        parolaClient, address = server.recvfrom(4096)
        print(f"parola client {address}: {parolaClient.decode()}")
        output = confrontaParole(parolaClient.decode(), parolaSort)

        print(output)
        server.sendto(output.encode(), address)  # manda parola di output

        if controlloVittoria(parolaClient.decode(), output):
            s = "hai vinto!"
            server.sendto(s.encode(), address)  # mex di vittoria
            break
        elif nTentativi <= 1 and not controlloVittoria(parolaClient.decode(), output):
            print(f"hai perso\nla parola era: {parolaSort}")
            mex = "hai perso\nla parola era: " + parolaSort
            server.sendto(mex.encode(), address)  # game over
            break
        elif not controlloVittoria(parolaClient.decode(), output) and nTentativi > 0:
            s = "riprova"
            server.sendto(s.encode(), address)  # riprova

        nTentativi -= 1

    server.close()


if __name__ == "__main__":
    main()
