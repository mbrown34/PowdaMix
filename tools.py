'''
created on October 28, 2012


@author matthew
'''
import random
def getItem(fileName, listName, itemName):
	# Function that performs the search for the item to be added to inventory
	# takes the file name and list name the item is located in as well as the item name
	# then imports the appropriate file and list and then searches through the list to return the proper object
	imported = getattr(__import__(fileName, fromlist=[listName]), listName)
	x=0
	for item in imported:
		if itemName == imported[x][0]:
			return item
		else:
			x+=1
def roll(num, sides):
	total = 0		
	while num > 0:
		total += random.randint(1, sides)
		num -= 1
	return total
