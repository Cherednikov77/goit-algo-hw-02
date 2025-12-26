import turtle
import argparse
def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in(60, -120, 60, 0):
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size):
    window = turtle.Screen()
    window.bgcolor("white")
    window.title(f"koch curve({order})")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()
    
    koch_curve(t, order, size)
    print(The end operation.Pls., closed window and exit)
    window.mainloop()
def parse_arguments():
    parser = argparse.ArgumentParser(descroption="__init__")
    parser.add_argument("--order" , type=int, default=3,help="3")
    parser.add_argument("--size", type=float, default=300.0, help=300.0)
    
    return prse_args()
if __name__ == "__main__":
    args = parse_arguments()
    draw_koch_curve(args.order, args.size)
    
