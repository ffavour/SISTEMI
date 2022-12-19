def main():
    tavolaPitagorica = [[indice * numero for numero in range(1, 11)] for indice in range(1, 11)]
    print(tavolaPitagorica)

    for riga in tavolaPitagorica:
        print(f"{riga}\n")

if __name__=="__main__":
		main()