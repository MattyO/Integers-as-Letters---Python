import convert 
import string

print(string.lowercase)
print "there are " + str(len(string.uppercase)) + " letters in the alphibet"
for i in range(0,100):
	print "conversion from " + str(i) + " is " + convert.numberToLetter(i)

print "conversion from 1381 is " + convert.numberToLetter(1381)
