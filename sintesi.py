lista1 = ["a", "b", "c", "d"]
lista2 = [1, 2, 3, 4]

#for su lista1 C-style
print("for su lista1 C-style: ", end=" ")
for indice in range(0, len(lista1)):
	print(lista1[indice], end=" ")

#for su lista1 Python style
print("\nfor su lista1 Python style: ", end=" ")
for elemento in lista1:
    print(elemento, end=" ")

#for su lista1 con enumerate
print("\nfor su lista1 con enumerate: ", end=" ")
for indice, elemento in enumerate(lista1):  #cicla su indice ed elemento
    print(elemento, end=" ")

#for su lista1 e lista2 python-style (zip)
print("\nfor su lista1 e lista2 python-style (zip): ", end=" ")
for elemento1, elemento2 in zip(lista1, lista2):  
        print(elemento1, elemento2, end=" - ")

#for su lista1 e lista2 c-style (range..)
for c in range(0, len(lista1)):
    print(lista1[c], lista2[c], end=" - ")


diz ={1:"a", 2:"b", 3:"c"}

#for su diz usando items()
print("\nfor su diz usando items(): ")
for chiave, valore in diz.items():
    print(chiave, valore, end=" ")

#for su diz senza items()
print("\nfor su diz senza items(): ")
for chiave in diz:
    print(chiave, diz[chiave], end=" ")
