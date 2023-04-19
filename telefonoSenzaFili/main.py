import socket


def main():
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket per ricevere
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket per inviare

    myAddress = ("0.0.0.0", 5000)
    s1.bind(myAddress)

    while True:
        mexRicevuto, address = s1.recvfrom(4096)
        print(f"ricevuto: {mexRicevuto.decode()} da {address}")
        s2.sendto(mexRicevuto, "127.0.0.1")


if __name__ == "__main__":
    main()
