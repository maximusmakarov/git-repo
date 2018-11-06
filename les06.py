# coding: utf-8

import turtle
import random
import math

phi = 360 / 7
radius_circle = 50
phi_rad: float
i: int
answer = ''
start = 0


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_circle(radius_circle, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius_circle)
    turtle.end_fill()


turtle.speed(0)


def draw_pistol(base_x, base_y):
    #рисование основного круга
    gotoxy(base_x, base_y)
    turtle.circle(80)
    #мушка
    gotoxy(base_x, base_y + 160)
    draw_circle(5, 'red')

    #барабан
    for i in range(0, 7):
        phi_rad = phi * i * math.pi / 180
        gotoxy(base_x + math.sin(phi_rad) * radius_circle, base_y + math.cos(phi_rad) * radius_circle + 58)
        draw_circle(21, 'white')


def rotate_pistol(base_x, base_y, start):
   for i in range(start, random.randrange(7, 100)):
       phi_rad = phi * i * math.pi / 180
       gotoxy(base_x + math.sin(phi_rad) * radius_circle, base_y + math.cos(phi_rad) * radius_circle + 58)
       draw_circle(21, 'brown')
       draw_circle(21, 'white')

   gotoxy(base_x + math.sin(phi_rad) * radius_circle, base_x + math.cos(phi_rad) * radius_circle + 58)
   draw_circle(21, 'brown')

   return i % 7

draw_pistol(100, 100)

while answer != 'N':
    answer = turtle.textinput("Играть?", "Y/N")
    if answer == 'Y':
        start = rotate_pistol(100, 100, start)
        if start == 0:
            gotoxy(-150, 250)
            turtle.write("Вы проиграли!", font=("Arial", 18, "normal"))

    else:
        pass
