import socket


def menu():
    print(f"premi 1 per data e ora")
    print(f"premi 2 per data")
    print(f"premi 3 per ora")


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("127.0.0.1", 5000)

    while True:
        menu()
        text = input("inserire un numero: ")
        if text == "EXIT":
            break
        text_b = text.encode()
        s.sendto(text_b, server_address)

        text_received, address = s.recvfrom(4096)
        print(f"ricevuto: {text_received.decode()} da {address}")

    s.close()


if __name__ == "__main__":
    main()
