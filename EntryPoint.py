import convert 
import string

print(string.lowercase)
print "there are " + str(len(string.uppercase)) + " letters in the alphibet"
for i in range(0,100):
	print "conversion from " + str(i) + " is " + convert.numberToLetter(i)
print "conversion from 701 is " + convert.numberToLetter(701)
print "conversion from 702 is " + convert.numberToLetter(702)
print "conversion from 1381 is " + convert.numberToLetter(1381)
