class Giocatore():
    def __init__(self, pedina):
         self.pedina = pedina
         self.posizione = None
         self.posOccupate = []

    def toString(self):
        s = ("pedina: " + self.pedina + "\nposizione: " + str(self.posizione))
        return s
    
    def isOccupato(self, pos):
        occupato = False

        for posizioni in self.posOccupate:
            if(pos == posizioni):
                occupato = True
        return occupato


    def posizionaPedina(self, posizione):
        if int(posizione) > 0 and int(posizione) < 10:
            self.posizione = posizione
            self.posOccupate.append(posizione)
    
    def stampaPosOccupate(self):
        for elementi in self.posOccupate:
            print(elementi)

    

def main():
    a = Giocatore("X")
    b = Giocatore("O")

    #while True:
    posizioneA = input("inserire la pedina A in una delle posizioini (1-9):")
    posizioneB = input("inserire la pedina B in una delle posizioini (1-9):")

    while True:
            if a.isOccupato(posizioneB) == False and b.isOccupato(posizioneB) == False and a.isOccupato(posizioneA) == False and b.isOccupato(posizioneA) == False:
                a.posizionaPedina(posizioneA)
                b.posizionaPedina(posizioneB)
                break

        #if(posizioneA == 0 or posizioneB == 0):
        #    break

    
    print(a.toString())
    print(b.toString())
    a.stampaPosOccupate()
    b.stampaPosOccupate()

    

    

if __name__ == "__main__":
        main()