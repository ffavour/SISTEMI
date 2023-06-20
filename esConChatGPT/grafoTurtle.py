import turtle

# Creazione della finestra di disegno
window = turtle.Screen()
window.title("Lamborghini Urus")
window.bgcolor("white")

# Creazione della tartaruga
car = turtle.Turtle()
car.color("black")
car.speed(3)

# Disegno della Lamborghini Urus
car.forward(100)  # Esempio di movimento in avanti
car.left(90)  # Esempio di svolta a sinistra
car.forward(50)  # Esempio di movimento in avanti

# Chiudere la finestra al clic
turtle.done()
