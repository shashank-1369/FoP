# Shashank Navale
# 10/03/2020
# Purpose: The purpose of this project is to convert Pounds to Kilograms or vice versa.


def poundsToKilograms(pounds):
    conversion = pounds * 0.45359237
    return conversion

def kilogramsToPounds(kilograms):
    conversion = kilograms / 0.45359237
    return conversion

def main():
    print("Welcome to mass converter!")
    print("This program allows you to convert between the US customary pounds (lbs) to the SI unit of mass, Kilograms (Kg) and vice versa")
    # prints the welcome message
    print("First lets set the desired unit of conversion")
    userInput = input("Please enter 'kg' to convert Kilograms or enter 'lb' to convert pounds ")
    # get the userinput of conversion
    
    if(userInput == "lb"):
        print("Okay let's convert pounds to kilogramns!")
        pounds = float(input("Please enter your value in pounds (please input neumerical values only)"))
        newKilograms = poundsToKilograms(pounds)
        roundedKilograms = round(newKilograms, 1)
        print(str(pounds)+" lb in kilograms would be "+str(roundedKilograms)+" kg")

    elif(userInput == "kg"):
        print("Okay let's convert kilograms to pounds")
        kilograms = float(input("Please enter your value in kilograms (please input numerical values only)"))
        newPounds = kilogramsToPounds(kilograms)
        roundedPounds = round(newPounds, 1)
        print(str(kilograms)+" kg in pounds is equal to "+str(roundedPounds)+" lb")
    # sets the units we for conversion
   
main()
    

