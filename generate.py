"""
Created on November 11, 2012


@author Matthew
"""
import diceRoll
class Player:
	def __init__(self):
		self.character=[]
		self.addName()
		self.addRace()
		self.statNames=["STR","DEX","CON","INT","WIS","CHA"]
		self.statVals=[]
		self.setVals(self.statNames, self.statVals)
		self.raceBonus(self.character, self.statVals)
		self.hp=0
		self.setHP(self.character, self.statVals)
		self.addClass()
		self.equip=[]
		self.equipment=[]
		self.items=[]
		self.spells=[]
		self.skills=[]
	def __str__(self):
		return "Character"
	def __repr__(self):
		return "Character"
	def addName(self):
		print "\nWhat will the character's name be?\n"
		name=raw_input(">>")
		self.character.append(name)
	def addRace(self):
		choice = 0
		while choice < 1 or choice > 5:
			print "\nWhat is the new character's race?\n\n\t1) Human\t2) Elven\t3) Half-Elven\t4) Dwarven\t5) Halfling\n"
			choice = input(">>")
			if choice == 1:
				self.character.append('Human')
			elif choice == 2:
				self.character.append('Elven')
			elif choice == 3:
				self.character.append('Half-Elven')
			elif choice == 4:
				self.character.append('Dwarven')
			elif choice == 5:
				self.character.append('Halfling')
			else:
				print "\nThat is not a valid option. Please try again..."

	def addClass(self):
		choice=0
		while choice < 1 or choice > 6:
			print "\nWhat will the new character's class be?\n\n\t1) Fighter\t2) Mage\t3) Thief\t4) Ranger\t5) Cleric\t6) Monk\n"
			choice = input(">>")
			if choice ==1:
				self.character.append('Fighter')
			elif choice ==2:
				self.character.append('Mage')
			elif choice ==3:
				self.character.append('Thief')
			elif choice ==4:
				self.character.append('Ranger')
			elif choice ==5:
				self.character.append('Cleric')
			elif choice == 6:
				self.character.append('Monk')
			else:
				print "\nThat is not a valid option. Please try again..."
	def setHP(self, character, statVals):
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
	def setVals(self, statNames, statVals):
		die=diceRoll.Die()
		x=0
		while x<6:
			roll=die.roll(3,6)
			self.statVals.append(roll)
			x+=1
		print "\nYour current stat rolls are:\n"
		for i in self.statNames and self.statVals:
			print"\t", self.statNames, ": ", self.statVals, "\n"
		extraPoints=die.roll(3,6)
	        while extraPoints > 0 or choice < 1 or choice > 6:
			print "You have", extraPoints,"to spend on increasing stats."
			print "Which stat would you like to increase? (You cannot increase higher than 18)"
			n=1
			for i in self.statNames and self.statVals:
				print"\t", n, ")", self.statNames[n-1], ": ", self.statVals[n-1], "\n"
				n+=1
			choice = input("\n>>")
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
	def raceBonus(self, character, statVals):
		print
	def addClass(self):
		print
	def displayInfo(self):
		print"\n\tYour Name:", self.character[0],"\n\tYour Race:", self.character[1],"\n\tYour Class: 'not completed yet.'"
		print"\tYour stats are:\n"
		x=0
		for stat in self.statNames and self.statVals:
			print "\t", self.statNames[x], ":", self.statVals[x], "\n"
			x+=1
		print"Your hp is:", self.hp, " "
		
