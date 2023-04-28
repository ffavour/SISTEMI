import socket as sck
import threading


class ClientThread(threading.Thread):
    def __init__(self, conn, address):
        super().__init__()
        self.conn = conn
        self.address = address

    def run(self):
        data = self.conn.recv(4096)
        print(f"messaggio ricevuto: {data.decode()} da {self.address}")
        self.conn.sendall(b'OK')


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    my_address = ("127.0.0.1", 8000)
    s.bind(my_address)

    s.listen()
    clientList = []

    while True:
        conn, address = s.accept()
        client = ClientThread(conn, address)
        clientList.append(client)
        client.start()
        client.run()

    """while True:
        data = conn.recv(4096)
        print(f"messaggio ricevuto: {data.decode()} da {address}")
        conn.sendall(b'OK')"""


if __name__ == "__main__":
    main()
