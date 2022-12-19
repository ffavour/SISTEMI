import turtle

finestra = turtle.Screen()  #sono istanze di un oggetto (turtle)
alice = turtle.Turtle()
bob = turtle.Turtle()

alice.color("red")
alice.forward(100)
alice.right(60)
alice.forward(100)

bob.penup()
bob.setposition(-50, 50)
bob.pendown()
bob.right(90)
bob.backward(80)

tartarughe = [turtle.Turtle() for _ in range(9)]  #crea 9 tartarughe salvate in una lista

tartarughe = [turtle.Turtle()] * 9 #crea 9 bob

turtle.done()
