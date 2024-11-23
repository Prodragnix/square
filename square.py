import turtle
screen=turtle.Screen()
pen=turtle.Turtle()
screen.bgcolor('Yellow')
pen.pencolor('Red')
pen.fillcolor('Blue')
pen.begin_fill()
pen.pensize(20)
for _ in range (4):
    pen.forward(150)
    pen.right(90)
pen.end_fill()
screen.mainloop()