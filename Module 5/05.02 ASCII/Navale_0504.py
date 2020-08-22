# Shashank Navale
# 08/20/2020
# Purpose: To implement OOP programming, that is classes and methods to print a description of my superhero

class Superhero:

    # Superhero class represents the facts related to a superhero.

    def __init__(self, name = "", strenthPts=0, sigAbility = "", secondaryAbility = "", xpLevel=99 ):

        # creates the superhero name and strenghtPts attributes

        self.name = name
        self.strenghtPts = strenthPts
        self.sigAbility = sigAbility
        self.secondaryAbility = secondaryAbility
        self.xpLevel = xpLevel

    def addStrengthPts(self, points):

        # adds points to the superhero's strengths

        self.strenghtPts = self.strenghtPts + points

    def addXpLevel(self, xp):

    	# adds experience levels to the superhero

    	self.xpLevel = self.xpLevel + xp

def main():

		# create new superhero called Phoenix and utilize its attributes

    	newSuperhero = Superhero("Phoenix", 0, "Blaze", "Hot Hands")
    	print("Let me tell you about my superhero :")
    	print("His name is "+newSuperhero.name+" and his signature ability is "+newSuperhero.sigAbility+".")
    	print("He also has a secondary ability called "+newSuperhero.secondaryAbility+".")

    	# create the villain called Omen and utilize his attributes

    	newVillain = Superhero("Omen", 0, "Teleport", "Paranoya")
    	print("Oh No! Looks like "+newSuperhero.name+" is facing his rival villain "+newVillain.name+"!")
    	print(newVillain.name+"'s signature ability is that he can "+newVillain.sigAbility+"!")
    	print(newVillain.name+" also has a secondary ability called "+newVillain.secondaryAbility+".")
    	print("Looks like Omen has sent a "+newVillain.secondaryAbility+ " towards "+newSuperhero.name+" to disrupt his senses.")
    	print("It is crucial that "+newSuperhero.name+" makes the right decision!")
    	print(newSuperhero.name+" shoots his "+newSuperhero.sigAbility+" towards "+newVillain.name+" and does damage worth 100 HP! ")
    	print("Phoenix has done it again")  
    	print("Phoenix has been awarded :")	

    	# calls the addStrengthPts function and adds 100 points

    	newSuperhero.addStrengthPts(100)

    	# prints the number of strength points after the addition of the duel

    	print(str(newSuperhero.strenghtPts)+" Strength Points")

    	print("Phoenix has also been promoted to the")

    	# calls the xpLevel function and adds 1 xp level to it

    	newSuperhero.addXpLevel(1)

    	print(str(newSuperhero.xpLevel)+"th Experience Level")

    	# prints the final line of the program

    	print("This makes Phoenix the most experienced and strongest superhero!")


main()





