# per trovare numero primo: ciclare da 2 a radice del numero

"""
client chiede numero
server lo manda
client trova i fattori primi del numero
"""
import socket as sck
import threading

dict_integer = {
    1: 33496218871,
    2: 28367584537,
    3: 20826399667,
    4: 18404793689,
    5: 34492812349,
    6: 24182790791}


class ClientThread(threading.Thread):
    def __init__(self, conn, address, numero):
        super().__init__()
        self.conn = conn
        self.address = address
        self.numero = numero

    def run(self):
        n = str(self.numero)
        self.conn.sendall(n.encode())
        data = self.conn.recv(4096)
        print(f"messaggio ricevuto: {data.decode()} da {self.address}")


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    my_address = ("127.0.0.1", 8000)
    s.bind(my_address)

    s.listen()
    clientList = []
    risposte = []

    # print(dict_integer[1])

    k = 0
    while True:
        conn, address = s.accept()
        ident = k % 2
        client = ClientThread(conn, address, ident)
        clientList.append(client)
        client.start()
        client.run()
        k += 1


if __name__ == "__main__":
    main()
