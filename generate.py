"""
Created on November 11, 2012


@author Matthew
"""
import diceRoll
#import spells
#import skills
#import equipment
#import items
class Player:
	def __init__(self):
		self.name=''
		self.race=''
		self.job=''
		self.statNames=["STR","DEX","CON","INT","WIS","CHA"]
		self.statVals=[]
		self.hp=0
		self.equip=[]
		self.equipment=[]
		self.items=[]
		self.spells=[]
		self.skills=[]
		#functions that will run to populate an initial character object's variables
		#this should allow each character object to be different from the last one created
		self.addName()
		self.addRace()
		self.setVals()
		#self.raceBonus()
		self.setHP()
		self.addJob()
		#self.initialEquip()
		#self.initialInv()
		#self.initialSpells()
		#self.initialSkills()
	def __str__(self):
		return "Character"
	def __repr__(self):
		return "Character"
	
	def addName(self):
		print "\nWhat will the character's name be?\n"
		self.name=raw_input(">>")	
	def addRace(self):
		choice = 0
		while choice < 1 or choice > 5:
			print "\nWhat is the new character's race?\n\n\t1) Human   2) Elven   3) Half-Elven   4) Dwarven   5) Halfling\n"
			choice = input(">>")
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
			choice = input(">>")
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
	def raceBonus(self):
		print
	def initialEquip(self):
		print
	def initialInv(self):
		print
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
		
