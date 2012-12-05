"""
Created on November 11, 2012


@author Matthew
"""
import diceRoll
import spells
#import skills
import equipment
#import items
class Player:
	def __init__(self):
		self.name='None'
		self.race='None'
		self.job='None'
		self.statNames=["STR","DEX","CON","INT","WIS","CHA"]
		self.statVals=[]
		self.currentHP=0
		self.maxHP=0
		self.currentMP=0
		self.maxMP=0
		self.equipped=[]
		self.equipment=[]
		#self.maxCarry=0
		self.items=[]
		self.accessories=[]
		self.spells=[]
		self.skills=[]
		self.gold=0
		#functions that will run to populate an initial character object's variables
		#this should allow each character object to be different from the last one created
		self.addName()
		self.addRace()
		self.setVals()
		self.raceBonus()
		self.setHP()
		self.setMP()
		self.displayInfo()
		self.addJob()
		self.initialInv()
		self.initialEquip()
		self.setGold()
		#self.initialSpells()
		#self.initialSkills()
	def __str__(self):
		return "Character"
	def __repr__(self):
		return "Character"
	
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
		die=diceRoll.Die()
		if self.statVals[2] >18:
			dice=16
		elif self.statVals[2] >16:
			dice=15
		elif self.statVals[2] >14:
			dice=14
		elif self.statVals[2] >12:
			dice=13
		elif self.statVals[2] >10:
			dice=12
		elif self.statVals[2] >8:
			dice=11
		elif self.statVals[2] >6:
			dice=10
		elif self.statVals[2] >4:
			dice=9
		elif self.statVals[2] >2:
			dice=8
		self.maxHP=die.roll(dice,6)
		self.currentHP=self.maxHP
	def setMP(self):
		die=diceRoll.Die()
		if self.statVals[4] >18:
			dice=14
		elif self.statVals[4] >16:
			dice=13
		elif self.statVals[4] >14:
			dice=12
		elif self.statVals[4] >12:
			dice=11
		elif self.statVals[4] >10:
			dice=10
		elif self.statVals[4] >8:
			dice=9
		elif self.statVals[4] >6:
			dice=8
		elif self.statVals[4] >4:
			dice=7
		elif self.statVals[4] >1:
			dice=6
		self.maxMP=die.roll(dice,6)
		self.currentMP=self.maxMP
	def setVals(self):
		die=diceRoll.Die()
		x=0
		while x<6:
			roll=die.roll(3,6)
			self.statVals.append(roll)
			x+=1
		print "\nYour current stat rolls are:\n"
		n=0
		for i in self.statNames and self.statVals:
			print"\t", self.statNames[n], ": ", self.statVals[n], ""
			n+=1
		extraPoints=die.roll(3,6)
	        while extraPoints > 0 or choice < 1 or choice > 6:
			print "\nYou have", extraPoints,"to spend on increasing stats."
			print "Which stat would you like to increase? (You cannot increase higher than 18)\n"
			n=1
			for i in self.statNames and self.statVals:
				print"\t", n, ")", self.statNames[n-1], ": ", self.statVals[n-1], ""
				n+=1
			choice = input("\n>> ")
			if choice == 1:
				if self.statVals[choice-1] < 18:
					self.statVals[choice-1] +=1
					extraPoints-=1
				else:
					print "That stat is maxed out..."
			elif choice ==2:
				if self.statVals[choice-1] < 18:
					self.statVals[choice-1] +=1
					extraPoints-=1
				else:
					print "That stat is maxed out..."
			elif choice ==3:
				if self.statVals[choice-1] < 18:
					self.statVals[choice-1] +=1
					extraPoints-=1
				else:
					print "That stat is maxed out..."
			elif choice ==4:
				if self.statVals[choice-1] < 18:
					self.statVals[choice-1] +=1
					extraPoints-=1
				else:
					print "That stat is maxed out..."
			elif choice ==5:
				if self.statVals[choice-1] < 18:
					self.statVals[choice-1] +=1
					extraPoints-=1
				else:
					print "That stat is maxed out..."
			elif choice ==6:
				if self.statVals[choice-1] < 18:
					self.statVals[choice-1] +=1
					extraPoints-=1
				else:
					print "That stat is maxed out..."			
			else:
				print"\nI am sorry, that is not a valid choice.  Please try again..."
	def raceBonus(self):
		#statVals[0]=STR [1]=DEX [2]=CON [3]=INT [4]=WIS [5]=CHA
		#Human Elven Half-Elven Dwarven Halfling
		if self.race == 'Elven':
			self.statVals[1] +=2
			self.statVals[2] -=1
			self.statVals[3] +=1
		elif self.race == 'Half-Elven':
			self.statVals[1] +=2
			self.statVals[2] -=1
		elif self.race == 'Dwarven':
			self.statVals[0]+=2
			self.statVals[2] +=3
			self.statVals[3] -=2
			self.statVals[5] -=2
		elif self.race == 'Halfling':
			self.statVals[1] +=3
			self.statVals[2] -=1
			self.statVals[3] +=1
			self.statVals[5] -=2
	def initialInv(self):
		if self.job=='Fighter':
			self.addItem("equipment","rangedList","Short Bow")
			self.addItem("equipment","meleeList","Long Sword")
			self.addItem("equipment", "shieldList","Medium Shield")
			self.addItem("equipment","armorList", "Studded Armor")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Medium Potion")
			
		elif self.job=='Mage':
			self.addItem("equipment", "meleeList","Staff")
			self.addItem("equipment", "armorList","Mage's Robes")
			self.addItem("equipment","meleeList", "Dagger")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Small Mana Potion")
			self.addItem("equipment","itemList", "Large Mana Potion")
			self.addItem("equipment","itemList", "Large Mana Potion")
		elif self.job=='Thief':
			self.addItem("equipment", "meleeList","Dagger")
			self.addItem("equipment", "rangedList","Short Bow")
			self.addItem("equipment", "armorList","Leather Armor")
			self.addItem("equipment","meleeList", "Short Sword")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Medium Potion")
		elif self.job=='Ranger':
			self.addItem("equipment", "meleeList","Long Sword")
			self.addItem("equipment", "rangedList","Long Bow")
			self.addItem("equipment", "armorList","Studded Armor")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Medium Potion")
			self.addItem("equipment","itemList", "Medium Potion")
		elif self.job=='Cleric':
			self.addItem("equipment", "meleeList","Mace")
			self.addItem("equipment", "shieldList","Small Shield")
			self.addItem("equipment", "armorList","Scale Armor")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Medium Potion")
			self.addItem("equipment","itemList", "Small Mana Potion")
		elif self.job=='Monk':
			self.addItem("equipment", "armorList","Monk's Garb")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Light Potion")
			self.addItem("equipment","itemList", "Medium Potion")
			self.addItem("equipment","itemList", "Medium Potion")
	def initialEquip(self):
		weapons=0
		armor=0
		shield=0
		for item in self.equipment:
			if item.__repr__ =="melee":
				if weapons <1:
					self.equipped.append(item)
					weapons+=1
			if item.__repr__ =="armor":
				if armor<1:
					self.equipped.append(item)
					armor+=1
			if item.__repr__=="shield":
				if shield<1:
					self.equipped.append(item)
					shield+=1
	def equip(self, fileName, listName, itemName):
		pass
	def unequip(self, fileName, listName, itemName):
		pass
				
	def displayEquip(self):
		print "Your equipped items are:"
		for x in self.equipped: 
			x.printInfo()
		loopEnter=0
		for x in self.equipment:
			if loopEnter<1:
				print "Your equippable items are:"
				loopEnter+=1
			try:
				x.printInfo()
			except:
				print "\nYou have no additional equippable items in inventory."
		print "Your usable items are:"
		for x in self.items:
			x.printInfo()
	def displaySpells(self):
		for x in self.equipped: 
			x.printInfo()
		loopEnter=0
		for x in self.spells:
			if isinstance(x, spells.Spell):
				if loopEnter==0:
					print "Your usable spells are:"
					loopEnter+=1
				x.printInfo()
			else:
				print "\nYou do not know any spells."
		
	def setGold(self):
		die=diceRoll.Die()
		self.gold=die.roll(100,5)
	def checkGold(self, itemPrice):
		if self.gold >= itemPrice:
			return True
		else:
			print "You do not have enough gold to purchase that item."
			return False

	def initialSpells(self):
		print
	def initialSkills(self):
		print
	def displayInfo(self):
		print"\n\tYour Name:", self.name,"\n\tYour Race:", self.race,"\n\tYour Class:", self.job, ""
		print"\tHP:", self.currentHP, "/", self.maxHP, "\t\tMP:", self.currentMP, "/", self.maxMP, " "
		print"\n\tYour stats are:"
		x=0
		for stat in self.statNames and self.statVals:
			print "\t", self.statNames[x], ":", self.statVals[x], ""
			x+=1	
	def save(self):
		print
	def load(self):
		print
	def addItem(self, fileName, listName, itemName):
		imported = getattr(__import__(fileName, fromlist=[listName]), listName)
		x=0
		for item in imported:
			if itemName==imported[x][0]:
				if listName == "meleeList":
					item=equipment.Weapon(imported[x])
					self.equipment.append(item)
				elif listName=="rangedList":
					item=equipment.Ranged(imported[x])
					self.equipment.append(item)
				elif listName=="armorList":        
					item=equipment.Armor(imported[x])
					self.equipment.append(item)
				elif listName=="shieldList":
					item=equipment.Shield(imported[x])
					self.equipment.append(item)
				elif listName=="gauntletList":
					item=equipment.Gauntlet(imported[x])
					self.equipment.append(item)
				elif listName=="bootList":
					item=equipment.Boots(imported[x])
					self.equipment.append(item)
				elif listName=="helmetList":
					item=equipment.Helmet(imported[x])
					self.equipment.append(item)
				elif listName=="necklaceList":
					item=equipment.Necklace(imported[x])
					self.accessories.append(item)
				elif listName=="ringList":
					item=equipment.Ring(imported[x])
					self.accessories.append(item)
				elif listName=="itemList":        
					item=equipment.Item(imported[x])
					self.items.append(item)
				elif listName=="spellList":
					item=spells.Spell(imported[x])
					self.spells.append(item)
				elif listName=="skillList":
					item=skills.Skill(imported[x])
					self.skills.append(item)
			else:
			        x+=1
	def removeItem(self, item):
		if item.__repr__ == "item":
			self.items.remove(item)
		elif item.__repr__ == "spell":
			self.spells.remove(item)
		elif item.__repr__ == "skill":
			self.skills.remove(item)
		elif item.__repr__ == "ring" or item.__repr__ == "necklace":
			self.accessories.remove(item)
		else:
			self.equipment.remove(item)
