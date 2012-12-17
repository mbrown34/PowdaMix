"""
Created on November 26, 2012

@author Matthew
"""
def purchaseStore(character, userChoice):
	if userChoice == 1:
		#print position 0,0 0,2 0,3 0,4
		from equipment import meleeList
		x=0
		choice=0
		while choice < 1 or choice > x:
			print "    ITEM NAME   \tITEM DAMAGE\tITEM PRICE"
			for item in meleeList:
				print x+1, ")", meleeList[x][0], "       \t", meleeList[x][2], "d", meleeList[x][3], "\t\t", meleeList[x][4]
				x+=1
			x+=1
			print x, ") Exit without purchasing"
			choice = input("\n>> ")
			if choice < x:
				enoughGold=character.checkGold(meleeList[choice-1][4])
				if enoughGold == True:
					character.addItem("equipment", "meleeList", meleeList[choice-1][0])
				else:
					print "\n\tSorry, but you do not have enough gold for that item."
			else:
				pass
			
	elif userChoice == 2:
		#index positions 0, 2, 3, 4, 5
		from equipment import rangedList
		x=0
		choice=0
		while choice < 1 or choice > x:
			print "    ITEM NAME   \tITEM DAMAGE\tITEM RANGE\tITEM PRICE"
			for item in rangedList:
				print x+1,")",rangedList[x][0],"     \t  ",rangedList[x][2],"d",rangedList[x][3],"  \t\t",rangedList[x][4],"\t\t",rangedList	[x][5]
				x+=1
			x+=1
			print x, ") Exit without purchasing"
			choice = input("\n>> ")
			if choice < x:
				enoughGold=character.checkGold(rangedList[choice-1][5])
				if enoughGold == True:
					character.addItem("equipment", "rangedList", rangedList[choice-1][0])
				else:
					print "\n\tSorry, but you do not have enough gold for that item."
			else:
				pass
		
	elif userChoice == 3:
		from equipment import armorList
		from equipment import shieldList
		#from equipment import gauntletList
		#from equipment import bootList
		#from equipment import helmetList
		items = 0
		while items <1 or items > 6:
			print "\n\n\t\t\tPURCHASE:\n\n\t\t1) Armor\n\t\t2) Shields\n\t\t3) Gauntlets\n\t\t4) Boots\n\t\t5) Helmets\n\t\t6) Cancel"
			items = input("\n>> ")
		listName = []
		if items == 1:
			listName [:]= armorList
			sList= "armorList"
		elif items == 2:
			listName [:]= shieldList
			sList = "shieldList"
		elif items == 3:
			listName [:]= gauntletList
			sList= "gauntletList"
			print "Gauntlets have not yet been implemented."
		elif items == 4:
			listName [:]= bootList
			sList = "bootList"
			print "Boots have not yet been implemented."
		elif items == 5:
			listName [:]= helmetList
			sList= "helmetList"
			"Helmets have not yet been implemented."
		elif items == 6:
			pass
		x=0
		choice=0
		while choice < 1 or choice > x:
			print "    ITEM NAME   \tITEM DEFENSE\tDEXTERITY PENALTY\tITEM PRICE"
			for item in listName:
				print x+1, ")", listName[x][0], "          \t", listName[x][2], "\t\t", listName[x][3], "\t\t", listName[x][4]
				x+=1
			x+=1
			print x, ") Exit without purchasing"
			choice = input("\n>> ")
			if choice < x:
				enoughGold=character.checkGold(listName[choice-1][4])
				if enoughGold == True:
					character.addItem("equipment", sList, listName[choice-1][0])
				else:
					print "\n\tSorry, but you do not have enough gold for that item."
			else:
				pass
			
	elif userChoice == 4:
		print "Accessories are coming soon...."
		
	elif userChoice == 5:
		from equipment import itemList
		x=0
		choice=0
		while choice < 1 or choice > x:
			print "    ITEM NAME  \tITEM PRICE"
			for item in itemList:
				print x+1, ")", itemList[x][0], "\t", itemList[x][4]
				x+=1
			x+=1
			print x, ") Exit without purchasing"
			choice = input("\n>> ")
			if choice < x:
				enoughGold=character.checkGold(itemList[choice-1][4])
				if enoughGold == True:
					character.addItem("equipment", "itemList", itemList[choice-1][0])
					character.changeGold("-", itemList[choice-1][4])
				else:
					print "\n\tSorry, but you do not have enough gold for that item."
			else:
				pass
		
	elif userChoice == 6:
		pass
	else:
		"\nI'm sorry, that is not a valid choice.Please try again..."

def sellStore(character, userChoice):
	if userChoice == 1:
		print "This functionality has not been added yet."
		
	elif userChoice == 2:
		print "This functionality has not been added yet."
		
	elif userChoice == 3:
		print "This functionality has not been added yet."
		
	elif userChoice == 4:
		print "This functionality has not been added yet."
		
	elif userChoice == 5:
		print "This functionality has not been added yet."
		
	elif userChoice == 6:
		pass
	else:
		"\nI'm sorry, that is not a valid choice.Please try again..."
