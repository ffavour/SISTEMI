"""
Scrivi un programma in Python in cui:
> inizializzi due variabili, prima e seconda, con due
numeri interi diversi a tua scelta;
> stampi i valori delle variabili usando una sola f-string;
> scambi i valori tra le due variabili;
> stampi i nuovi valori della variabili usando una sola
f-string.
"""

prima, seconda = 5, 7  #assegnazione multipla

print(f'il valore della 1^ variabile è {prima}, quello 2^ è {seconda}')

prima, seconda = seconda, prima

print(f'i valori delle due varibili scambiate sono: {prima} e {seconda}')