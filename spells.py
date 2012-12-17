"""
Created on November 27, 2012
	
@author Matthew
"""
class Spell:
	def __init__(self, item):
		self.name=item[0]
		self.desc=item[1]
		self.effect=item[2]
		self.effectVal=item[3]
		self.effectVal2=item[4]
		self.type="spell"
		
	def __repr__(self):
		return "spell"
	def printInfo(self):
		print "Spell Name:", self.name
		print "Spell Desc:", self.desc
		print "Spell Effect:", self.effect
		print "Effect Value 1:", self.effectVal
		print "Effect Value 2:", self.effectVal2, "\n"


spellList=[
		["Magic Darts", "Magically conjured darts that attack your foe without fail.", "damage", 3, 4],
		["Fire", "Magically conjured fire that burns your foe.", "damage", 2, 6],
		["Ice", "Magically conjured ice that freezes your foe.", "damage", 2, 6],
	  ]
