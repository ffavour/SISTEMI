import matplotlib.pyplot as plt

import numpy as np


def leggiFileAnomaly():
    fileAnomaly = []
    file = open("./Temperature_Anomaly.csv")
    lista_tempAnomaly = file.readlines()
    file.close()

    # print(lista_tempAnomaly)

    for riga in lista_tempAnomaly:
        riga_senza_linefeed = riga[:-1]  # senza messa a capo
        listaCampi = riga_senza_linefeed.split(",")  # fa lavoro strtok in
        fileAnomaly.append(listaCampi)
        # print(listaCampi)

    # print(fileAnomaly)
    fileAnomalyNoIntestaz = fileAnomaly[5:]  # toglie intestazione

    return fileAnomalyNoIntestaz


def leggiFileCO2Emissions():
    fileCo2 = []
    file = open("CO2_emissions.csv")
    lista_CO2 = file.readlines()
    file.close()

    for riga in lista_CO2:
        riga_senza_linefeed = riga[:-1]
        listaCampi = riga_senza_linefeed.split(",")
        fileCo2.append(listaCampi)

    fileCo2_NoIntestaz = fileCo2[1:]

    return fileCo2_NoIntestaz


def main():
    # per il primo file
    annoAnomaly = []
    valoreAnomaly = []

    # per il secondo file
    annoCO2 = []
    totale = []
    benzinaLiquida = []
    benzinaGas = []
    benzinaSolida = []
    cemento = []
    combustioneGas = []
    proCapite = []

    fileAnomaly = leggiFileAnomaly()
    fileAnomalyConGag = fileAnomaly[::20]  # serve per rendere grafico leggibile
    # print(fileAnomaly)

    fileCO2Emssions = leggiFileCO2Emissions()
    # print(fileCO2Emssions)

    for riga in fileAnomaly:
        annoAnomaly.append(int(riga[0]))
        valoreAnomaly.append(float(riga[1]))

    # print(annoAnomaly)
    # print(valoreAnomaly)

    fileCO2EmssionsConGap = fileCO2Emssions[::50]

    for riga in fileCO2Emssions:
        annoCO2.append(int(riga[0]))
        totale.append(int(riga[1]))
        benzinaGas.append(int(riga[2]))
        benzinaLiquida.append(int(riga[3]))
        benzinaSolida.append(int(riga[4]))
        cemento.append(int(riga[5]))
        combustioneGas.append(int(riga[6]))
        proCapite.append(float(riga[7]))

    # grafico anomalie
    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(annoAnomaly, valoreAnomaly)
    ax1.set(xlabel='anno', ylabel='valore di anomalia')
    # title='anomalie di temperatura')

    # fig, (ax2) = plt.subplots(1, 1)
    # grafico emissioni
    ax2.plot(annoCO2, benzinaLiquida, label='benzina liquida')
    ax2.plot(annoCO2, benzinaSolida, label='benzina solida')
    ax2.plot(annoCO2, benzinaGas, label='benzina gas')
    ax2.plot(annoCO2, totale, label='totale')
    ax2.plot(annoCO2, cemento, label='cemento')
    ax2.plot(annoCO2, combustioneGas, label='combustione gas')
    ax2.plot(annoCO2, proCapite, label='pro capite')
    ax2.set_xlabel('anno')
    ax2.set_ylabel('emissioni')
    # ax2.set_title("emissioni annue di CO2")
    ax2.legend()

    plt.show()

    # fig(ax1....ax7)
    # plot(x, y)
    # set x label e y


if __name__ == "__main__":
    main()
