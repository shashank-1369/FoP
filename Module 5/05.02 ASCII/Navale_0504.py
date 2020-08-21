# Shashank Navale
# 08/20/2020
# Purpose: To implement OOP programming, that is classes and methods to print a description of my superhero

class Superhero:

    # Superhero class represents the facts related to a superhero.

    def __init__(self, name = "", strenthPts=0, sigAbility = "", secondaryAbility = "" ):

        # creates the superhero name and strenghtPts attributes

        self.name = name
        self.strenghtPts = strenthPts
        self.sigAbility = sigAbility
        self.secondaryAbility = secondaryAbility

    def addStrengthPts(self, points):

        # adds points to the superhero's strengths

        self.strenghtPts = self.strenghtPts + points

    def userInput(self, sigAbility, secondaryAbility):

    	# allows the user to input and control how the superhero reacts to the oppenent he/she is fighting

    	if(userIn == "Blaze"):
    		print(newSuperhero.sigAbility)

    	elif(userIn == "Hot Hands"):
    		print(newSuperhero.secondaryAbility)

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
    	print("Can you help him decide if he should use his signature ability, "+newSuperhero.sigAbility+" or his secandary ability, "+newSuperhero.secondaryAbility+"?")
    	userIn = input("Please input 'Blaze' to use his signature ability or 'Hot Hands' to use his secondary ability.")

    	# call the userInput function
    	newSuperhero.userInput()



main()





