import socket as sck


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)  # istanzio un socket
    server_address = ("127.0.0.1", 8000)  # tupla con ip e porta (del server - destinatario)

    s.connect(server_address)

    while True:
        mex = input("scrivi un messaggio: ")
        if mex == "EXIT":
            break
        s.sendall(mex.encode())
        data = s.recv(4096)
        print(f"messaggio ricevuto: {data}")

    s.close()


if __name__ == "__main__":
    main()
