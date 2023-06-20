import networkx as nx


def main():
    nodi = ["a", "b", "c", "d", "e", "f", "g"]
    a = [[0, 2, 0, 0, 1, 0, 0],
         [2, 0, 4, 0, 0, 4, 0],
         [0, 4, 0, 1, 1, 0, 1],
         [0, 0, 1, 0, 2, 0, 2],
         [1, 0, 1, 2, 0, 3, 0],
         [0, 4, 0, 0, 3, 0, 2],
         [0, 0, 1, 2, 0, 2, 0]]

    dizionario_adiacenze = {n: {} for n in nodi}
    for i, n_i in enumerate(nodi):
        for j, peso in enumerate(a[i]):
            if peso > 0:
                dizionario_adiacenze[n_i][nodi[j]] = {"weight": peso}

    nodo_iniziale = "a"
    nodi_etichettati = {nodo: {"label": 999999, "predecessore": None,
                               "usato": False} for nodo in nodi}
    nodi_etichettati[nodo_iniziale]["label"] = 0
    successori = [nodo_iniziale]

    while len(successori) > 0:
        print(successori)

        label_min = nodi_etichettati[successori[0]]["label"]
        nodo_min = successori[0]
        for s in successori:
            if nodi_etichettati[s]["label"] < label_min:
                label_min = nodi_etichettati[s]["label"]
                nodo_min = s

        successori.remove(nodo_min)
        nodi_etichettati[nodo_min]["usato"] = True

        nodi_vicini = dizionario_adiacenze[nodo_min]
        for nodo_vicino in nodi_vicini:
            if not (nodi_etichettati[nodo_vicino]["usato"]):
                if nodo_vicino not in successori:
                    successori.append(nodo_vicino)
                nuova_distanza = nodi_etichettati[nodo_min]["label"] + nodi_vicini[nodo_vicino]["weight"]
                if nodi_etichettati[nodo_vicino]["label"] > nuova_distanza:
                    nodi_etichettati[nodo_vicino]["label"] = nuova_distanza
                    nodi_etichettati[nodo_vicino]["predecessore"] = nodo_min
        print(successori)

        print(dizionario_adiacenze )


if __name__ == "__main__":
    main()
