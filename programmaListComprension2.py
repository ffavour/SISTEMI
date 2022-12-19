"""
programma che toglie vocali
"""
vocali = ['a', 'e', 'i', 'o', 'u']
carattere = 'b'

#print(carattere in vocali)  #la parola chiave in indica il simbolo di appartenenza in py
parola = input("inserire una parola: ")
l = [c for c in parola if (c in vocali) == False] #crea lista di cara
print(l)
