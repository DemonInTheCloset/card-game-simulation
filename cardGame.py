from random import shuffle
import sys

## Print function to use the \r character, useful for printing progress bars and progress percentages
def writeInLine(string):
	sys.stdout.write("\r" + str(string))
	sys.stdout.flush()

## Card Pile class (FIFO list) 
class Pile
	## Initialize object
	def __init__(self,cards):
		# Add the cards
		self.__cards = cards
		
		# If nothing is provided, set to empty list
		if self.__cards == None:
			self.__cards = list()
			
		# Set the topCard
		self.__update()
	
	## Update the topCard
	def __update(self):
		# If not empty update the topCard
		if ( not self.empty() ) and ( self.__cards[0] != self.topCard ):
			try:
				self.topCard = cards[0]
			except Exception as e:
				print(e)
		# If empty set topCardto None
		elif ( self.empty() and self.topCard() != None ):
			self.topCard = None
	
	## Check if pile is empty
	def empty(self):
		if not self.__cards:
			return True
	
	## Pop the topCard out
	def pop(self):
		card = self.__cards.pop(0)
		self.__update()
		return card
		
	## Add a card
	def add(self,card):
		if self.empty():
			self.__cards = [card]
			self.topCard = card
			
		else:
			raise PileNotEmpty("The pile wasn't empty when it tried to be modified")

## Player Class
class Player
	def __init__(self, cards):
		if len(cards) < 28:
			raise IndexError("The Player was provided with too few cards",len(cards))
		
