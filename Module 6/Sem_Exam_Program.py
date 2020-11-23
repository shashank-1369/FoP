#Shashank Navale
'''Purpose: The purpose of this program is to allow users to order their desing of shirts, while getting to pick 3 charactersitics, 
and display a summary. Please note, enter inputs within 5 seconds, due to the sleep command.
'''
def main():
    import time
    #prints welcome/introductory message
    print("welcome to the T-shirt Creator!")
    print("Here you can design your own shirt by choosing your size, color and design to fit your needs!")
    time.sleep(2)
    #end of introductions

    #takes in user inputs for each characteristic and stores it in their respective variables
    shirtSize = input("Please enter your shirt size: Small, Medium, large or Extra-Large")
    time.sleep(5)
    shirtColor = input("Please enter your shirt color: Blue, Green, Red, or Yellow")
    time.sleep(5)
    shirtDesign = input("Please enter your shirt design: Cheveron, Solid, or Stripes")
    time.sleep(5)
    #end of user input

    #prints the summary of the order
    print("Order summary")
    print("Shirt Size: "+shirtSize)
    print("shirt Color: "+shirtColor)
    print("shirt Design: "+shirtDesign)
    #end of order summary

main()