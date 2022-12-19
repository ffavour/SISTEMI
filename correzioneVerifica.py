from ast import comprehension

#es1
s = "chikakok"
print(s[::2])


#es2
n = int(input("inserire un numero: "))
lista = [1] * n

lista[0], lista[-1] = 0, 0
print(lista)


#es3
n1 = int(input("inserire un numero: "))
l = []

for i in range(1, n1 + 1):
    l.append(i)
print(l)

#es3(variazione)
n2 = int(input("inserire un numero: "))
#list comprehension: crea lista al volo con dentro i valori da 1 a n
l1 = [i for i in range(1, n2 + 1)]

print(l1)
