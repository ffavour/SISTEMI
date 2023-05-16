import socket as sck


# f = avanti, b = indietro, l = sinistra, r = destra
def controlloComando(stringa):
    if stringa == "F" or stringa == "B" or stringa == "L" or stringa == "R":
        return True
    else:
        return False


def controlloValore(numero):
    if numero >= 0 and numero <= 100:
        return True
    else:
        return False


def controlloErrori(stringaRicevuta):
    mexDaInviare = ""
    # print(stringaRicevuta[1])
    if stringaRicevuta[1] != ";":
        mexDaInviare = "errore"
    else:
        listaComandoValore = stringaRicevuta.split(";")
        # print(listaComandoValore)
        comando = str(listaComandoValore[0])
        # print(comando)
        valore = int(listaComandoValore[1])
        # print(valore)
        if controlloComando(comando) == False or controlloValore(valore) == False:
            mexDaInviare = "errore"
        else:
            mexDaInviare = "OK"

    return mexDaInviare


def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    my_address = ("127.0.0.1", 8000)
    s.bind(my_address)

    s.listen()
    b = "F;a"
    # a = controlloErrori(b)
    # print(a)

    # controlloErrori("F;100")

    while True:
        conn, address = s.accept()
        comandoRicevuto = conn.recv(4096)
        print(f"{comandoRicevuto.decode()}")

        if comandoRicevuto.decode() == "EXIT":
            break

        reply = controlloErrori(comandoRicevuto.decode())
        print(comandoRicevuto.decode())
        conn.sendall(reply.encode())

    s.close()


if __name__ == "__main__":
    main()
