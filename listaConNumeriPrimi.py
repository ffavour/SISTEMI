def primo(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

#modo 1
lista = []
for i in range(0, 100):
        if(primo(i) == True):
                lista.append(i)

print(lista)

#modo 2, usa un filtro (if) con la condizione sulla variabile i
l = [i for i in range(2, 100) if primo(i)]
print(l)