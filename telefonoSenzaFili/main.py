import socket as sck


server = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
myAddress = ("192.168.1.129", 8000)
server.bind(myAddress)

client = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
serverAddress = ("192.168.1.126", 8000)  # ip del prossimo server a cui invio


while(True):
    textRecieved, address = server.recvfrom(4096)
    print(f"ricevuto {textRecieved.decode()} da {address}")
    # server.sendto(b"bellaFra",address)
    input("premere per trasmettere")
    print(textRecieved, serverAddress)
    client.sendto(textRecieved, serverAddress)

server.close()
client.close()