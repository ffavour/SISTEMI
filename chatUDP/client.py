# 192.168.1.130
import socket  # nativa
from threading import Thread

s = socket.socket(socket.AF_INET,
                  socket.SOCK_DGRAM)  # costruttore --> con questa riga ho istanziato il socket (creazione del socket)
server_address = ("192.168.1.117", 8000)


class Ricevitore(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            text_received, address = s.recvfrom(4096)
            print(text_received.decode())


def main():
    nickname = "?" + input("inserisci il tuo nome: ")

    print(f"{nickname}")

    s.sendto(nickname.encode(), server_address)
    '''
    while True:
        text_received, server = s.recvfrom(4096)
        if text_received.decode()!="":
            print(text_received)
            break
    '''
    rec = Ricevitore()
    rec.start()

    while True:
        text = input("Scrivi il nome del destinatario: ") + ";" + input("inserisci il testo: ")
        print(text)

        text_b = text.encode()  # passo da stringa a stringa binaria
        s.sendto(text_b, server_address)  # mando il messaggio al server

    s.close()
    rec.join()


if __name__ == "__main__":
    main()
