# By Pytel, Guly
import curses
"""
Funkce hrace pro hru 2048.
"""

MOVE = ["w","a","s","d"]
DEBUG = False

class Player:
	
	#def __init__ (self):
	
	def Move (self):
		while True != False:
			key = curses.initscr()
			if DEBUG:
				print(key)
			if key in MOVE:
				return key
			elif key == 'q':
				return key

"""
END

import sys
import termios
import tty
fd = sys.stdin.fileno()
old = termios.tcgetattr(fd)
tty.setcbreak(fd)
try:
	print 'Stiskni q pro konec'
	ch = sys.stdin.read(1)
	while ch <> 'q':
		print 'To nebylo ono'
		ch = sys.stdin.read(1)
finally:
	termios.tcsetattr(fd, termios.TCSAFLUSH, old)

	OR

	import curses
stdscr = curses.initscr()
try:
	stdscr.scrollok(True)
	curses.noecho()
	curses.cbreak()

	stdscr.addstr('Stiskni q pro konec\n')
	ch = stdscr.getch()
	while ch <> ord('q'):
		stdscr.addstr('To nebylo ono\n')
		ch = stdscr.getch()
	
finally:
	curses.nocbreak()
	curses.echo()
	curses.endwin()
"""