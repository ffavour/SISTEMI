import socket as sck


def main():
    client = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    serverAddress = ("127.0.0.1", 8000)

    nTentativi = 3  # è uguale per server e client

    while nTentativi > 0:
        parola = input("inserisci una parola per continuare: ")
        client.sendto(parola.encode(), serverAddress)
        output, serverAddress = client.recvfrom(4096)
        print(output.decode())
        mex, serverAddress = client.recvfrom(4096)
        print(mex.decode())

        nTentativi -= 1


if __name__ == "__main__":
    main()
