"""
Created on November 14, 2012

@author Matthew
"""
class Weapon:
	def __init__(self, item):
		self.name=item[0]
		self.desc=item[1]
		self.dieNum=item[2]
		self.dieSides=item[3]
		self.buy=item[4]
		self.sell=item[5]
		#self.weight=item[6]
	def __repr__(self):
		return "melee"
	def printInfo(self):
		print "Name:", self.name, ""
		print "Description:", self.desc, ""
		print "Damage Die:", self.dieNum, "d", self.dieSides, ""
		print "Purchase Amount:", self.buy, ""
		print "Sell Value:", self.sell, "\n"
		#print "The item's weight is", self.weight, "\n"
class Ranged:
	def __init__(self, item):
		self.name=item[0]
		self.desc=item[1]
		self.dieNum=item[2]
		self.dieSides=item[3]
		self.range=item[4]		
		self.buy=item[5]
		self.sell=item[6]
		#self.weight=item[7]
	def __repr__(self):
		return "ranged"
	def printInfo(self):
		print "Name:", self.name, ""
		print "Description:", self.desc, ""
		print "Damage Die:", self.dieNum, "d", self.dieSides, ""
		print "Range:", self.range, "meters"
		print "Purchase Amount:", self.buy, ""
		print "Sell Value:", self.sell, "\n"
		#print "The item's weight is", self.weight, "\n"
class Armor:
	def __init__(self, item):
		self.name=item[0]
		self.desc=item[1]
		self.defense=item[2]
		self.dexPenalty=item[3]
		self.buy=item[4]
		self.sell=item[5]
		#self.weight=item[6]
	def __repr__(self):
		return "armor"
	def printInfo(self):
		print "Name:", self.name, ""
		print "Description:", self.desc, ""
		print "Defense Value:", self.defense, ""
		print "Dexterity Penalty:", self.dexPenalty, ""
		print "Purchase Amount:", self.buy, ""
		print "Sell Value:", self.sell, "\n"
		#print "The item's weight is", self.weight, "\n"
class Gauntlet:
	def __init__(self, item):
		self.name=item[0]
		self.desc=item[1]
		self.defense=item[2]
		self.dexPenalty=item[3]
		self.buy=item[4]
		self.sell=item[5]
		#self.weight=item[6]
	def __repr__(self):
		return "gauntlets"
	def printInfo(self):
		print "Name:", self.name, ""
		print "Description:", self.desc, ""
		print "Defense Value:", self.defense, ""
		print "Dexterity Penalty:", self.dexPenalty, ""
		print "Purchase Amount:", self.buy, ""
		print "Sell Value:", self.sell, "\n"
		#print "The item's weight is", self.weight, "\n"
class Helmet:
	def __init__(self, item):
		self.name=item[0]
		self.desc=item[1]
		self.defense=item[2]
		self.dexPenalty=item[3]
		self.buy=item[4]
		self.sell=item[5]
		#self.weight=item[6]
	def __repr__(self):
		return "helmet"
	def printInfo(self):
		print "Name:", self.name, ""
		print "Description:", self.desc, ""
		print "Defense Value:", self.defense, ""
		print "Dexterity Penalty:", self.dexPenalty, ""
		print "Purchase Amount:", self.buy, ""
		print "Sell Value:", self.sell, "\n"
		#print "The item's weight is", self.weight, "\n"
class Boots:
	def __init__(self, item):
		self.name=item[0]
		self.desc=item[1]
		self.defense=item[2]
		self.dexPenalty=item[3]
		self.buy=item[4]
		self.sell=item[5]
		#self.weight=item[6]
	def __repr__(self):
		return "boots"
	def printInfo(self):
		print "Name:", self.name, ""
		print "Description:", self.desc, ""
		print "Defense Value:", self.defense, ""
		print "Dexterity Penalty:", self.dexPenalty, ""
		print "Purchase Amount:", self.buy, ""
		print "Sell Value:", self.sell, "\n"
		#print "The item's weight is", self.weight, "\n"
class Shield:
	def __init__(self, item):
		self.name=item[0]
		self.desc=item[1]
		self.defense=item[2]
		self.dexPenalty=item[3]
		self.buy=item[4]
		self.sell=item[5]
		#self.weight=item[6]
	def __repr__(self):
		return "shield"
	def printInfo(self):
		print "Name:", self.name, ""
		print "Description:", self.desc, ""
		print "Defense Value:", self.defense, ""
		print "Dexterity Penalty:", self.dexPenalty, ""
		print "Purchase Amount:", self.buy, ""
		print "Sell Value:", self.sell, "\n"
		#print "The item's weight is", self.weight, "\n"
class Necklace:
	def __init__(self, item):
		self.name=item[0]
		self.desc=item[1]
		self.trait=item[2]
		self.effect=item[3]
		self.value=item[4]
		self.buy=item[5]
		self.sell=item[6]
		#self.weight=item[7]
	def __repr__(self):
		return "necklace"
	def printInfo(self):
		print "Name:", self.name, ""
		print "Description:", self.desc, ""
		print "Trait affected:", self.trait, ""
		print "Effect:", self.effect, ""
		print "Effect Value:", self.value, ""
		print "Purchase Amount:", self.buy, ""
		print "Sell Value:", self.sell, "\n"
		#print "The item's weight is", self.weight, "\n"
