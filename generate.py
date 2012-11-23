"""
Created on November 11, 2012


@author Matthew
"""
import diceRoll
#import spells
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
		self.hp=0
		self.mp=0
		self.weapon=[]
		self.range=[]
		self.equipment=[]
		self.armor=[]
		self.items=[]
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
		self.hp=die.roll(dice,6)
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
		self.mp=die.roll(dice,6)
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
			print"\t", self.statNames[n], ": ", self.statVals[n], "\n"
			n+=1
		extraPoints=die.roll(3,6)
	        while extraPoints > 0 or choice < 1 or choice > 6:
			print "You have", extraPoints,"to spend on increasing stats."
			print "Which stat would you like to increase? (You cannot increase higher than 18)"
			n=1
			for i in self.statNames and self.statVals:
				print"\t", n, ")", self.statNames[n-1], ": ", self.statVals[n-1], "\n"
				n+=1
			choice = input("\n>> ")
			if choice == 1:
				if self.statVals[choice-1] < 18:
					self.statVals[choice-1] +=1
					extraPoints-=1
			elif choice ==2:
				if self.statVals[choice-1] < 18:
					self.statVals[choice-1] +=1
					extraPoints-=1
			elif choice ==3:
				if self.statVals[choice-1] < 18:
					self.statVals[choice-1] +=1
					extraPoints-=1
			elif choice ==4:
				if self.statVals[choice-1] < 18:
					self.statVals[choice-1] +=1
					extraPoints-=1
			elif choice ==5:
				if self.statVals[choice-1] < 18:
					self.statVals[choice-1] +=1
					extraPoints-=1
			elif choice ==6:
				if self.statVals[choice-1] < 18:
					self.statVals[choice-1] +=1
					extraPoints-=1
			else:
				print"\nI am sorry, either that is not a valid choice or that stat is maxed out.  Please try again..."
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
	def initialEquip(self):
		if self.job=='Fighter':
			self.weapon.append(equipment.addItem(self,"equipment","meleeList","Long Sword"))
			self.range.append(equipment.addItem(self,"equipment","rangedList","Short Bow"))
			self.armor.append(equipment.addItem(self,"equipment", "armorList","Medium Shield"))
			self.armor.append(equipment.addItem(self,"equipment","armorList", "Studded Armor"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Light Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Light Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Medium Potion"))			
		elif self.job=='Mage':
			self.weapon.append(equipment.addItem(self,"equipment", "meleeList","Staff"))
			self.armor.append(equipment.addItem(self,"equipment", "armorList","Mage's Robes"))
			self.equipment.append(equipment.addItem(self,"equipment","meleeList", "Dagger"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Light Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Light Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Small Mana Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Large Mana Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Large Mana Potion"))
		elif self.job=='Thief':
			self.weapon.append(equipment.addItem(self,"equipment", "meleeList","Dagger"))
			self.range.append(equipment.addItem(self,"equipment", "rangedList","Short Bow"))
			self.armor.append(equipment.addItem(self,"equipment", "armorList","Leather Armor"))
			self.equipment.append(equipment.addItem(self,"equipment","meleeList", "Short Sword"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Light Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Light Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Medium Potion"))
		elif self.job=='Ranger':
			self.weapon.append(equipment.addItem(self,"equipment", "meleeList","Long Sword"))
			self.range.append(equipment.addItem(self,"equipment", "rangedList","Long Bow"))
			self.armor.append(equipment.addItem(self,"equipment", "armorList","Studded Armor"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Light Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Light Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Medium Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Medium Potion"))
		elif self.job=='Cleric':
			self.weapon.append(equipment.addItem(self,"equipment", "meleeList","Mace"))
			self.armor.append(equipment.addItem(self,"equipment", "armorList","Small Shield"))
			self.armor.append(equipment.addItem(self,"equipment", "armorList","Scale Armor"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Light Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Light Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Medium Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Small Mana Potion"))
		elif self.job=='Monk':
			self.armor.append(equipment.addItem(self,"equipment", "armorList","Monk's Garb"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Light Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Light Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Light Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Light Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Medium Potion"))
			self.items.append(equipment.addItem(self,"equipment","itemList", "Medium Potion"))
	def displayEquip(self):
			print "Your equipped melee weapon is:"
			for x in self.weapon: 
				print x
			print "Your equipped ranged weapon is:"
			for x in self.range: 
				print x
			print "Your equipped armor is:"
			for x in self.armor: 
				print x
			print "Your equippable items are:"
			for x in self.equipment:
				print x
			print "Your usable items are:"
			for x in self.items:
				print x
	def setGold(self):
		die=diceRoll.Die()
		self.gold=die.roll(100,5)
	def initialSpells(self):
		print
	def initialSkills(self):
		print
	def displayInfo(self):
		print"\n\tYour Name:", self.name,"\n\tYour Race:", self.race,"\n\tYour Class:", self.job, "\n"
		print"\tYour stats are:\n"
		x=0
		for stat in self.statNames and self.statVals:
			print "\t", self.statNames[x], ":", self.statVals[x], "\n"
			x+=1
		print"Your hp is:", self.hp, " "
		print"Your mp is:", self.mp, " "
	def save(self):
		print
	def load(self):
		print
