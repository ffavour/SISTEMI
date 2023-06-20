import threading
import serial
import pygame

BLACK = (0, 0, 0)


class PaddleMicrobit(pygame.sprite.Sprite):
    def __init__(self, porta_seriale, color, width, height):
        super().__init__()

        self.pulsante = False
        self.ser = serial.Serial(porta_seriale, 115200)
        self.lettura_pulsante = threading.Thread(target=self.leggi_pulsante)
        self.lettura_pulsante.daemon = True

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def start(self):
        self.lettura_pulsante.start()

    def leggi_pulsante(self):
        while True:
            if self.ser.readable():
                linea = self.ser.readline().decode().strip()
                if linea == 'down':
                    self.pulsante = "down"
                    self.moveDown(15)
                elif linea == 'up':
                    self.pulsante = "up"
                    self.moveUp(15)

    def ottieni_direzione(self):
        return self.pulsante

    def moveUp(self, pixels):
        self.rect.y -= pixels

        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels

        if self.rect.y > 400:
            self.rect.y = 400


"""microbit = PaddleMicrobit('COM6')  # Inserisci la porta seriale corretta del tuo microbit
microbit.start()

while True:
    direzione = microbit.ottieni_direzione()
    if direzione:
        print("Hai premuto", direzione)
        microbit.pulsante = False"""
