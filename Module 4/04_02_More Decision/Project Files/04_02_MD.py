# Shashank Navale
# 08/09/2020
# Purpose: The purpose of the program is to allow the user to control the movements of the turtle, using the turtle module

import turtle # imports turtle module

def square(shashank): # defines new function called square
    shashank.color("green yellow") # sets turtle color to Green Yellow
    for n in range(0, 4): # loop code 4 times
        shashank.forward(100)  # Forward turtle by 100 units
        shashank.left(90)  # Turn turtle by 90 degree
    turtle.done() # keeps the turtle window open

def rectangle(shashank): # defines new function called rectangle
    shashank.color("blue") # sets turtle color to blue
    shashank.forward(300) # forward turtle by 300 units
    shashank.left(90) # turns left by 90 degrees
    shashank.forward(200) # forward turtle by 200 units
    shashank.left(90) # turns left by 90 degrees
    shashank.forward(300) # forward turtle by 300 units
    shashank.left(90) # turns left by 90 degrees
    shashank.forward(200) # forward turtle by 200 units
    shashank.left(90) # turns left by 90 degrees
    turtle.done()

def circle(shashank): # defines new function called circle
    shashank.color("red") # sets turtle color to red
    shashank.circle(50) # circle turtle by radius of 50
    turtle.done() # keeps the turtle window open

def triangle(shashank): # defines new function called triangle
    shashank.color("green") # sets turtle color to green
    shashank.forward(100) # turtle forward by 100
    shashank.left(120) # turtle left by 120
    shashank.forward(100) # turtle forward by 100
    shashank.left(120) # turtle left by 120
    shashank.forward(100) # turtle forward by 100
    shashank.left(120) # turtle left by 120
    turtle.done()

def main(): # defines the main function
    shashank = turtle.Turtle() # names the turtle "Shashank"
    shashank.setpos(0, 0) # sets teh turtle position to 0, 0
    shashank.speed(1) # sets turtle speed to 1
    shashank.shape("turtle") # sets turtle shape to "Turtle"

    # prints the following instructions for the user
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please enter the following Input Values as desired")
    print("Input S to draw a Square")
    print("Input R to draw a Rectangle")
    print("Input C to draw a Circle")
    print("Input T to draw a Triangle")
    print("Input Q to Quit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    userInput = input("Input Value to Move Turtle (Read Instructions above)") # asks for user input with the following message
    if(userInput == "S"): # checks if the user input equals S
        square(shashank) # if yes, runs the square function
    elif(userInput == "R"): # checks if the user input equals R
        rectangle(shashank) # if yes, runs the rectangle function

    if(userInput == "C"): # checks if the user input equals C
        circle(shashank) # if yes, runs the circle function
    elif(userInput == "T"): # checks if the user input equals T
        triangle(shashank) # if yes, runs the triangle function

    if(userInput == "Q"): # checks if the user input equals Q
        turtle.bye() # if yes, quits and closes the Turtle Graphics Window

main() # ends the program









