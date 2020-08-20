'''
Shashank Navale
07/20/2020
Purpose: To calculate the Subtotal and Order Total that is including Tax and Shipping of the items in my wish list.
'''
def main():
#program inputs
    print("Welcome to your Wish List Calculator")
    f1 = float(input("Please enter the Price of F1 2020 Xbox Game $")) #asks for user input for the price
    appleWatch = float(input("Please enter the Price of Apple Watch Series 3 $")) #asks for user input for the price
    gamingHeadset = float(input("Please enter the Price of the Logitech Gaming Headset $")) #asks for user input for the price

#variable assignment
    subTotal = f1 + appleWatch + gamingHeadset # sums all prices
    tax = subTotal * 0.065 #calcualtes the tax based on subTotal
    orderTotal = subTotal + tax + 5.99
    orderTotal1 = "{:.2f}".format(orderTotal)

#Order Reciept
    print("Your Wishlist:")
    print("")
    print("Items                     Cost")
    print("F1 2020 Xbox One          $"+str(f1))
    print("Apple Watch Series 3      $"+str(appleWatch))
    print("Logitech Gaming Headset   $"+str(gamingHeadset))
    print("----------------------------------")
    print("Subtotal:                 $"+str(subTotal))
    print("Tax:                      $"+str(tax))
    print("Shipping:                 $5.99")
    print("Order Total:              $"+str(orderTotal1))
main()
