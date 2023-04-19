import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_address = ("0.0.0.0", 5000)
    s.bind(my_address)  # lega socket (concetto informatico) a concetto tcp/ip (ip e porta)

    while True:
        text_received, address = s.recvfrom(4096)
        print(f"ricevuto: {text_received.decode()} da {address}")  # .decode per trasformare in ascii
        s.sendto(b"OK", address)  # invia un ok al client


if __name__ == "__main__":
    main()
