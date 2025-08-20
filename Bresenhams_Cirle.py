#TASK1 - drawing 4 different cirles
from ColabTurtle.Turtle import *
import time

def put_pixel(x, y, color="red"):
    penup()
    goto(x, y)
    pencolor(color)
    pendown()
    forward(1)
    penup()

def draw_circle(xc, yc, x, y, color):
    put_pixel(xc + x, yc + y, color)
    put_pixel(xc - x, yc + y, color)
    put_pixel(xc + x, yc - y, color)
    put_pixel(xc - x, yc - y, color)
    put_pixel(xc + y, yc + x, color)
    put_pixel(xc - y, yc + x, color)
    put_pixel(xc + y, yc - x, color)
    put_pixel(xc - y, yc - x, color)

def circle_bres(xc, yc, r, color):
    initializeTurtle(initial_speed=13, initial_window_size=(800, 600))

    x = 0
    y = r
    d = 3 - 2 * r

    draw_circle(xc, yc, x, y, color)

    while y >= x:
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        x += 1
        draw_circle(xc, yc, x, y, color)
        time.sleep(0.01)


if __name__ == "__main__":
    xc, yc = 400, 300
    radii = [50, 100, 150, 200, 250]
    colors = ["red", "blue", "green", "purple", "orange"]

    for r, color in zip(radii, colors):
        circle_bres(xc, yc, r, color)


#TASK2 - drawing 3 cirles within one center
from ColabTurtle.Turtle import *
import time

def put_pixel(x, y, color="red"):
    penup()
    goto(x, y)
    pencolor(color)
    pendown()
    forward(1)
    penup()

def draw_circle(xc, yc, x, y, color):
    put_pixel(xc + x, yc + y, color)
    put_pixel(xc - x, yc + y, color)
    put_pixel(xc + x, yc - y, color)
    put_pixel(xc - x, yc - y, color)
    put_pixel(xc + y, yc + x, color)
    put_pixel(xc - y, yc + x, color)
    put_pixel(xc + y, yc - x, color)
    put_pixel(xc - y, yc - x, color)

def circle_bres(xc, yc, r, color):
    x = 0
    y = r
    d = 3 - 2 * r
    draw_circle(xc, yc, x, y, color)

    while y >= x:
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        x += 1
        draw_circle(xc, yc, x, y, color)
        time.sleep(0.005)

if __name__ == "__main__":

    initializeTurtle(initial_speed=13, initial_window_size=(800, 600))

    xc, yc = 400, 300  #center
    radius = [50, 100, 150]
    colors = ["red", "blue", "green"]

    for r, color in zip(radius, colors):
        circle_bres(xc, yc, r, color)



#task3-circles in 4 sides
from ColabTurtle.Turtle import *
import time

def put_pixel(x, y, color="red"):
    penup()
    goto(x, y)
    pencolor(color)
    pendown()
    forward(1)
    penup()

def draw_circle(xc, yc, x, y, color):
    put_pixel(xc + x, yc + y, color)
    put_pixel(xc - x, yc + y, color)
    put_pixel(xc + x, yc - y, color)
    put_pixel(xc - x, yc - y, color)
    put_pixel(xc + y, yc + x, color)
    put_pixel(xc - y, yc + x, color)
    put_pixel(xc + y, yc - x, color)
    put_pixel(xc - y, yc - x, color)

def circle_bres(xc, yc, r, color):
    x = 0
    y = r
    d = 3 - 2 * r
    draw_circle(xc, yc, x, y, color)
    while y >= x:
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        x += 1
        draw_circle(xc, yc, x, y, color)
        time.sleep(0.005)

if __name__ == "__main__":
    initializeTurtle(initial_speed=13, initial_window_size=(800, 600))
    r = 120
    width, height = 800, 600

    centers = [
        (width // 4, height // 4),       # Bottom-left quadrant
        (3 * width // 4, height // 4),   # Bottom-right quadrant
        (width // 4, 3 * height // 4),   # Top-left quadrant
        (3 * width // 4, 3 * height // 4) # Top-right quadrant
    ]

    colors = ["red", "blue", "green", "purple"]

    for (xc, yc), color in zip(centers, colors):
        circle_bres(xc, yc, r, color)
