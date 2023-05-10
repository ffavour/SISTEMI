import socket as sck
from threading import Thread, Lock

ipServer = '127.0.0.1'
serverAddress = (ipServer, 8000)
s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
continua = True


class thredSend(Thread):
    def _init_(self, s, serverAddress):
        Thread.__init__(self)
        self.s = s
        self.serverAddress = serverAddress

    def run(self):
        global continua

        while continua:
            mex = input('mex: ')
            if mex == 'EXIT':
                continua = False
            else:
                id = input('chi? ')
                concatenazione = f'{mex};{id}'
                s.sendto(concatenazione.encode(), serverAddress)
        s.close()


class thredLissen(Thread):
    def _init_(self, s):
        Thread.__init__(self)
        self.s = s

    def run(self):
        global continua

        while continua:
            textRecived, address = s.recvfrom(4096)
            if (textRecived.decode() == 'EXIT'):
                continua = False
            else:
                print(f"text: {textRecived.decode()} -> fromIP: {address}")


def main():
    send = thredSend(s, serverAddress)
    lissen = thredLissen(s)

    send.start()
    lissen.start()

    send.join()
    lissen.join()


if __name__ == '__main__':
    main()
