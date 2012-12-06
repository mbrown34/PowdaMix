"""
Created on November 10, 2012

@author Matthew
"""
import generate
import enemy
#import store
def start():
	title()
	choice = 0
	while choice < 1 or choice > 3:
		print"""\n\n\t\t\tSTART MENU:
		1) Create new player
		2) Load previously saved character
		3) Exit the game
		"""
		choice=input(">> ")
		if choice == 1:
			print
			character=generate.Player()
			character.displayEquip()
			character.displayItems()
			character.displayInfo()
			character.displaySpells()
		elif choice == 2:
			print "This functionality has not been added yet."
			#character= generate.load()
		elif choice == 3:
			gameOver=True
			return gameOver
		else:
			print"\n\nThat is not a valid input choice. Please try again..."
	gameOver=main(character)
	return gameOver

def main(character):
	choice=0
	gameOver=False
	while choice < 1 or choice > 5 or gameOver != True:
		print"""\n\n\t\t\tMAIN MENU:
		1) Purchase equipment from the store
		2) Combat foes in the battle square
		3) View your current character information
		4) Save your current inventory and status
		5) Exit the game
		"""
		choice = input(">> ")
		if choice == 1:
			store(character)
		elif choice == 2:
			print "This functionality has not been fully implemented yet."
			villain=enemy.Enemy()
			villain.printInfo()
		elif choice == 3:
			character.displayEquip()
			character.displayInfo()
			character.displaySpells()
		elif choice == 4:
			print "This functionality has not been added yet."
			#save character
		elif choice == 5:
			gameOver=True
			return gameOver
		else:
			"\nI'm sorry, that is not a valid choice.  Please try again..."
def store(character):
	choice = 0
	while choice < 1 or choice > 3:
		print"""\n\n\t\t\tSTORE MENU:
		1) Buy items
		2) Sell items
		3) Exit the store
		"""
		choice = input(">> ")
		if choice == 1:
		    userChoice = 0
		    while userChoice < 1 or userChoice > 6:
			print"""\n\n\t\t\tPURCHASE MENU:
			1) Melee Weaponry
			2) Ranged Weaponry
			3) Armor
			4) Accessories
			5) Items
			6) Cancel
			"""
			userChoice = input(">> ")
			store.purchaseStore(character, userChoice) 
			
	#####
###############
#################
##############
###############
###############
##############
###########THIS IS WHERE YOU LEFT OFF		
		elif choice ==2:
		    userChoice = 0
		    while userChoice < 1 or userChoice > 6:
			print"""\n\n\t\t\tSELL MENU:
			1) Melee Weaponry
			2) Ranged Weaponry
			3) Armor
			4) Accessories
			5) Items
			6) Cancel
			"""
			userChoice = input(">> ")
			if userChoice == 1:
				print "This functionality has not been added yet."
				#store.meleeSell(character)
			elif userChoice == 2:
				print "This functionality has not been added yet."
				#store.rangedSell(character)
			elif userChoice == 3:
				print "This functionality has not been added yet."
				#store.armorSell(character)
			elif userChoice == 4:
				print "This functionality has not been added yet."
				#store.accSell(character)
			elif userChoice == 5:
				print "This functionality has not been added yet."
				#store.itemSell(character)
			elif userChoice == 6:
				pass
			else:
				"\nI'm sorry, that is not a valid choice.Please try again..."
def title():
	print"""\n\n\t\t    WELCOME TO...\n\n
	    @@   @      @      @@@   @@@@@@@@    @@@         @@      @@@@@@@
   	   @@   @@     @@     @@@    @@ @@ @@   @@@         @@@@    @@@@@@   
 	   @@@  @@     @@    @@     @  @@  @   @@         @@  @@    @@
	  @@@@@@@@     @@    @@@@      @@      @@@@       @@   @@   @@@@@@   
	@ @@@ @ @@     @@      @@@     @@        @@@      @@   @@   @@@  
	@@@@    @@     @@  @@@ @@@     @@@   @@@ @@@      @@   @@   @@   
	@@@     @@@  @@@   @@@@@@      @@@   @@@@@@        @@ @@    @@   
	 @       @@   @     @@@@      @@@@    @@@@          @@@    @@@@   

	          @@      @@@@@@     @@@@        @@     @@@@
	         @@@@     @@   @@     @@@@      @@@@    @@@@
	         @@ @@    @@  @@@     @@@@@     @@ @@    @@@
	        @@  @@    @@@@@       @@ @@    @@  @@    @@@
	        @@@@@@    @@  @@      @@ @@    @@@@@@    @@@
	      @ @@   @    @@   @@     @@ @@  @ @@  @@       
	      @@@@  @@    @@    @@    @@@@   @@@@  @@    @@@
	       @@   @@    @@    @@@  @@@      @@   @@    @@@
"""
	raw_input("\n\n\t\t...Press the enter key to continue")
	
