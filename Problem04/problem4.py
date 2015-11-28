#returns bool rindicating whether or not
#the provided number is a palindrome
def isPalindrome(numString):
	reverseNum = numString[::-1]
	if numString == reverseNum:
		return True		
	else:
		return False



def main():
	highestProduct = 0

	for i in range(100,1000):
		for j in range(100,1000):
			product = i * j
			if(isPalindrome(str(product))):
				if(product > highestProduct):
					highestProduct = product

	print "highest palindrome: " + str(highestProduct)

main()