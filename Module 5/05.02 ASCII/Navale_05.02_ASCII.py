# Shashank Navale
# 08/14/2020
# Purpose: The purpose of this program is to encode and decode a secret message

def main():
	secretMessage = "I solemnly swear I am upto no good."
	encodedMessage = []

	print("The encoded message is :")

	for m in secretMessage:
		encodedMessage.append(ord(m))

	for c in encodedMessage:
		print(c)

	print("The decoded message is :")

	decodedMessage = ""

	for d in encodedMessage:
		decodedMessage = decodedMessage + chr(d)

	print(decodedMessage)


main()
