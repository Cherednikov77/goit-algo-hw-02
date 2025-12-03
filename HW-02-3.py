import turtle
def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in():
            t.left(angle)

def draw_koch_curve(order, size):
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()
    koch_curve(t, order, size)
    window.mainloop()
draw_koch_curve(5)