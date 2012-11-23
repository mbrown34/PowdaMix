"""
Created on November 10, 2012

@author Matthew
"""
import generate
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
			character.displayInfo()
		elif choice == 2:
			print
			#character= generate.Player.load()
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
			print
			#store(character)
		elif choice == 2:
			print
			#battle(character)
		elif choice == 3:
			character.displayEquip()
			character.displayInfo()
		elif choice == 4:
			print
			#save character
		elif choice == 5:
			gameOver=True
			return gameOver
		else:
			"\nI'm sorry, that is not a valid choice.  Please try again..."
def store(character):
	choice = 0:
	while choice < 1 or choice > 3:
		print"""\n\n\t\t\tSTORE MENU:
		1) Buy items
		2) Sell items
		3) Exit the store
		"""
		if choice == 1:
		    userChoice=0
		    while userChoice < 1 or userChoice > 5:
			"""\n\n\t\t\tPURCHASE MENU:
			1) Melee Weaponry
			2) Ranged Weaponry
			3) Armor
			4) Items
			5) Cancel
			"""
		userChoice = input(">> ")
def title():
	print"""\n\n\t\t\t    WELCOME TO...\n\n
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
	
