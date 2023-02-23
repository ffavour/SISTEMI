import pygame
from pygame.locals import *


def caricaMappa(mappa):
    file = open("C:\\Users\\favou\Documents\\4A\\sistemi\\phyton\\esercizi\\matriceAdiacente\\file.csv", "r")
    lista_righe = file.readlines()
    file.close()

    for riga in lista_righe:
        riga_senza_linefeed = riga[:-1]
        mappa.append(riga_senza_linefeed.split(","))  # fa lavoro strtok in c

    return mappa


def creaMappaNumerata(mappa1, mappa2):
    mappa2 = mappa1
    cont = 0  # contatore progressivo degli zeri

    for r in range(len(mappa2)):
        riga = mappa2[r]
        for c in range(len(mappa2)):
            if riga[c] == '1':
                mappa2[r][c] = -1
            else:
                mappa2[r][c] = cont
                cont += 1

    return mappa2


def PrintMatriceAdiacente(mat):
    matAd = []
    c = False
    for el1 in mat:
        l = []
        for k in range(len(mat)):
            c = False
            for j in range(len(el1)):
                if k == el1[j]:
                    l.append(1)
                    c = True
            if c == False:
                l.append(0)
        matAd.append(l)
    # print(matAd)

    for k in matAd:
        print(k)


def creaMappaSpaziLiberi(matAd, mappa):
    for n, riga in enumerate(mappa):
        for k, el in enumerate(riga):
            if el != -1:
                l = []
                # destra
                if k != (len(riga) - 1) and riga[k + 1] != -1:
                    l.append(riga[k + 1])
                    # print(l)
                # sinistra
                if k != 0 and riga[k - 1] != -1:
                    l.append(riga[k - 1])
                # sopra
                if n != 0 and mappa[n - 1][k] != -1:
                    l.append(mappa[n - 1][k])
                # sotto
                if n != (len(riga) - 1) and mappa[n + 1][k] != -1:
                    l.append(mappa[n + 1][k])
                matAd.append(l)

    return matAd


def creaMatriceAdiacenza(mat):
    matAd = []

    c = False
    for el1 in mat:
        l = []
        for k in range(len(mat)):
            c = False
            for j in range(len(el1)):
                if k == el1[j]:
                    l.append(1)
                    c = True
            if c == False:
                l.append(0)
        matAd.append(l)
    # print(matAd)

    for k in matAd:
        print(k)

def main():
    mappa = []  # mappa iniziale
    mappaNumerata = []
    mappaSpaziLiberi = []
    matriceAdiacenza = []

    caricaMappa(mappa)
    # print(mappa)

    mappaNumerata = creaMappaNumerata(mappa, mappaNumerata)
    # print(mappaNumerata)

    mappaSpaziLiberi = creaMappaSpaziLiberi(matriceAdiacenza, mappa)
    # print(mappaSpaziLiberi)

    creaMatriceAdiacenza(matriceAdiacenza)


if __name__ == "__main__":
    main()
