#Shashank Navale
#Purpose: To create a program that plays Rock Paper Scissors with the user and the computer has 100% win rate 


def main():
    print("Welcome to the RPS Bot!")
    print(" You can play Rock Paper Scissors with for as long as you want and I will not get bored unlike a human :)")

    playerInput = input("Please enter R for Rock, P for Paper and S for Scissors")
    
    x = 100


        if (playerInput == "R"):
            
            print("Your input: Rock")
            print("Computer's Input: Paper")
        if (playerInput == "P"):
            
            print("Your input: Paper")
            print("Computer's Input: Scissors")
        if (playerInput == "S"):
            
            print("Your input: Scissors")
            print("Computer's Input: Rock")
    print("You loose! Try again!")

    x = x+1

main()
