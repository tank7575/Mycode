import random
import turtle as t

def get_turn_size():
    turn_size = input("Enter turn size (wide, square, narrow): ")
    return turn_size

def get_line_length():
    choice = input("Enter line length (long, medium, short): ")
    if choice == "long":
        line_length = 250
    elif choice == "medium":
        line_length = 200
    else:
        line_length = 100
    return line_length

def get_line_width():
    choice = input("Enter line width (superthick, thick, thin): ")
    if choice == "superthick":
        line_width = 40
    elif choice == "think":
        line_width = 25
    else:
        line_width = 10
    return line_width

def inside_window():
    left_limit = (-t.window_width() / 2) + 100
    right_limit = (t.window_width() / 2) - 100
    top_limit = (t.window_height() / 2) - 100
    bottom_limit = (-t.window_height() / 2) + 100
    (x, y) = t.pos()
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    return inside

def move_turtle(line_length, turn_size):
    t.colormode(255)
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    t.pencolor(red, green, blue)
    t.pensize(random.randint(1, 40))
    t.speed("slow")
    if inside_window():
        if turn_size == "wide":
            angle = random.randint(120, 150)
        elif turn_size == "square":
            angle = random.randint(80, 90)
        else:
            angle = random.randint(20, 40)
            t.right(angle)
            t.forward(line_length)
    else:
        t.backward(line_length)

line_length = get_line_length()
line_width = get_line_width()
turn_size = get_turn_size()

t.shape('turtle')
t.fillcolor("green")
t.bgcolor("black")
t.speed("fastest")
t.pensize(line_width)

while True:
    move_turtle(line_length, turn_size)
