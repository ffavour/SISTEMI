# per trovare numero primo: ciclare da 2 a radice del numero

"""Un server TCP possiede il dizionario di numeri dict_integer = { 1:33496218871, 2:28367584537, 3:20826399667,
4:18404793689, 5:34492812349, 6:24182790791} Ciascun numero è fattorizzabile come il prodotto di due numeri primi. Il
server invia un numero alla volta a uno dei due client connessi e questi rispondono al server con i due fattori primi
trovati. Il server salva i fattori primi di ciascun numero in un apposito dizionario. Il client 1 riceve i numeri 1,
3,5; il client 2 riceve i numeri 2,4,6."""

import socket as sck
import threading

"""dict_integer = {
    1: 33496218871,
    2: 28367584537,
    3: 20826399667,
    4: 18404793689,
    5: 34492812349,
    6: 24182790791}"""

dict_integer = {
    1: 334,
    2: 283,
    3: 208,
    4: 184,
    5: 344,
    6: 241}

indiceClient = 1


def listaIndici():
    l = []
    for elementi in dict_integer:
        l.append(elementi)
    print(l)



class ClientThread(threading.Thread):
    def __init__(self, conn, address):
        global indiceClient
        super().__init__()
        self.conn = conn
        self.address = address
        self.numeroId = indiceClient
        indiceClient += 1

    def run(self):

        for i in range(1, 7):

            if self.numeroId % 2 == 0 and i % 2 == 0:
                numClient = dict_integer[i]
            else:
                numClient = dict_integer[i + 1]

            num_str = str(numClient)
            self.conn.sendall(num_str.encode())

            rispostaClient = self.conn.recv(4096)
            print(rispostaClient.decode())

            fattoriTrovati = self.conn.recv(4096)
            print(fattoriTrovati.decode)


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    my_address = ("127.0.0.1", 8000)
    s.bind(my_address)

    s.listen()
    clientList = []

    listaIndici()

    while True:
        conn, address = s.accept()
        client = ClientThread(conn, address)
        clientList.append(client)
        client.start()


if __name__ == "__main__":
    main()
