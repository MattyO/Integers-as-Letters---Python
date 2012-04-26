import string

ALPHEBET_LENGTH = len(string.uppercase)
NEW_SIZE_OFFSET = 1

def numberToLetter(number):
	if number < ALPHEBET_LENGTH: 
		return string.uppercase[number]

	newSize, letter = divmod(number,ALPHEBET_LENGTH)
	letter = string.uppercase[letter]
	
	return numberToLetter(newSize - NEW_SIZE_OFFSET) + letter 
