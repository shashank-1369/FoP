'''
Shashank Navale
07/11/2020
Purpose: The purpose of this code is to use the turtle Module to Draw the logo of the Formula 1, my favorite sport,
while incorporating the use of functions
'''

import turtle

def drawF(f1):
    f1.color("red")
    f1.setpos(0, 0)
    f1.begin_fill()
    f1.left(90)
    f1.forward(200)
    f1.right(90)
    f1.forward(100)
    f1.right(90)
    f1.forward(50)
    f1.right(90)
    f1.forward(50)
    f1.left(90)
    f1.forward(50)
    f1.left(90)
    f1.forward(25)
    f1.right(90)
    f1.forward(50)
    f1.right(90)
    f1.forward(25)
    f1.left(90)
    f1.forward(50)
    f1.right(90)
    f1.forward(50)
    f1.end_fill()

def draw1(f1):
    f1.color("black")
    f1.penup()
    f1.setpos(150, 0)
    f1.right(180)
    f1.pendown()
    f1.begin_fill()
    f1.left(90)
    f1.forward(200)
    f1.right(90)
    f1.forward(50)
    f1.right(90)
    f1.forward(200)
    f1.right(90)
    f1.forward(50)
    f1.end_fill()
    turtle.done()





def main():
    f1 = turtle.Turtle()
    f1.speed(5)

    drawF(f1)
    draw1(f1)
    print('Formula 1')
main()