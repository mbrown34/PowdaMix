"""
Created on November 11, 2012


@author Matthew
"""
import tools
import spells
#import skills
import equipment
#import items
class Player:
	def __init__(self, load):
		self.name='None'
		self.race='None'
		self.job='None'
		self.stats={"STR": 0,"DEX": 0,"CON": 0,"INT": 0,"WIS": 0,"CHA": 0}
		self.statusEffects=[]
		self.currentHP=0
		self.maxHP=0
		self.currentMP=0
		self.maxMP=0
		self.equipped={'HEAD': ' ', 'BODY': ' ', 'R-HAND': ' ', 'L-HAND': ' ', 'ARMS': ' ', 'FEET': ' ', 'ACC': ' ', 'R-RING': ' ', 'L-RING': ' '}
		self.equipment=[]
		#self.currentLoad= 0
		#self.maxCarry=0
		self.items=[]
		self.spells=[]
		self.skills=[]
		self.gold=0
		#functions that will run to populate an initial character object's variables
		#this should allow each character object to be different from the last one created
		if load == False:
			self.newChar()
		else:
			self.loadChar()
	def __str__(self):
		return "Character"
	def __repr__(self):
		return "Character"
######################################           INITIAL CHARACTER CREATION FUNCTIONS                ######################################
	def newChar(self):
		self.addName()
		self.addRace()
		self.setVals()
		self.raceBonus()
		self.setHP()
		self.setMP()
		self.setGold()
		self.displayInfo()
		self.addJob()
		self.initialInv()
		#self.setMaxCarry()
		#self.initialSpells()
		#self.initialSkills()
	def loadChar(self):
		#  This function will load a character's information into a new character object.
		pass
	def addName(self):
		print "\nWhat will the character's name be?\n"
		self.name=raw_input(">> ")	
	
	def addRace(self):
		choice = 0
		while choice < 1 or choice > 5:
			print "\nWhat is the new character's race?\n\n\t1) Human   2) Elven   3) Half-Elven   4) Dwarven   5) Halfling\n"
			choice = input(">> ")
			if choice == 1:
				self.race='Human'
			elif choice == 2:
				self.race='Elven'
			elif choice == 3:
				self.race='Half-Elven'
			elif choice == 4:
				self.race='Dwarven'
			elif choice == 5:
				self.race='Halfling'
			else:
				print "\nThat is not a valid option. Please try again..."

	def addJob(self):
		choice=0
		while choice < 1 or choice > 6:
			print "\nWhat will the new character's class be?\n\n\t1) Fighter   2) Mage   3) Thief   4) Ranger  5) Cleric  6) Monk\n"
			choice = input(">> ")
			if choice ==1:
				self.job='Fighter'
			elif choice ==2:
				self.job='Mage'
			elif choice ==3:
				self.job='Thief'
			elif choice ==4:
				self.job='Ranger'
			elif choice ==5:
				self.job='Cleric'
			elif choice == 6:
				self.job='Monk'
			else:
				print "\nThat is not a valid option. Please try again..."
	
	def setHP(self):
		if self.stats['CON'] >18:
			dice=16
		elif self.stats['CON'] >16:
			dice=15
		elif self.stats['CON'] >14:
			dice=14
		elif self.stats['CON'] >12:
			dice=13
		elif self.stats['CON'] >10:
			dice=12
		elif self.stats['CON'] >8:
			dice=11
		elif self.stats['CON'] >6:
			dice=10
		elif self.stats['CON'] >4:
			dice=9
		elif self.stats['CON'] >2:
			dice=8
		self.maxHP=tools.roll(dice,6)
		self.currentHP=self.maxHP
	
	def setMP(self):
		if self.stats['WIS'] >18:
			dice=14
		elif self.stats['WIS'] >16:
			dice=13
		elif self.stats['WIS'] >14:
			dice=12
		elif self.stats['WIS'] >12:
			dice=11
		elif self.stats['WIS'] >10:
			dice=10
		elif self.stats['WIS'] >8:
			dice=9
		elif self.stats['WIS'] >6:
			dice=8
		elif self.stats['WIS'] >4:
			dice=7
		elif self.stats['WIS'] >1:
			dice=6
		self.maxMP=tools.roll(dice,6)
		self.currentMP=self.maxMP
	
	def setGold(self):
		self.gold=tools.roll(100,5)
	
	def setVals(self):
		self.stats['STR'] = tools.roll(3,6)
		self.stats['DEX'] = tools.roll(3,6)
		self.stats['CON'] = tools.roll(3,6)
		self.stats['INT'] = tools.roll(3,6)
		self.stats['WIS'] = tools.roll(3,6)
		self.stats['CHA'] = tools.roll(3,6)
		print "\nYour current stat rolls are:\n"
		print "\tSTR:", self.stats['STR'], "\tDEX:", self.stats['DEX'], "\tCON:", self.stats['CON']
		print "\tINT:", self.stats['INT'], "\tWIS:", self.stats['WIS'], "\tCHA:", self.stats['CHA']
		extraPoints=tools.roll(4,6)
	        while extraPoints > 0 or choice < 1 or choice > 6:
			print "\nYou have", extraPoints,"to spend on increasing stats."
			print "Which stat would you like to increase? (You cannot increase higher than 18)\n"
			print "\n\t1) STR:",self.stats['STR'],"\t2) DEX:",self.stats['DEX'],"\t3) CON:",self.stats['CON']
			print "\t4) INT:",self.stats['INT'],"\t5) WIS:",self.stats['WIS'],"\t6) CHA:",self.stats['CHA'],"\n"
			choice = input("\n>> ")
			if choice == 1:
				if self.stats['STR'] < 18:
					self.stats['STR'] +=1
					extraPoints-=1
				else:
					print "That stat is maxed out..."
			elif choice ==2:
				if self.stats['DEX'] < 18:
					self.stats['DEX'] +=1
					extraPoints-=1
				else:
					print "That stat is maxed out..."
			elif choice ==3:
				if self.stats['CON'] < 18:
					self.stats['CON'] +=1
					extraPoints-=1
				else:
					print "That stat is maxed out..."
			elif choice ==4:
				if self.stats['INT'] < 18:
					self.stats['INT'] +=1
					extraPoints-=1
				else:
					print "That stat is maxed out..."
			elif choice ==5:
				if self.stats['WIS'] < 18:
					self.stats['WIS'] +=1
					extraPoints-=1
				else:
					print "That stat is maxed out..."
			elif choice ==6:
				if self.stats['CHA'] < 18:
					self.stats['CHA'] +=1
					extraPoints-=1
				else:
					print "That stat is maxed out..."			
			else:
				print"\nI am sorry, that is not a valid choice.  Please try again..."
	def raceBonus(self):
		#statVals[0]=STR [1]=DEX [2]=CON [3]=INT [4]=WIS [5]=CHA
		#Human Elven Half-Elven Dwarven Halfling
		if self.race == 'Elven':
			self.stats['DEX'] +=2
			self.stats['CON'] -=1
			self.stats['INT'] +=1
		elif self.race == 'Half-Elven':
			self.stats['DEX'] +=2
			self.stats['CON'] -=1
		elif self.race == 'Dwarven':
			self.stats['STR']+=2
			self.stats['CON'] +=3
			self.stats['INT'] -=2
			self.stats['CHA'] -=2
		elif self.race == 'Halfling':
			self.stats['DEX'] +=3
			self.stats['CON'] -=1
			self.stats['INT'] +=1
			self.stats['CHA'] -=2
	def initialInv(self):
		if self.job=='Fighter':
			self.addItem("equipment","rangedList","Short Bow")
			self.addItem("equipment","meleeList","Long Sword")
			self.addItem("equipment", "shieldList","Medium Shield")
			self.addItem("equipment","armorList", "Studded Armor")
			self.equip('R-HAND', self.equipment[1])
			self.equip('L-HAND', self.equipment[1])
			self.equip('BODY', self.equipment[1])
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Medium Potion")
		elif self.job=='Mage':
			self.addItem("equipment", "meleeList","Staff")
			self.addItem("equipment", "armorList","Mage's Robes")
			self.addItem("equipment","meleeList", "Dagger")
			self.equip('R-HAND', self.equipment[0])
			self.equip('BODY', self.equipment[0])
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Small Mana Potion")
			self.addItem("equipment","itemList", "Large Mana Potion")
			self.addItem("equipment","itemList", "Large Mana Potion")
			self.addItem("spells", "spellList", "Magic Darts")
			self.addItem("spells", "spellList", "Fire")
			self.addItem("spells", "spellList", "Ice")
		elif self.job=='Thief':
			self.addItem("equipment", "meleeList","Dagger")
			self.addItem("equipment", "rangedList","Short Bow")
			self.addItem("equipment", "armorList","Leather Armor")
			self.addItem("equipment","meleeList", "Short Sword")
			self.equip('BODY', self.equipment[2])
			self.equip('R-HAND', self.equipment[2])
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Medium Potion")
		elif self.job=='Ranger':
			self.addItem("equipment", "meleeList","Long Sword")
			self.addItem("equipment", "rangedList","Long Bow")
			self.addItem("equipment", "armorList","Studded Armor")
			self.equip('R-HAND', self.equipment[1])
			self.equip('BODY', self.equipment[1])
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Medium Potion")
			self.addItem("equipment","itemList", "Medium Potion")
		elif self.job=='Cleric':
			self.addItem("equipment", "meleeList","Mace")
			self.addItem("equipment", "shieldList","Small Shield")
			self.addItem("equipment", "armorList","Scale Armor")
			self.equip('R-HAND', self.equipment[0])
			self.equip('L-HAND', self.equipment[0])
			self.equip('BODY', self.equipment[0])
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Medium Potion")
			self.addItem("equipment","itemList", "Small Mana Potion")
		elif self.job=='Monk':
			self.addItem("equipment", "armorList","Monk's Garb")
			self.equip('BODY', self.equipment[0])
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Medium Potion")
			self.addItem("equipment","itemList", "Medium Potion")
	def initialSpells(self):
		print
	def initialSkills(self):
		print
