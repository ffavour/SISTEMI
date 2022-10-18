num = int(input("inserire un numero: "))

if (num % 2 == 0) & (num % 5 == 0) & (num % 3 == 0):
    print("il numero è divisibile per 2, 3 e 5")
elif (num % 2 == 0) & (num % 5 == 0) & (num % 3 != 0):
    print("il numero è divisibile per 2 e 5")
elif(num % 2 == 0) & (num % 5 != 0) & (num % 3 == 0):
    print("il numero è divisibile per 2 e 3")
elif(num % 2 != 0) & (num % 5 == 0) & (num % 3 == 0):
    print("il numero è divisibile per 3 e 5")
elif(num % 2 != 0) & (num % 5 != 0) & (num % 3 != 0):
    print("il numero non è divisibile per 2, 3 e 5")
