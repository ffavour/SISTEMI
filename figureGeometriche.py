"""
triangolo, quadrato, pentagono, esagono, ettagono, ottagono, ennagono, decagono 
"""
import turtle

def quadrato():
    quadrato = turtle.Turtle()

    return quadrato

def poligono(posX, posY, nLati, cursore, colore):
    cursore.color("black")
    cursore.begin_fill()
    cursore.penup()
    cursore.setposition(posX, posY)
    cursore.pendown()

    lato = 360/nLati
    angolo = 360/nLati

    for _ in range(0, nLati):
        cursore.right(angolo)  
        cursore.forward(lato)
    cursore.color(colore)
    cursore.end_fill()

def main():
    #figure = [turtle.Turtle() for _ in range(9)] 

    #figure[0] = quadrato()

    poligono(30, 30, 5, 5, "red")
    turtle.done()


if __name__=="__main__":
		main()