def main():
    stringa = "(hey)"

    lista = []
    
    for lettera in stringa:
        lista.append(lettera)
    
    print(lista)

    ind = 0    
    for elemento in lista:
        if(elemento == "[" or elemento == "(" or elemento == "{"):
          parentesi = lista.pop(int(elemento))
          #print(parentesi)
        """if(elemento == "]" or elemento == ")" or elemento == "}"):
            pass
        ind += 1"""
    
    #print(parentesi)


if __name__ == "__main__":
        main()