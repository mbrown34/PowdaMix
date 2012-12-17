"""
Created on November 10, 2012

@author Matthew
"""
import generate
import enemy
import store
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
			load = False
			print
			character=generate.Player(load)
			character.displayEquipped()
			character.displayInventory()
			character.displayItems()
			character.displayInfo()
			character.displaySpells()
		elif choice == 2: 
			print "This functionality has not been added yet."
			#load = True
			#character= generate.load(load)
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
	while choice < 1 or choice > 6 or gameOver != True:
		print"""\n\n\t\t\tMAIN MENU:
		1) Enter the item and equipment shop
		2) Combat foes in the battle square
		3) View your current character information
		4) Manage your Inventory and Equipment
		5) Save your current inventory and status
		6) Exit the game
		"""
		choice = input(">> ")
		if choice == 1:
			shop(character)
		elif choice == 2:
			print "This functionality has not been fully implemented yet."
			villain=enemy.Enemy()
			villain.printInfo()
		elif choice == 3:
			character.displayInfo()
			character.displaySpells()
		elif choice == 4:
			character.manageInventory()
		elif choice == 5:
			print "This functionality has not been added yet."
			#save character
		elif choice == 6:
			gameOver=True
			return gameOver
		elif gameOver==True:
			overScreen()
		else:
			"\nI'm sorry, that is not a valid choice.  Please try again..."
def shop(character):
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
			store.sellStore(character, userChoice)
		elif choice ==3:
			pass
		else:
			print "I'm sorry, but that is not a valid entry. Please try again."
def title():
	print"""\n\n\t\t        WELCOME TO...\n\n
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
	      @@@@  @@    @@   @@     @@@@   @@@@  @@    @@@
	       @@   @@    @    @     @@@      @@   @@    @@@
"""
	raw_input("\n\n\t\t\t...Press the enter key to continue")

def overScreen():
	print"""\n\n\n\t\t     YOU WERE DEFEATED...\n\n
                     @@@@@       @@        @@   @    @@@@@@    
                   @@@  @@@     @@@@      @@   @@   @@@  @@@   
                  @@@           @@ @@     @@@  @@   @@         
                  @@@  @@@@@   @@  @@    @@@@@@@@   @@ @@@    
                  @@@  @@@@@   @@@@@@  @ @@@ @ @@   @@@@@     
                   @@@   @@  @ @@   @  @@@@    @@   @@@    @@@
                    @@@@@@   @@@@  @@  @@@     @@@   @@@@@@@@ 
                      @@      @@   @@   @       @@     @@@@   
	
                        @@     @  @@    @@@@@@    @@@@@@ 
                       @@@@   @    @@  @@@  @@@   @@   @@
                     @@  @@  @@    @@@ @@         @@  @@@
                     @@   @@ @@    @@@ @@ @@@     @@@@@ 
                     @@   @@ @@@   @@@ @@@@@      @@  @@ 
                     @@   @@ @@@  @@@  @@@   @@@  @@   @@
                      @@ @@   @@@@@@    @@@@@@@@  @@   @@ 
                       @@@     @@@        @@@@    @    @  
"""

