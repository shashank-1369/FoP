'''
Shashank Navale
06/30/2020
The purpose of this program is to calculate the answer to the give word problem based on user inputs.
'''

from math import *


def main():
    print("Tim is at a make-a-rubik's cube workshop. He can customize the volume and surface area of the cube.")
    print("He needs your help by providing him the volume and surface area of the cube")
    
    sideLength = int(input("Please enter a suitable integer for the side length of Tim's cube!"))
    
    volume = float(pow(sideLength, 3))
    surfaceArea = float(6 * (pow(sideLength, 2)))
    
    print("According to your entered value, the volume of the cube will be " +str(volume)+ " and the surface area will be " +str(surfaceArea)+ ".")
    
main()