# This is a simple snake game for Selenium testing

import random
import time
import turtle # pip install turtle
#The turtle module provides turtle graphics primitives, in both object-oriented and procedure-oriented ways.

#create screen using turtle
screen = turtle.Screen()
screen.title('SNAKE GAME')
screen.setup(width = 700, height = 700)
screen.tracer(0)
turtle.bgcolor('green')

#creating a border inside the frame for the game to live
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