##########################################            CHARACTER DATA DISPLAY FUNCTIONS      ########################################	
	def displayInventory(self):
		loopEnter = 0
		for item in self.equipment:
			if loopEnter<1:
				print "\t\t\tEQUIPPABLE ITEMS IN INVENTORY:"
				loopEnter+=1
			print "", item.name, "\t"
		print "\nYou have no additional equippable items in inventory.\n"
	def displayEquipped(self):
		if self.equipped['ARMS'] == ' ':
			arms = self.equipped['ARMS']
		else:
			gaunt = self.equipped['ARMS']
			arms = gaunt.name
		if self.equipped['HEAD'] == ' ':
			head =self.equipped['HEAD']
		else:
			helm = self.equipped['HEAD']
			head = helm.name
		if self.equipped['ACC'] == ' ':
			accessory =self.equipped['ACC']
		else:
			neck = self.equipped['ACC']
			accessory = neck.name
		if self.equipped['BODY'] == ' ':
			armor=self.equipped['BODY']
		else:
			body = self.equipped['BODY']
			armor=body.name
		if self.equipped['R-HAND'] == ' ':
			rightHand=self.equipped['R-HAND']
		else:
			rHand = self.equipped['R-HAND']
			rightHand=rHand.name
		if self.equipped['L-HAND'] == ' ':
			leftHand=self.equipped['L-HAND']
		else:
			lHand = self.equipped['L-HAND']
			leftHand= lHand.name
		if self.equipped['FEET'] == ' ':
			boots=self.equipped['FEET']
		else:
			feet = self.equipped['FEET']
			boots=feet.name
		if self.equipped['R-RING'] == ' ':
			rRing=self.equipped['R-RING']
		else:
			rightRing = self.equipped['R-RING']
			rRing=rightRing.name
		if self.equipped['L-RING'] == ' ':
			lRing=self.equipped['L-RING']
		else:
			leftRing = self.equipped['L-RING']
			lRing=leftRing.name
		print "\t\t\tEQUIPPED ITEMS:\n"
		print "  ARMS [", arms , "]       HEAD  [", head, "]       ACCESSORY [", accessory, "]"
		print "                     ARMOR [", armor, "]  "
		print "  RIGHT HAND [",rightHand , "]   BOOTS [", boots, "]      LEFT HAND  [", leftHand, "]"
		print "         RIGHT RING [", rRing, "]           LEFT RING [", lRing, "]" 
		
	def displayItems(self):		
		print "\t\t\tITEMS:"
		for item in self.items:
			print item.name, "\t"
	def displaySpells(self):
		spells = 0
		for x in self.spells:
			if x.type == "spell":
				spells+=1
			else:
				pass
		if spells > 0:
			print "\t\t\tKNOWN SPELLS:"
			for spell in self.spells:
				spell.name
		else:
			print "\nYou do not know any spells."

	def displayInfo(self):
		print"\n\tYour Name:", self.name,"\n\tYour Race:", self.race,"\n\tYour Class:", self.job, ""
		print"\tHP:", self.currentHP, "/", self.maxHP, "\t\tMP:", self.currentMP, "/", self.maxMP, " "
		print"\n\tYour stats are:"
		print "\tSTR:", self.stats['STR'], "\tDEX:", self.stats['DEX'], "\tCON:", self.stats['CON']
		print "\tINT:", self.stats['INT'], "\tWIS:", self.stats['WIS'], "\tCHA:", self.stats['CHA']
		print"\n\tGold:", self.gold
		print "\tCurrent Status: " 
		if len(self.statusEffects) > 0:
			for stat in self.statusEffects:
				print "\t", stat, ", "
		else:
			print "\t    Normal"			
			
