class IPaddress():
    def __init__(self, ip_stringa): 
        self.ipNotazioneDec = ip_stringa 
        self.ipNotazioneBin 
        self.ipBinario = None
	
    def dec2bin(self):
        listaGruppi = self.toList()
        s = " "
        for gruppo in listaGruppi:
            s = s + bin(gruppo)
            temp = bin(gruppo)[2:]
            temp = "0"*(8 - len(temp)) + temp
            s =  s + temp + "."
        self.ipNotazioneBin = s[:-1]
    
    def dec2binNoPunti(self):
        listaGruppi = self.toList()
        s = " "
        for gruppo in listaGruppi:
            s = s + bin(gruppo)
            temp = bin(gruppo)[2:]
            temp = "0"*(8 - len(temp))
        self.ipNotazioneBin = s[:-1]
    
    def bin2dec():
        pass

    def ipBroadcast(self, subnetMask = "/24"): #ha definito valore default
        pass


    def toList(self):
        listaStringhe = self.ipNotazioneDec.split(".")
        return[int(gruppo) for gruppo in listaStringhe]

def main():
	indirizzoIP = IPaddress("192.168.0.123")
     
	print(indirizzoIP.ipNotazioneDec)
	print(indirizzoIP.ipNotazioneBin())



if __name__ == "__main__":
        main()