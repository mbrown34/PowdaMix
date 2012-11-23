"""
Created on November 10, 2012


@author Matthew
"""

import menus
import sys

gameOver = False

while gameOver != True:
	gameOver = menus.start()
#simple loop to continue game execution while a value is not returned to the menus.main()
#indicating that the game should be terminated.