###############################################  BEGINNING OF CHARACTER DATA MANAGEMENT FUNCTIONS    #########################################	
	def save(self):
		print
###############################################  CHARACTER HP/MP/STATUS MANAGEMENT FUNCTIONS      ######################################################
	def changeHP(self, damage, amount):
		if damage == "+":
			self.currentHP += amount
		elif damage == "-":
			self.currentHP -= amount
	def changeMP(self, damage, amount):
		if damage == "+":
			self.currentMP += amount
		elif damage == "-":
			self.currentMP -= amount
	def changeStatus(self, damage, status):
		newStats = []
		if damage == "+":
			for stat in self.statusEffects:
				if stat == "Normal":
					self.statusEffects.remove("Normal")
			self.statusEffects.append(status)
			newStats = list(set(self.statusEffects))
		elif damage == "-":
			for stat in self.statusEffects:
				if stat == status:
					self.statusEffects.remove(status)
			newStats = list(set(self.statusEffects))
		self.statusEffects=newStats

######################################           CHARACTER ITEM MANAGEMENT FUNCTIONS       ############################################
	def addItem(self, fileName, listName, itemName):
		# Function for adding an item to the player's inventory
		# Takes the file name and list name that the item is located in as well as the item name and finds that item
		# Then creates the appropriate item object and appends it to the appropriate player inventory slot
		if listName == "meleeList":
			theItem=equipment.Weapon(tools.getItem(fileName, listName, itemName))
			self.equipment.append(theItem)
		elif listName=="rangedList":
			theItem=equipment.Ranged(tools.getItem(fileName, listName, itemName))
			self.equipment.append(theItem)
		elif listName=="armorList":      
			theItem=equipment.Armor(tools.getItem(fileName, listName, itemName))
			self.equipment.append(theItem)
		elif listName=="shieldList":
			theItem=equipment.Shield(tools.getItem(fileName, listName, itemName))
			self.equipment.append(theItem)
		elif listName=="gauntletList":
			theItem=equipment.Gauntlet(tools.getItem(fileName, listName, itemName))
			self.equipment.append(theItem)
		elif listName=="bootList":
			theItem=equipment.Boots(tools.getItem(fileName, listName, itemName))
			self.equipment.append(theItem)
		elif listName=="helmetList":
			item=equipment.Helmet(tools.getItem(fileName, listName, itemName))
			self.equipment.append(item)
		elif listName=="necklaceList":
			item=equipment.Necklace(tools.getItem(fileName, listName, itemName))
			self.equipment.append(item)
		elif listName=="ringList":
			item=equipment.Ring(tools.getItem(fileName, listName, itemName))
			self.equipment.append(item)
		elif listName=="itemList":       
			item=equipment.Item(tools.getItem(fileName, listName, itemName))
			self.items.append(item)
		elif listName=="spellList":
			item=spells.Spell(tools.getItem(fileName, listName, itemName))
			self.spells.append(item)
		elif listName=="skillList":
			item=skills.Skill(tools.getItem(fileName, listName, itemName))
			self.skills.append(item)
	def removeItem(self, item):
		#  Function to remove an item from inventory in the case it is destroyed or stolen
		if item.typeItem == "item":
			self.items.remove(item)
		elif item.typeItem == "spell":
			self.spells.remove(item)
		elif item.typeItem == "skill":
			self.skills.remove(item)
		else:
			self.equipment.remove(item)
	def checkItem(self, slot):
		if slot == ' ':
			item = 'empty'
		elif slot != ' ':
			item = slot.type
		return item
	def manageInventory(self):
		self.displayEquipped()
		choice =0
		while choice < 1 or choice > 10:
			print "\nEquip to which slot?"
			print "\t1) Head 2) Body 3) Arms 4) Right Hand 5) Left Hand"
			print "\t6) Boots 7) Accessory 8) Right Ring 9) Left Ring 10) Exit"
			choice = input("\n>> ")
		if choice == 1:
			helmets = []
			helmetNum=0
			choice = 0
			for item in self.equipment:
				if item.type == "helmet":
					helmetNum +=1
					helmets.append(item)
			if helmetNum > 0:
				while choice < 1 or choice > helmetNum:
					for index, item in enumerate(helmets):
						print index+1, ")", item.name
					choice = input("\n>> ")
				theItem= helmets[choice-1]
				if self.equipped['HEAD'] != ' ':
					self.equipment.append(self.equipped['HEAD'])
				self.equip('HEAD', theItem)			
			elif helmetNum == 0:
				print "You do not have any helmets to equip."
		elif choice == 2:
			armor = []
			armorNum=0
			choice = 0
			for item in self.equipment:
				if item.type == "armor":
					armorNum +=1
					armor.append(item)
			if armorNum > 0:
				while choice < 1 or choice > armorNum:
					for index, item in enumerate(armor):
						print index+1, ")", item.name
					choice = input("\n>> ")
				theItem=armor[choice-1]
				if self.equipped['BODY'] != ' ':
					self.equipment.append(self.equipped['BODY'])
				self.equip('BODY', theItem)		
			elif armorNum == 0:
				print "You do not have any armor to equip."
		elif choice == 3:
			gauntlets = []
			gauntNum=0
			choice = 0
			for item in self.equipment:
				if item.type == "gauntlets":
					gauntNum +=1
					gauntlets.append(item)
			if gauntNum > 0:
				while choice < 1 or choice > gauntNum:
					for index, item in enumerate(gauntlets):
						print index+1, ")", item.name
					choice = input("\n>> ")
				theItem= gauntlets[choice-1]
				if self.equipped['ARMS'] != ' ':
					self.equipment.append(self.equipped['ARMS'])
				self.equip('ARMS', theItem)	
			elif gauntNum == 0:
				print "You do not have any gauntlets to equip."
		elif choice == 4:
			items=[]
			meleeNum=0
			rangedNum=0
			shieldNum=0
			choice = 0
			right = self.equipped['R-HAND']
			left = self.equipped['L-HAND']
			for item in self.equipment:
				if item.type == "melee":
					meleeNum +=1
					items.append(item)
				elif item.type == "ranged":
					rangedNum +=1
					items.append(item)
				elif item.type == "shield":
					shieldNum +=1
					items.append(item)
			totalItems = meleeNum + rangedNum + shieldNum
			if totalItems > 0:
				while choice < 1 or choice > totalItems:
					for index, equippable in enumerate(items):
						print index+1, ")", item.name
					choice = input("\n>> ")
				theItem = items[choice-1]
				if rangedNum > 0:	
					if theItem.type == 'ranged':
						if right != ' ' and left == ' ':
							self.equipment.append(right)
						elif right == ' ' and left != ' ':
							self.equipment.append(left)
						elif right != ' ' and left != ' ':
							self.equipment.append(right)
							self.equipment.append(left)
						self.equip('R-HAND', theItem)
					else:
						if right!= ' ':
							self.equipment.append(right)
						self.equip('R-HAND', theItem)		
			elif totalItems == 0:
				print "You do not have any weapons or shields to equip."
		elif choice == 5:
			items=[]
			meleeNum=0
			rangedNum=0
			shieldNum=0
			choice = 0
			right = self.equipped['R-HAND']
			left = self.equipped['L-HAND']
			for item in self.equipment:
				if item.type == "melee":
					meleeNum +=1
					items.append(item)
				elif item.type == "ranged":
					rangedNum +=1
					items.append(item)
				elif item.type == "shield":
					shieldNum +=1
					items.append(item)
			totalItems = meleeNum + rangedNum + shieldNum
			if totalItems > 0:
				while choice < 1 or choice > totalItems:
					for index, equippable in enumerate(items):
						print index+1, ")", item.name
					choice = input("\n>> ")
				theItem = items[choice-1]
				if rangedNum > 0:	
					if theItem.type == 'ranged':
						if right != ' ' and left == ' ':
							self.equipment.append(right)
						elif right == ' ' and left != ' ':
							self.equipment.append(left)
						elif right != ' ' and left != ' ':
							self.equipment.append(right)
							self.equipment.append(left)
						self.equip('L-HAND', theItem)
					else:
						if left != ' ':
							self.equipment.append(left)
						self.equip('L-HAND', theItem)		
			elif totalItems == 0:
				print "You do not have any weapons or shields to equip."
		elif choice == 6:
			boots = []
			bootNum=0
			choice = 0
			for item in self.equipment:
				if item.type == "boot":
					bootNum +=1
					boots.append(item)
			if bootNum > 0:
				while choice < 1 or choice > bootNum:
					for index, item in enumerate(boots):
						print index+1, ")", item.name
					choice = input("\n>> ")
				theItem = boots[choice-1]
				if self.equipped['FEET'] != ' ':
					self.equipment.append(self.equipped['FEET'])
				self.equip('FEET', theItem)			
			elif bootNum == 0:
				print "You do not have any boots to equip."
		elif choice == 7:
			accessory = []
			accessoryNum=0
			choice = 0
			for item in self.equipment:
				if item.type == "necklace":
					accessoryNum +=1
					accessory.append(item)
			if accessoryNum > 0:
				while choice < 1 or choice > accessoryNum:
					for index, item in enumerate(accessory):
						print index+1, ")", item.name
					choice = input("\n>> ")
				theItem = accessory[choice-1]
				if self.equipped['ACC'] != ' ':
					self.equipment.append(self.equipped['ACC'])
				self.equip('ACC', theItem)			
			elif accessoryNum == 0:
				print "You do not have any accessories to equip."
		elif choice == 8:
			rightRing = []
			rightRingNum=0
			choice = 0
			for item in self.equipment:
				if item.type == "ring":
					rightRingNum +=1
					rightRing.append(item)
			if rightRingNum > 0:
				while choice < 1 or choice > rightRingNum:
					for index, item in enumerate(rightRing):
						print index+1, ")", item.name
						choice = input("\n>> ")
				theItem = rightRing[choice-1]
				if self.equipped['R-RING'] != ' ':
					self.equipment.append(self.equipped['R-RING'])
				self.equip('R-RING', theItem)			
			elif rightRingNum == 0:
				print "You do not have any rings to equip."
		elif choice == 9:
			leftRing = []
			leftRingNum=0
			choice = 0
			for iitem in self.equipment:
				if item.type == "ring":
					leftRingNum +=1
					leftRing.append(item)
			if leftRingNum > 0:
				while choice < 1 or choice > leftRingNum:
					for index, item in enumerate(leftRing):
						print index+1, ")", item.name
						choice = input("\n>> ")
				theItem=leftRing[choice-1]
				if self.equipped['L-RING'] != ' ':
					self.equipment.append(self.equipped['L-RING'])
				self.equip('L-RING', theItem)			
			elif leftRingNum == 0:
				print "You do not have any rings to equip."
		elif choice == 10:
			pass
		else:
			"\nI'm sorry that is not a valid entry."
	def equip(self, slot, item):
		self.equipped[slot] = item
		self.equipment.remove(item) 
	def unequip(self, slot, item):
		self.equipment.append(item)
		self.equipped[slot] = " "
#####   $$$$$$$$$$$$$$$$$$$$$$$$   CHARACTER MONEY MANAGEMENT FUNCTIONS $$$$$$$$$$$$$$$$$$$$$$$$$    ##########
	def checkGold(self, itemPrice):
		if self.gold >= itemPrice:
			return True
		else:
			return False
	def changeGold(self, increaseDecrease, amount):
		if increaseDecrease == "-":
			self.gold -= amount
		elif increaseDecrease == "+":
			self.gold += amount
