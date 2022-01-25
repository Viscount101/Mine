from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from boardGen import *

class window(QMainWindow):
	def __init__(self):
		super().__init__()
		
		
		#These attributes will be used to modify the window values
		self.wins = 0
		self.losses= 0
		self.gameState = -1
		self.moves = 0
		
		#this will represent the underlying model of the game
		self.game = gridSquare().create_board(10, 10, 10)
		
		#This will keep track of all the buttons in the grid
		self.buttons = []
		
		#these buttons and labels represent the data of wins, losses, etc.
		self.reset = QPushButton("Reset Game", self)
		self.winsLabel = QLabel("Wins: ", self)
		self.winsVal = QLabel(str(self.wins), self)
		self.lossesLabel = QLabel("Losses: ", self)
		self.lossVal = QLabel(str(self.losses), self)
		self.WLRatio = QLabel("Win/Loss Ratio: ", self)
		self.moveCount = QLabel("Moves: ", self)
		self.movesVal = QLabel(str(self.moves), self)
		if (self.losses == 0):
			self.WLVal = QLabel("0.00", self)
		else:
			self.WLVal = QLabel(str(self.wins/float(self.losses)), self)
		
  		
		# setting title
		self.setWindowTitle("Minesweeper")
		
		# setting geometry
		self.setGeometry(100, 100, 500, 550)
  
        	# calling UiComponents
		self.UiComponents()
  
	# method for widgets
	def UiComponents(self):
        
		# setting geometry of buttons and labels
		self.reset.setGeometry(0, 0, 90, 40)
		self.reset.setStyleSheet("background-color: Red;")
		self.reset.clicked.connect(lambda: self.resetGame())
		self.winsLabel.setGeometry(100, 0, 50, 40)
		self.winsVal.setGeometry(141, 0, 30, 40)
		self.lossesLabel.setGeometry(165, 0, 70, 40)
		self.lossVal.setGeometry(221, 0, 30, 40)
		self.WLRatio.setGeometry(251, 0, 110, 40)
		self.WLVal.setGeometry(361, 0, 50, 40)
		self.moveCount.setGeometry(411, 0, 50, 40)
		self.movesVal.setGeometry(471, 0, 50, 40)
		
		#set up grid and style as well as properties to complete the interface, ready to start a game
		for i in range(1, 11):
			for j in range(0, 10):
				val = QPushButton("", self)
				val.setFont(QFont('Consolas', 20))
				val.setGeometry(j * 50, i * 50, 50, 50)
				val.setStyleSheet("border : 1px solid black; background-color: Grey")
				val.setProperty("row", i-1)
				val.setProperty("col", j)
				val.clicked.connect(lambda: self.checkClicked(self))
				self.buttons.append(val)
	
	#clicked method for when we hit a button on the grid
	def checkClicked(self, event):
	
		#get the button and its properties
		clicked = self.sender()
		row = clicked.property("row")
		col = clicked.property("col")
		
		modifiers = QApplication.keyboardModifiers()
		if modifiers == Qt.ShiftModifier:
			if (clicked.text() == "🚩"):
				clicked.setStyleSheet("border : 1px solid black; background-color: Grey")
				clicked.setText("")
				clicked.setFont(QFont("Consolas", 20))
				return
			clicked.setStyleSheet("border : 1px solid black; background-color: Grey")
			clicked.setText("🚩")
			clicked.setFont(QFont("Consolas", 20))
			return
		
		#set the text on the button to what reveal returns and set the font
		clicked.setText(self.game[row][col].reveal(self.game[row][col]))
		clicked.setFont(QFont("Consolas", 20))
		
		#these checks will set the buttons according to adj bomb count or if its a mine
		if (self.game[row][col].reveal(self.game[row][col]) == "X"):
			clicked.setStyleSheet("border : 1px solid black; background-color: Grey")
			self.gameState = 0
			clicked.setText("💣")
		elif (self.game[row][col].reveal(self.game[row][col]) == "1"):
			clicked.setStyleSheet("border : 1px solid black; background-color: Grey; color: Black")
		elif (self.game[row][col].reveal(self.game[row][col]) == "2"):
			clicked.setStyleSheet("border : 1px solid black; background-color: Grey; color: Red")
		elif (self.game[row][col].reveal(self.game[row][col]) == "3"):
			clicked.setStyleSheet("border : 1px solid black; background-color: Grey; color: Green")
		elif (self.game[row][col].reveal(self.game[row][col]) == "4"):
			clicked.setStyleSheet("border : 1px solid black; background-color: Grey; color: Blue")	
		elif (self.game[row][col].reveal(self.game[row][col]) == "5"):
			clicked.setStyleSheet("border : 1px solid black; background-color: Grey; color: Yellow")
		elif (self.game[row][col].reveal(self.game[row][col]) == "6"):
			clicked.setStyleSheet("border : 1px solid black; background-color: Grey; color: Cyan")
		elif (self.game[row][col].reveal(self.game[row][col]) == "7"):
			clicked.setStyleSheet("border : 1px solid black; background-color: Grey; color: Magenta")
		elif (self.game[row][col].reveal(self.game[row][col]) == "8"):
			clicked.setStyleSheet("border : 1px solid black; background-color: Grey; color: Orange")
		
		#disable the button and update moves
		clicked.setEnabled(False)
		self.moves += 1
		self.movesVal.setText(str(self.moves))
		
		#if we have a win, change game state to a win and reveal all buttons
		if (self.moves == 90):
			self.gameState = 1
			self.revealAll()
			
		#if we hit a mine, change game state to a loss and reveal all buttons
		if (self.gameState == 0):
			self.gameState = 0
			self.revealAll()
	
	def revealAll(self):
		for button in self.buttons:
				row=button.property("row")
				col=button.property("col")
				button.setText(str(self.game[row][col].reveal(self.game[row][col])))
				if (self.game[row][col].reveal(self.game[row][col]) == "X"):
					button.setStyleSheet("border : 1px solid black; background-color: Grey")
					button.setText("💣")
				elif (self.game[row][col].reveal(self.game[row][col]) == "1"):
					button.setStyleSheet("border : 1px solid black; background-color: Grey; color: Black")
				elif (self.game[row][col].reveal(self.game[row][col]) == "2"):
					button.setStyleSheet("border : 1px solid black; background-color: Grey; color: Red")
				elif (self.game[row][col].reveal(self.game[row][col]) == "3"):
					button.setStyleSheet("border : 1px solid black; background-color: Grey; color: Green")
				elif (self.game[row][col].reveal(self.game[row][col]) == "4"):
					button.setStyleSheet("border : 1px solid black; background-color: Grey; color: Blue")	
				elif (self.game[row][col].reveal(self.game[row][col]) == "5"):
					button.setStyleSheet("border : 1px solid black; background-color: Grey; color: Yellow")
				elif (self.game[row][col].reveal(self.game[row][col]) == "6"):
					button.setStyleSheet("border : 1px solid black; background-color: Grey; color: Cyan")
				elif (self.game[row][col].reveal(self.game[row][col]) == "7"):
					button.setStyleSheet("border : 1px solid black; background-color: Grey; color: Magenta")
				elif (self.game[row][col].reveal(self.game[row][col]) == "8"):
					button.setStyleSheet("border : 1px solid black; background-color: Grey; color: Orange")
				button.setEnabled(False)
		self.endGame()
	
	#resets the game if the reset button is hit
	def resetGame(self):
		
		#for all buttons, reset them to unknowns, generate a new board, and make them clickable again.
		for button in self.buttons:
			button.setStyleSheet("border : 1px solid black; background-color: Grey")
			button.setText("")
			button.setEnabled(True)
		self.moves = 0
		self.movesVal.setText(str(self.moves))
		self.game = gridSquare().create_board(10, 10, 10)
		
		#if game was in progress, count as a loss
		if (self.gameState == -1):
			self.losses += 1
		
		#update wins and losses
		self.winsVal.setText(str(self.wins))
		self.lossVal.setText(str(self.losses))
		
		#reset game state
		self.gameState = -1
		
		#update win loss ratio
		if (self.losses == 0):
			self.WLVal.setText(str("%.2f" % float(self.wins)))
		else:
			self.WLVal.setText(str("%.2f" % float(self.wins/self.losses)))
		
	#updates wins and losses for labels		
	def endGame(self):
		if (self.gameState == 1):
			self.wins += 1
		else:
			self.losses += 1
						
					
		
	
	

