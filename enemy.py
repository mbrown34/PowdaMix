"""
Created on November 27, 2012

@author Matthew
"""
import diceRoll
import random
class Enemy:	      
	def __init__(self):
		self.name=""
		self.desc=""
		self.hp=0
		self.attack=0
		self.defense=0
		self.xp=0
		self.renown=0
		self.gold=0
		
		self.setVals(genEnemy())
 	def __str__(self):
		return self.name
	def __repr__(self):
		return 'Enemy'
	def hp(self):
		return self.hp
	def attack(self):
		return self.attack
	def defense(self):
		return self.defense
	def exp(self):
		return self.xp
	def renown(self):
		return self.renown
	def gold(self):
		return self.gold
	def setVals(self, enemy):
		self.name=enemy[0]
		self.desc=enemy[1]
		self.hp=enemy[2]
		self.attack=enemy[3]
		self.defense=enemy[4]
		self.xp=enemy[5]
		self.renown=enemy[6]
		self.gold=enemy[7]
	def printInfo(self):
		print "Name:", self.name,""
		print "Desc:", self.desc,""
		print "HP:", self.hp, ""
		print "Attack:", self.attack,""
		print "Defense:", self.defense,""
		print "Exp:", self.xp,""
		print "Renown:", self.renown,""
		print "Gold Drop:", self.gold,"\n"

def genEnemy():
	badguy = []
	from enemylist import enemylist
	foe = random.choice(enemylist)
	badguy = foe[:]
	hp = setHealth(foe[2])
	goldDrop = setGold(foe[7])
	badguy[2] = hp
	badguy[7] = goldDrop
	return badguy
def setHealth(hitdice):
	die = diceRoll.Die()
	hp = die.roll(hitdice, 6)
	return hp
def setGold(gold):
	die = diceRoll.Die()
	goldAmt = die.roll(gold, 6)
	return goldAmt

