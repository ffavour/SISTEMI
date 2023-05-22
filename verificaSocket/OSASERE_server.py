import socket as sck
import threading

"""Il seguente client invia a un server di controllo la temperatura della CPU  (simulata con un numero pseudocasuale) 
e il suo ID univoco. Il server deve ricevere ID e temperatura da tutti i client che si connettono. Inoltre il server 
deve stampare un allarme per quei client con temperatura >=70°C. L'allarme deve essere stampato soltanto al 
superamento della temperatura di 70°C, per cui quando la temperatura scende nuovamente sotto i 70°C, il server stampa 
che l'allarme è rientrato. In tutte le stampe deve essere  presente l'ID univoco del client."""


class ClientThread(threading.Thread):
    def __init__(self, conn, address):
        super().__init__()
        self.conn = conn
        self.address = address
        self.temp = None

    def run(self):
        while True:
            data = self.conn.recv(4096)  # riceve dato da client
            print(f"messaggio ricevuto: {data.decode()} da {self.address}")

            dataDecodificato = data.decode()
            listaInfo = []
            listaInfo = dataDecodificato.split(":")  # divide la stringa e la salva in lista
            # print(listaInfo)

            self.temp = float(listaInfo[1])  # converte temperatura in float
            id = listaInfo[0]  # salva id in una variabile
            # print(temp)

            buffer = self.temp  # salva temperatura in un buffer

            # controllo sulla temperatura

            if self.temp >= 70:
                print(f"ALLARME su client {id}")
            if self.temp < 70 and buffer >= 70:
                print(f"l'allarme di client {id} è rientrato")
            buffer = 0


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)  # istanzia socket
    my_address = ("127.0.0.1", 11000)  # tupla con ip e porta
    s.bind(my_address)  # lega ip e porta a server

    s.listen()  # si mette in "ascolto" per connessioni da client
    clientList = []  # lista di client connessi

    while True:
        conn, address = s.accept()  # accetta connessioni
        client = ClientThread(conn, address)  # istanzia oggetto client
        clientList.append(client)
        client.start()  # parte il thread


if __name__ == "__main__":
    main()
