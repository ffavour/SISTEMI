"""
Scrivi un programma in Python in cui inizializzi la lista
X = [0, 1, 2, 3, 5, 6, 7, 8] e poi che:
> crei due nuove liste contenenti ciascuna una delle
due metà della lista;
> aggiungi il valore 5 alla lista contenente la prima
metà.
"""
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
a = len(x)//2

x1 = x[1:a:]
x2 = x[a::]
x1.append = 5

print(x)
print(x1)
print(x2)
