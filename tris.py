import math
import random

class Tris():
    def __init__(self):
         self.scacchiera = [' ' for _ in range(9)]  #lista con posizioni tris
         self.VicitoreCorrente = None #controlla chi sta vincendo
    
    def stampaScacchiera(self):
        #restituisce le righe?
      for riga in [self.scacchiera[i * 3: (i + 1) * 3] for i in range(3)]:
         print('|' + '|' .join(riga) + '|')
    
    @staticmethod
    def stampaNumScacchiera():
       #stampa posizioni nella scacchiera
       numScacchiera = [[str(i) for i in range(j * 3, (j + 1) * 3) ]for j in range(3)]
       for  riga in numScacchiera:
        print('|' + '|' .join(riga) + '|')    
    
    def mosseDisponibili(self):
        mosse = []
        for (i, posPedina) in enumerate(self.scacchiera):
            if posPedina == ' ' : #controlla se lo spazio è libero
                mosse.append(i)
        
        return mosse


class Giocatore():
    def __init__(self, pedina):  #pedina puo essere X o O
         self.pedina = pedina

    def mossa(self, gioco):
        pass

class GiocatorePC(Giocatore):
    def __init__(self, pedina):
         super().__init__(pedina)
    
    def mossa(self, gioco):
        #cerca se puo posizionare la pedina nella spazio
         spazio = random.choice(gioco.mosseDisponibili())
         return spazio

class GiocatoreUmano(Giocatore):
    def __init__(self, pedina):
         super().__init__(pedina)

    def mossa(self, gioco):
         spazioDisponibile = False
         val = None
         while not spazioDisponibile:
            spazio = input(self.pedina + "inserire mossa tra 0 e 9")
            try:
                val = int (spazio)
                if val not in gioco.mosseDisponibili():
                    raise ValueError
                spazioDisponibile = True
            except ValueError:
                print("spazio non disponibile, riprova")
         return val

        


def main():
    a = Tris()
    a.stampaScacchiera()
    

if __name__ == "__main__":
        main()