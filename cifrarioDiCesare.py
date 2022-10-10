parola = input("inserire una parola: ")

dizonario = {'a':'b', 'b':'c', 'c':'d', 'd':'e', 'e':'f', 'f':'g', 'g':'h', 'h':'i', 'i':'l', 'l':'m', 'm':'n', 'n':'o', 'o':'p', 'p':'q', 'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'z', 'z':'a'}
parola2 = ""

for lettera in parola:
    parola2 += dizonario[lettera]
    #print(dizonario[lettera], end="")

print(parola2)