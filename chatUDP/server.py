import socket

"""
per aggiungere client => ?nomeUtente
"""


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_address = ("127.0.0.1", 8000)
    s.bind(my_address)

    while True:
        mex, address = s.recvfrom(4096)


if __name__ == "__main__":
    main()
