"""
Created on November 14, 2012

@author Matthew
"""
#info for item addition========
	# [item1 in list = Name, item2 = Description of item, item3 = amount of dice to roll for damage, item4 = sides of the dice to roll]
def addItem(self, fileName, listName, itemName):
		imported = getattr(__import__(fileName, fromlist=[listName]), listName)
		x=0
		for item in imported:
			if itemName==imported[x][0]:
				return imported[x]
			else:
			        x+=1

meleeList= [
	    ["Dagger", "A very small knife. Only suitable for emergency situations.", 1, 4], 
	    ["Short Sword", "A small sword used to fight smaller foes.", 1, 6],
	    ["Long Sword", "A decent sword used in combat.", 1, 8], 
	    ["Staff", "A wooden staff engraved with the user's insignia.", 1, 6],
	    ["Mace", "A large club used typically by Clerics.", 1, 8], 
	    ["Warhammer", "A heavy, two-handed weapon capable of a large amount of damage", 2, 8],
	   ] 
#ranged weapons follow the same formula above, with the addition of a fifth item in the list used for the range of the weapon
rangedList= [
	     ["Short Bow", "A small bow used for hunting.", 1, 6, 350], 
	     ["Long Bow", "A large bow used by the military for long-range combat.", 2,6, 500],
	     ["Sling", "A small slingshot which hurls stones at your enemies.", 1, 6, 200],
	     ["Throwing Knives", "Sharp knives that deal a good amount of damage.", 2, 4, 100],
	    ]
#armor addition is name, description, defense value, dexterity penalty
armorList= [
	    ["Mage's Robes", "Lightweight robes providing little protection.", 10, 0],
	    ["Monk's Garb", "Heavier cloth providing more protection than a mage's robes.", 15, 0], 
            ["Leather Armor", "Lightweight armor that provides decent protection.", 20, 0],
	    ["Studded Armor", "Leather armor with studs to deflect sword slashes.", 25, 0], 
            ["Hide Armor", "Armor made from the tough hides of animals.", 15, 1],
	    ["Scale Armor", "Leather armor made from the hard scales of creatures.", 30, 2], 
            ["Chainmail", "Linked metal rings that provide a lot of protection.", 35, 3],
            ["Steel Armor", "Heavy armor forged to withstand a lot of damage.", 40, 4], 
	    ["Plate Armor", "Iron plates forged and pieced together to allow superior protection.", 50, 5],
	    ["Small Shield","A small shield used to increase defense.", 15, 2],
	    ["Medium Shield", "A larger shield that provides a substantial boost to defense.", 25, 3],
	   ]

#item addition is name, description, effect type, i.e. heal, status, damage, etc., value for effect, i.e. +100 for healing, -20 for damage, "+Confused" for status adding #confusion, "-Poison" for removing poison
itemList= [
		["Light Potion", "A small potion for healing light wounds.", "Healing", 25],
		["Sober Potion", "A potion used to aid in recovering one's wits.", "Status", "-Confused"],
		["Medium Potion", "A medium-sized potion for healing more serious wounds.", "Healing", 50],
	  ]
