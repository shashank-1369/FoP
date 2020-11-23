#Shashank Navale
#Purpose: To create a program that plays Rock Paper Scissors with the user and the computer has 100% win rate 


def main():
    import time
    import datetime
    print("Welcome to the RPS Bot!")
    print(" You can play Rock Paper Scissors with for as long as you want and I will not get bored unlike a human :)")

    playerInput = input("Please enter R for Rock, P for Paper and S for Scissors")
    
    localTime = time.time()


    if (playerInput == "R"):
            
            print("Your input: Rock")
            time.sleep(1)
            print("Computer's Input: Paper")
    if (playerInput == "P"):
            
            print("Your input: Paper")
            time.sleep(1)
            print("Computer's Input: Scissors")
    if (playerInput == "S"):
            
            print("Your input: Scissors")
            time.sleep(1)
            print("Computer's Input: Rock")
    time.sleep(2)
    print("You loose! Try again!")
    convertedTime = datetime.datetime.fromtimestamp(localTime).strftime('%c')
    print("Timestamp: ", convertedTime)

main()
