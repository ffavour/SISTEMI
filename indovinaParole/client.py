import socket as sck


def main():
    client = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    serverAddress = ("127.0.0.1", 8000)

    while True:
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