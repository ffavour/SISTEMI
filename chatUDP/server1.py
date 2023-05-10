import socket as sck

ipServer = '0.0.0.0'
s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
serverAddress = (ipServer, 8000)
s.bind(serverAddress)
continua = True
contatti = {}


def main():
    while continua:
        textRecived, address = s.recvfrom(4096)
        lParametri = textRecived.decode().split(';')

        if lParametri[1][0] == '?':
            contatti[lParametri[1][1:]] = address
            print(contatti)
        else:
            print(f"riceved: {textRecived.decode()} -> fromIP: {address}")
            add = ''
            for k, v in contatti.items():
                if lParametri[1] == k:
                    add = v

            s.sendto(lParametri[0].encode(), add)


if __name__ == '__main__':
    main()
