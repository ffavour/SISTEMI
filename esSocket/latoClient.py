import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # istanzio un socket
    server_address = ("192.168.1.122", 5000)  # tupla con ip e porta

    while True:
        text = input("Scrivi un messaggio: ")
        if text == "EXIT":
            break
        text_b = text.encode()  # trasforma testo in binario
        s.sendto(text_b, server_address)
        text_received, address = s.recvfrom(4096)
        print(f"ricevuto: {text_received.decode()} da {address}")

    s.close()


if __name__ == "__main__":
    main()
