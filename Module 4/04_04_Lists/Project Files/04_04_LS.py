# Shashank Navale
# 08/09/2020
# Purpose: They prupose of this program is to let users know my Top 5 car makers I like and also tell them if we have any in common

def main():

    # creates a list with my top 5 car makers in an order
    myCarList = ["Tesla", "Mercedes Benz", "Audi", "Lexus", "Honda"]
    # assigns the length of myCarList to the variable "length"
    length = len(myCarList)

    # prints "My top 5 Car Makers are:"
    print("My Top "+str(length)+" Car Makers are:")
    # starts a for loop upto the value of the variable "length" or aka the length of myCarList
    for x in range(0, length):
        # traverses through the list to print them in an order
        print(str(x+1)+". "+myCarList[x])
    print("")  # prints a blank line for better viewing

    userCarList = []  # creates an empty list called "userCarList"

    # starts a for loop upto the value of the variable "length" or aka the lenght of the userCarList
    for n in range(0, length):
        # Asks for 5 inputs of the user's Top 5 Car Makers
        userInput = input("Enter your Top "+str(n+1)+" Car Maker ")
        # appends the user input into the userCarList
        userCarList.append(userInput)

    print("")  # prints a blank line for better viewing
    print("Your Top 5 Car Makers are:")  # prints "Your Top 5 Car Makers are:"

    # starts a for loop upto the value of the variable "legnth" or aka the length of userCarList
    for y in range(0, length):
        # prints the user's Top 5 list in an order
        print(str(y+1)+". "+userCarList[y])

    myCarSet = set(myCarList)  # converts myCarList into a set
    # looks for common elements between myCarList and userCarList ans stores it in commonCarMakers
    commonCarMakers = myCarSet.intersection(userCarList)

    print("")  # prints a blank line for better viewing
    # prints "We have these Car Makers in common!"
    print(" We have these Car Makers in common!")
    # prints the variable "commonCarMakers" aka elements common in myCarList and userCarList
    print(commonCarMakers)


main()
