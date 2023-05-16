import socket as sck


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    server_address = ("127.0.0.1", 8000)

    s.connect(server_address)

    while True:
        comando = input("inserisci un comando [com; valore]: ")
        if comando == "EXIT":
            break
        s.sendall(comando.encode())
        data = s.recv(4096)
        print(f"messaggio ricevuto: {data.decode()}")

    s.close()


if __name__ == "__main__":
    main()
