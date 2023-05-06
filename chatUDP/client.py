import socket

"""
per aggiungere client => ?nomeUtente
"""


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("127.0.0.1", 8000)

    while True:
        nomeUtente = input("inserisci il tuo nome: ")
        nomeUtenteS = "?" + nomeUtente
        s.sendto(server_address, nomeUtenteS)



if __name__ == "__main__":
    main()
