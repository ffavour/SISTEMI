
#eserecizio dei matematici
def leggifile():
    file = open("C:\\Users\\favou\Documents\\4A\\sistemi\\phyton\\esercizi\\fileEsempio\\matematici.csv", "r")
    righe = file.readlines()
    file.close()

    diz = {"id":[], "nome":[]}

    for riga in righe[1:]:
        campi_riga = riga[:-1].split(",")
        diz["id"].append(int(campi_riga[0]))
        diz["nome"].append(campi_riga[1][1:])
    
    return diz

def nomeId(id, diz):
    litaID = diz["id"]
    listaNome = diz["nome"]

    for i, n in zip(litaID, listaNome):  #zip scorre liste in parallelo
        if i == id:
            return n


def main():
    diz = leggifile()
    print(diz)

    id = 2
    nome = nomeId(id, diz)
    print(nome)


if __name__=="__main__":
		main()