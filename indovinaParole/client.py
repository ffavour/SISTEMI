import socket as sck


def controllaNumero(num):
    if 1 <= num <= 3:
        return True
    else:
        return False


def impostaLivello():
    while True:
        l = int(input("livello pls: "))
        if 1 <= l <= 3:
            break
    return l


def main():
    client = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    serverAddress = ("127.0.0.1", 8000)
    livello = 0

    while True:
        # imposta il livello di difficoltà
        if not controllaNumero(livello):
            livello = impostaLivello()

        client.sendto((str(livello)).encode(), serverAddress)  # invia livello a server

        parola = input("inserisci una parola per continuare: ")
        client.sendto(parola.encode(), serverAddress)

        output, serverAddress = client.recvfrom(4096)
        print(output.decode())

        mex, serverAddress = client.recvfrom(4096)
        print(mex.decode())

        if mex.decode() != "riprova":
            break

    client.close()


if __name__ == "__main__":
    main()
