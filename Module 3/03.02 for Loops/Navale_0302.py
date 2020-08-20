'''
Shashank Navle
07/05/2020
Purpose: The purpose of this program is to draw a Ninja Star using the Python's Turtle Graphics Module and Display the caption "Star"
'''

import turtle

def main():

    sn = turtle.Turtle()
    sn.shape("turtle")
    sn.color("aqua")
    sn.speed(1)

    for side in range(0, 5):
        sn.forward(100)
        sn.left(144)

    print("Star")

main()

