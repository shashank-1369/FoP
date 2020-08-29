# Shashank Navale
# 08/23/2020
# Purpose: The purpose of this program is to allow interested memebers to apply to the Python Programming club!

def main():

	# display intro message
	print("Welcome to Python Programmers Club, of Middleton High School and Thank You for showing your interest in our club!")
	print("Please enter your information as part of our Application Process!")

	# receive input from the user
	userName = input("Please enter your Full Name ")
	userAge = int(input("Please enter you age "))
	studentConfirmation = input("Please confirm that you are a Middleton High School student by entering 'Y' ")
	participationConfirmation = input("Please confirm that you will actively participate and follow the Standard Code of Conduct while interacting with the Club and its memebers by entering 'Y' ")

	# print User Responses
	print("Your Application Responses are :")
	print("Full Name: "+userName)
	print("Age: "+str(userAge))
	print("Student Confirmation: "+studentConfirmation)
	print("Particpation Confirmation: "+participationConfirmation)

	# check if user is eligibile to apply
	
	if (userAge >= 14 and studentConfirmation == "Y" and participationConfirmation == "Y"):
		print("Your Application has been accepted!")

	else:
		print("Sorry, you must be over 14 years of age and must confirm with 'Y' to our student and participation requirements for your application to be accepted")


main()

