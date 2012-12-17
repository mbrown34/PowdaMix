"""
Created on November 11, 2012


@author Matthew
"""
import diceRoll
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
		self.stats={"STR": 0,"DEX": 0,"CON": 0,"INT": 0,"WIS": 0,"CHA: 0"}
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
		print self.stats.items()
		extraPoints=tools.roll(4,6)
	        while extraPoints > 0 or choice < 1 or choice > 6:
			print "\nYou have", extraPoints,"to spend on increasing stats."
			print "Which stat would you like to increase? (You cannot increase higher than 18)\n"
			print "\n\t1) STR:",self.stats['STR'],"\t2) DEX:",self.stats['DEX'],"\t3) CON:",self.stats['CON'],"\t4) INT:",self.stats['INT'],"\t5) WIS:",self.stats['WIS'],"\t6) CHA:",self.stats['CHA'],"\n"
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
			self.equipment.remove(self.equipment[1])
			self.equip('L-HAND', self.equipment[1])
			self.equipment.remove(self.equipment[1])
			self.equip('BODY', self.equipment[1])
			self.equipment.remove(self.equipment[1])
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Medium Potion")
		elif self.job=='Mage':
			self.addItem("equipment", "meleeList","Staff")
			self.addItem("equipment", "armorList","Mage's Robes")
			self.addItem("equipment","meleeList", "Dagger")
			self.equip('R-HAND', self.equipment[0])
			self.equipment.remove(self.equipment[0])
			self.equip('BODY', self.equipment[0])
			self.equipment.remove(self.equipment[0])
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
			self.equipment.remove(self.equipment[2])
			self.equip('R-HAND', self.equipment[2])
			self.equipment.remove(self.equipment[2])
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Medium Potion")
		elif self.job=='Ranger':
			self.addItem("equipment", "meleeList","Long Sword")
			self.addItem("equipment", "rangedList","Long Bow")
			self.addItem("equipment", "armorList","Studded Armor")
			self.equip('R-HAND', self.equipment[1])
			self.equipment.remove(self.equipment[1])
			self.equip('BODY', self.equipment[1])
			self.equipment.remove(self.equipment[1])
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Medium Potion")
			self.addItem("equipment","itemList", "Medium Potion")
		elif self.job=='Cleric':
			self.addItem("equipment", "meleeList","Mace")
			self.addItem("equipment", "shieldList","Small Shield")
			self.addItem("equipment", "armorList","Scale Armor")
			self.equip('R-HAND', self.equipment[0])	
			self.equipment.remove(self.equipment[0])
			self.equip('L-HAND', self.equipment[0])
			self.equipment.remove(self.equipment[0])
			self.equip('BODY', self.equipment[0])
			self.equipment.remove(self.equipment[0])
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Medium Potion")
			self.addItem("equipment","itemList", "Small Mana Potion")
		elif self.job=='Monk':
			self.addItem("equipment", "armorList","Monk's Garb")
			self.equip('BODY', self.equipment[0])
			self.equipment.remove(self.equipment[0])
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
		arms = self.equipped['ARMS']
		head = self.equipped['HEAD']
		accessory=self.equipped['ACC']
		armor=self.equipped['BODY']
		rightHand=self.equipped['R-HAND']
		leftHand=self.equipped['L-HAND']
		boots=self.equipped['FEET']
		rRing=self.equipped['R-RING']
		lRing=self.equipped['L-RING']
		print "\t\t\tEQUIPPED ITEMS:\n"
		print "  ARMS [", arms.name , "]       HEAD  [", head.name, "]       ACCESSORY [", accessory.name, "]"
		print "                     ARMOR [", armor.name, "]  "
		print "  RIGHT HAND [",rightHand.name , "]   BOOTS [", boots.name, "]      LEFT HAND  [", leftHand.name, "]"
		print "         RIGHT RING [", rRing.name, "]           LEFT RING [", lRing.name, "]" 
		
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
		x=0
		for stat in self.statNames and self.statVals:
			print "\t", self.statNames[x], ":", self.statVals[x], ""
			x+=1
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
	def manageInventory(self):
		self.displayEquipped()
		choice =0
		while choice < 1 or choice > 10:
			print "\nWhat equipment do you want to wear?"
			print "1) Helmet 2) Armor 3) Gauntlets 4) Equip to right hand 5) Equip to left hand 6) Boots 7) Accessory 8) Right-hand ring 9) Left-hand ring 10) Exit"
			choice = input("\n>> ")
		if choice == 1:
			helmets = []
			indeces = []
			helmetNum=0
			choice = 0
			for index, item in enumerate(self.equipment):
				if item.type == "helmet":
					helmetNum +=1
					indeces.append(index)
					helmets.append(item)
			if helmetNum > 0:
				x=1
				while choice < 0 or choice > helmetNum:
					for item in helmets:
						print x, ")", item.name
						x+=1
					choice = input("\n>> ")
					if self.equipped['HEAD'] == ' ':
						self.equipped['HEAD'] = helmets[choice-1]
						self.equipment.remove(self.equipment[indeces[choice-1]])
					else:
						self.equipment.append(self.equipped['HEAD'])
						self.equipped['HEAD'] = helmets[choice-1]
						self.equipment.remove(self.equipment[indeces[choice-1]])
					
						
			elif helmetNum == 0:
				print "You do not have any helmets to equip."
		elif choice == 2:
			armor = []
			indeces = []
			armorNum=0
			choice = 0
			for index, item in enumerate(self.equipment):
				if item.type == "armor":
					armorNum +=1
					indeces.append(index)
					armor.append(item)
			if armorNum > 0:
				x=1
				while choice < 0 or choice > armorNum:
					for item in armor:
						print x, ")", item.name
						x+=1
					choice = input("\n>> ")
					if self.equipped['BODY'] == ' ':
						self.equipped['BODY'] = armor[choice-1]
						self.equipment.remove(self.equipment[indeces[choice-1]])
					else:
						self.equipment.append(self.equipped['BODY'])
						self.equipped['BODY'] = armor[choice-1]
						self.equipment.remove(self.equipment[indeces[choice-1]])
					
						
			elif armorNum == 0:
				print "You do not have any armor to equip."
		elif choice == 3:
			gauntlets = []
			indeces = []
			gauntNum=0
			choice = 0
			for index, item in enumerate(self.equipment):
				if item.type == "gauntlets":
					gauntNum +=1
					indeces.append(index)
					gauntlets.append(item)
			if gauntNum > 0:
				x=1
				while choice < 0 or choice > gauntNum:
					for item in gauntlets:
						print x, ")", item.name
						x+=1
					choice = input("\n>> ")
					if self.equipped['ARMS'] == ' ':
						self.equipped['ARMS'] = gauntlets[choice-1]
						self.equipment.remove(self.equipment[indeces[choice-1]])
					else:
						self.equipment.append(self.equipped['ARMS'])
						self.equipped['ARMS'] = gauntlets[choice-1]
						self.equipment.remove(self.equipment[indeces[choice-1]])
					
						
			elif gauntNum == 0:
				print "You do not have any gauntlets to equip."
			
	
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
