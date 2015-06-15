FILE_NAME='nums.txt'


def getProduct(index, nums):
	
	#initialize product
	product=1

	productIndex=0
	while(productIndex<13):
		product=product * int(nums[index + productIndex])
		productIndex+=1

	return product	
	

def main():
	numsFile=open(FILE_NAME)

	nums=[]

	for line in numsFile:
		for char in line:
			if(char!="\n"):
				nums.append(char)

	#nums has been constructed

	#get size of nums
	numsSize=len(nums)

	#initialize index variable 
	currentIndex=0

	#initialize index representing start of 13 consecutive digits
	highestIndex=0
	highestProduct=0

	#as long as we can access 13 consecutive digits from the array, call the get product function
	while((currentIndex+13)<numsSize):
		newProduct=getProduct(currentIndex, nums)

		if(newProduct>highestProduct):
			highestIndex=currentIndex
			highestProduct=newProduct

		currentIndex+=1


	print "The highest product of " + str(highestProduct) + " starts at index: " + str(highestIndex)
	print "The 13 consecutive numbers are:"
	i=0
	while i<13:
		print(nums[i+highestIndex])
		i+=1	
main()
