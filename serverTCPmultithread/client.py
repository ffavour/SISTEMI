import socket as sck



def trovaFattori(numero):
    listaFattori = []
    for i in range(2, numero):
        if numero % i == 0:
            listaFattori.append(i)
    print(listaFattori)


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)  # istanzio un socket
    server_address = ("127.0.0.1", 8000)  # tupla con ip e porta (del server - destinatario)

    s.connect(server_address)
    trovaFattori(8)

    while True:
        numero = s.recv(4096)
        print(f"numero ricevuto: {numero.decode()}")
        s.sendall(b"OK")

    s.close()


if __name__ == "__main__":
    main()
