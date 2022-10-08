"""
Scrivi un programma in Python nel quale assegni alla
variabile lista voti una lista con tutti i tuoi voti (al-
meno 6 voti). Sfrutta l'indicizzazione per:
> stampare la lista senza il primo e l'ultimo voto;
sostituire il quarto voto con un 10;
> stampare i primi 3 voti della lista.
"""
voti = [8, 9.32, 7.75, 7, 8]
print(voti[1:-1:])
voti[3] = 10
print(voti[:2:])
