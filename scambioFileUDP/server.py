import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_address = ("127.0.0.1", 8000)
    s.bind(my_address)

    while True:
        mex_client, address = s.recvfrom(4096)
        print(f"ricevuto: {mex_client.decode()} da {address}")
        s.sendto(b"ok", address)
        break

    s.close()


if __name__ == "__main__":
    main()
