import socket
from datetime import date
from datetime import datetime

data = date.today()
ora = datetime.now()


def controlloComandi(comandoClient):
    rispostaClient = ""

    if comandoClient == 1:
        print("invio data e ora")
        rispostaClient = "data: " + str(data) + " ora: " + str(ora)
    elif comandoClient == 2:
        print("invio data")
        rispostaClient = "data: " + str(data)
    elif comandoClient == 3:
        print("invio ora")
        rispostaClient = "ora: " + str(ora.hour) + str(ora.min) + str(ora.second)

    print(rispostaClient)
    return rispostaClient


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_address = ("127.0.0.1", 5000)
    s.bind(my_address)

    while True:
        text_received, address = s.recvfrom(4096)

        print(f"ricevuto: {text_received.decode()} da {address}")  # .decode per trasformare in ascii
        risposta = controlloComandi(int(text_received.decode()))
        print(risposta)

        s.sendto(risposta.encode(), address)


if __name__ == "__main__":
    main()
