# Shashank Navale
# 08/20/2020
# Purpose: To implement OOP programming, that is classes and methods to print a description of my superhero

class Superhero:

    # Superhero class represents the facts related to a superhero.

    def __init__(self, name="", strenthPts=0):

        # creates the superhero name and strenghtPts attributes

        self.name = name
        self.strenghtPts = strenthPts

    def addStrengthPts(self, points):

        # adds points to the superhero's strengths

        self.strenghtPts = self.strenghtPts + points
