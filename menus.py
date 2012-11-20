"""
Created on November 10, 2012

@author Matthew
"""
import generate
def main():
	title()
	choice = 0
	gameOver = False
	while choice < 1 or choice > 6 or gameOver != True:
		print"""\n\n\t\t\tMAIN MENU:
		1) Create your player
		2) Enter the Equipment Store
		3) Enter the Battle Square	
		4) Check Equipment
		5) Save current character and inventory status
		6) Exit the game
		"""
		choice=input(">> ")
		if choice == 1:
			print
			character=generate.Player()
			character.displayEquip()
			character.displayInfo()
		elif choice == 2:
			print
			#equip.store()
		elif choice == 3:
			print			
			#world.battle()
		elif choice == 4:
			print
		elif choice == 5:
			print
		elif choice == 6:
			gameOver=True
			return gameOver
		else:
			print"\n\nThat is not a valid input choice. Please try again..."
			
def title():
	print"""\n\n\t\t\t    WELCOME TO...\n\n
	    @@   @       @       @@@   @@@@@@@@     @@@         @@      @@@@@@@
   	   @@   @@      @@      @@@    @@ @@ @@    @@@         @@@@    @@@@@@   
 	   @@@  @@      @@     @@     @  @@  @    @@         @@  @@    @@
	  @@@@@@@@      @@     @@@@      @@       @@@@       @@   @@   @@@@@@   
	@ @@@ @ @@      @@       @@@     @@         @@@      @@   @@   @@@  
	@@@@    @@      @@   @@@ @@@     @@@    @@@ @@@      @@   @@   @@   
	@@@     @@@   @@@    @@@@@@      @@@    @@@@@@        @@ @@    @@   
	 @       @@    @      @@@@      @@@@     @@@@          @@@    @@@@   

	          @@      @@@@@@      @@@@         @@     @@@@
	         @@@@     @@   @@      @@@@       @@@@    @@@@
	         @@ @@    @@  @@@      @@@@@      @@ @@    @@@
	        @@  @@    @@@@@        @@ @@     @@  @@    @@@
	        @@@@@@    @@  @@       @@ @@     @@@@@@    @@@
	      @ @@   @    @@   @@      @@ @@   @ @@  @@       
	      @@@@  @@    @@    @@     @@@@    @@@@  @@    @@@
	       @@   @@    @@    @@@   @@@       @@   @@    @@@
"""
	raw_input("\n\n\t\t...Press the enter key to continue")
	