class Ring:
	def __init__(self, item):
		self.name=item[0]
		self.desc=item[1]
		self.trait=item[2]
		self.effect=item[3]
		self.value=item[4]
		self.buy=item[5]
		self.sell=item[6]
		#self.weight=item[7]
	def __repr__(self):
		return "ring"
	def printInfo(self):
		print "Name:", self.name, ""
		print "Description:", self.desc, ""
		print "Trait affected:", self.trait, ""
		print "Effect:", self.effect, ""
		print "Effect Value:", self.value, ""
		print "Purchase Amount:", self.buy, ""
		print "Sell Value:", self.sell, "\n"
		#print "The item's weight is", self.weight, "\n"
class Item:
	def __init__(self, item):
		self.name=item[0]
		self.desc=item[1]
		self.effectType=item[2]
		self.effectVal=item[3]
		self.buy=item[4]
		self.sell=item[5]
		#self.weight=item[6]
	def __repr__(self):
		return "item"
	def printInfo(self):
		print "Name:", self.name, ""
		print "Description:", self.desc, ""
		print "Effect:", self.effectType, ""
		print "Effect Value:", self.effectVal, ""
		print "Purchase Amount:", self.buy, ""
		print "Sell Value:", self.sell, "\n"
		#print "The item's weight is", self.weight, "\n"
#info for item addition========
	# [item1 in list = Name, item2 = Description of item, item3 = amount of dice to roll for damage, item4 = sides of the dice to roll, item5 = buy value, item6= sell value, item7=weight]
meleeList= [
	    ["Dagger", "A very small knife. Only suitable for emergency situations.", 1, 4, 25, 10], 
	    ["Short Sword", "A small sword used to fight smaller foes.", 1, 6, 35, 15],
	    ["Long Sword", "A decent sword used in combat.", 1, 8, 50, 20], 
	    ["Staff", "A wooden staff engraved with the user's insignia.", 1, 6, 35, 15],
	    ["Mace", "A large club used typically by Clerics.", 1, 8, 50, 20], 
	    ["Warhammer", "A heavy, two-handed weapon capable of a large amount of damage", 2, 8, 100, 45],
	   ] 
#ranged weapons follow the same formula above, with the addition of a fifth item in the list used for the range of the weapon, followed by buy value, sell value, and weight
rangedList= [
	     ["Short Bow", "A small bow used for hunting.", 1, 6, 350, 55, 25], 
	     ["Long Bow", "A large bow used by the military for long-range combat.", 2,6, 500, 100, 45],
	     ["Sling", "A small slingshot which hurls stones at your enemies.", 1, 6, 200, 40, 15],
	     ["Throwing Knives", "Sharp knives that deal a good amount of damage.", 2, 4, 100, 5, 1],
	    ]
#armor addition is name, description, defense value, dexterity penalty, buy value, sell value, weight.
armorList= [
	    ["Mage's Robes", "Lightweight robes providing little protection.", 10, 0, 10, 1],
	    ["Monk's Garb", "Heavier cloth providing more protection than a mage's robes.", 12, 0, 15, 2], 
            ["Leather Armor", "Lightweight armor that provides decent protection.", 20, 0, 25, 10],
	    ["Studded Armor", "Leather armor with studs to deflect sword slashes.", 25, 0, 50, 30], 
            ["Hide Armor", "Armor made from the tough hides of animals.", 15, 1, 20, 5],
	    ["Scale Armor", "Leather armor made from the hard scales of creatures.", 30, 2, 75, 35], 
            ["Chainmail", "Linked metal rings that provide a lot of protection.", 35, 3, 100, 45],
            ["Steel Armor", "Heavy armor forged to withstand a lot of damage.", 40, 4, 125, 55], 
	    ["Plate Armor", "Iron plates forged and pieced together to allow superior protection.", 50, 5, 175, 75],
	   ]

shieldList=[
	    ["Small Shield","A small shield used to increase defense.", 15, 2, 20, 7],
	    ["Medium Shield", "A larger shield that provides a substantial boost to defense.", 25, 3, 30, 10],
	   ]
#gauntletList=[]
#bootList=[]
#helmetList=[]
#necklaceList=[]
#ringList=[]
#item addition is name, description, effect type, i.e. heal, status, damage, etc., value for effect, i.e. +100 for healing, -20 for damage, "+Confused" for status adding #confusion, "-Poison" for removing poison, buy value, sell value, weight
itemList= [
		["Light Potion", "A small potion for healing light wounds.", "Healing", 25, 50, 30],
		["Sober Potion", "A potion used to aid in recovering one's wits.", "Status", "-Confused", 25, 10],
		["Medium Potion", "A medium-sized potion for healing more serious wounds.", "Healing", 50, 100, 45],
		["Small Mana Potion", "A small potion for recovering mp.", "MP Recover", 25, 50, 30],
		["Large Mana Potion", "A large potion that recovers a large amount of mp.", "MP Recover", 50, 100, 45],
		["Elixir", "A special potion that fully restores all hp and mp.", "Healing", 100, 200, 1],
	  ]
