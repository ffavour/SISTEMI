import socket


def leggiFile():
    file = open("file.txt", "rb")
    dati = file.readlines()
    file.close()

    return dati[0]


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("127.0.0.1", 8000)

    data = leggiFile()

    while True:
        print(f"dati file: {data}")
        s.sendto(data, server_address)
        mex, address = s.recvfrom(4096)
        print(f"{mex}")
        break

    s.close()


if __name__ == "__main__":
    main()
