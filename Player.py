# By Pytel, Guly
import prompt
"""
Funkce hrace pro hru 2048.
"""

MOVE = ["w","a","s","d"]
DEBUG = False

class Player:
	
	#def __init__ (self):
	
	def Move (self):
		while True != False:
			key = prompt()
			if DEBUG:
				print(key)
			if key in MOVE:
				return key
			elif key == 'q':
				return key

"""
END
"""

"""
from prompt_toolkit import prompt
 
cmd = prompt("Command: ")
print("Entered: '{cmd}'".format(cmd=cmd))
"""