import socket as sck


def isNumeroPrimo(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def trovaFattori(numero):
    listaFattori = []
    for i in range(numero):
        if isNumeroPrimo(i) and numero % i == 0:
            listaFattori.append(i)
    return listaFattori


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    server_address = ("127.0.0.1", 8000)
    s.connect(server_address)

    # listaFattoriPrimiP = trovaFattori(28367584537)
    # print(listaFattoriPrimiP)

    while True:
        numero = s.recv(4096)
        print(f"numero ricevuto: {numero.decode()}")

        # è solo di feedback
        s.sendall(b"OK")

        numero_int = int(numero.decode())
        listaFattoriPrimi = trovaFattori(numero_int)

        print(listaFattoriPrimi)
        listaFattoriPrimi_str = str(listaFattoriPrimi)
        print(listaFattoriPrimi_str)
        mex = "i fattori trovati sono: " + listaFattoriPrimi_str
        print(mex)

        s.sendall(mex.encode())

    s.close()


if __name__ == "__main__":
    main()
