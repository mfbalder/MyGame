import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
######################

GAME_WIDTH = 8
GAME_HEIGHT = 8

#### Put class definitions here ####
class Block(GameElement):
	IMAGE = 'WoodBlock'
	SOLID = True

class Gem(GameElement):
	SOLID = False

class BlueGem(Gem):
	IMAGE = "BlueGem"

class OrangeGem(Gem):
	IMAGE = "OrangeGem"

	def interact(self, player):
		player.POWER += 100

class Heart(GameElement):
	IMAGE = "Heart"

	def interact(self, player):
		"""When player interacts with heart, orange gem is deleted, player gains power"""
		self.board.draw_msg("You've gained power, but lost a gem!")
		self.board.del_el(6,7)
		player.POWER += 10

class Character(GameElement):
	IMAGE = "Princess"
	POWER = 0

	def next_pos(self, direction):
		"""returns our next set of coordinates, based on the direction we're heading"""
		if direction == "up":
			return (self.x, self.y - 1)
		elif direction == "down":
			return (self.x, self.y + 1)
		elif direction == "right":
			return (self.x + 1, self.y)
		elif direction == "left":
			return (self.x - 1, self.y)
		return None

	def keyboard_handler(self, symbol, modifier):
		direction = None

		# detects what key is being pressed, sets it to the variable 'direction'
		if symbol == key.UP:
			direction = "up"
		elif symbol == key.DOWN:
			direction = "down"
		elif symbol == key.RIGHT:
			direction = "right"
		elif symbol == key.LEFT:
			direction = "left"
		elif symbol == key.Q:
			sys.exit()

		# if a specified key has been pressed, get the next coordinates, delete the player where they currently are
		# and move them to their new location	
		if direction:
			next_location = self.next_pos(direction)
			next_x = next_location[0]
			next_y = next_location[1]

			next_item = self.board.get_el(next_x, next_y)
			if next_item:
				next_item.interact(self)

			self.board.del_el(self.x,self.y)
			self.board.set_el(next_x, next_y, self)




####   End class definitions    ####

def initialize():
    """Put game initialization code here"""

    block_objects = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), 
    	(0,2), (1, 2), (2, 2), (3, 2), (4,2), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7)
    	]
    for pos in block_objects:
    	block = Block()
    	GAME_BOARD.register(block)
    	GAME_BOARD.set_el(pos[0], pos[1], block)

    bluegem = BlueGem()
    GAME_BOARD.register(bluegem)
    GAME_BOARD.set_el(1, 1, bluegem)

    orangegem = OrangeGem()
    GAME_BOARD.register(orangegem)
    GAME_BOARD.set_el(6, 7, orangegem)

    player = Character()
    GAME_BOARD.register(player)
    GAME_BOARD.set_el(6,1, player)

    heart = Heart()
    GAME_BOARD.register(heart)
    GAME_BOARD.set_el(6, 2, heart)

    GAME_BOARD.draw_msg("Use the arrow keys to move the princess through the game. Can you win in only 10 moves?")

