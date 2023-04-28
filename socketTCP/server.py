import socket as sck


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    my_address = ("127.0.0.1", 8000)
    s.bind(my_address)

    s.listen()
    conn, address = s.accept()

    while True:
        data = conn.recv(4096)
        print(f"messaggio ricevuto: {data} da {address}")
        conn.sendall(b'OK')


if __name__ == "__main__":
    main()
