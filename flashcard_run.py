#Create a front page for Flashcard Gui, Justin Womack
#-*- coding: utf-8 -*-

import sys, random
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt


class Label(QtGui.QLabel):
	#class allows for a picture to be created in paint
	#thus allowing for picture to scale well when window shifts
    def __init__(self, img):
        super(Label, self).__init__()
        self.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.pixmap = QtGui.QPixmap(img)

    def paintEvent(self, event):
        size = self.size()
        painter = QtGui.QPainter(self)
        point = QtCore.QPoint(0,0)
        scaledPix = self.pixmap.scaled(size, Qt.KeepAspectRatio, transformMode = Qt.SmoothTransformation)
        painter.drawPixmap(point, scaledPix)

class Create_Flash(QtGui.QWidget):
	#designed to open page of app to create flash cards
	def __init__(self):
		super(Create_Flash, self).__init__()
		#Reset for changing pages in app
		self.new_window = None

		self.grid = QtGui.QGridLayout()
		self.setLayout(self.grid)

		#creates labels for lineEdits
		self.label_word = QtGui.QLabel('Word:')
		self.grid.addWidget(self.label_word, 1, 1, 1, 1)
		
		self.label_definition = QtGui.QLabel('Definition:')
		self.grid.addWidget(self.label_definition, 2, 1, 1, 1)

		#creates lineEdit to type word into
		self.word_le = QtGui.QLineEdit(self)
		self.grid.addWidget(self.word_le, 1, 2, 1, 3)
		
		self.definition_le = QtGui.QLineEdit(self)
		self.grid.addWidget(self.definition_le, 2, 2, 1, 3)

		self.btn1 = QtGui.QPushButton('Enter')
		#self.btn1.setMaximumWidth(100)
		self.grid.addWidget(self.btn1, 3, 2, 1, 1)

		self.btn2 = QtGui.QPushButton('Back')
		#self.btn.setMaximumWidth(100)
		self.grid.addWidget(self.btn2, 3, 3, 1, 1)

		self.btn3 = QtGui.QPushButton(u'á')
		self.grid.addWidget(self.btn3, 4, 1, 1, 1, Qt.AlignRight)
		self.btn3.setMaximumWidth(50)
		self.btn3.setMinimumWidth(50)

		self.btn4 = QtGui.QPushButton(u'é')
		self.grid.addWidget(self.btn4, 4, 2, 1, 1)

		self.btn5 = QtGui.QPushButton(u'í')
		self.grid.addWidget(self.btn5, 4, 3, 1, 1)

		self.btn6 = QtGui.QPushButton(u'ó')
		self.grid.addWidget(self.btn6, 4, 4, 1, 1)

		self.btn7 = QtGui.QPushButton(u'ú')
		self.grid.addWidget(self.btn7, 5, 1, 1, 1, QtCore.Qt.AlignRight)
		self.btn7.setMaximumWidth(50)
		self.btn7.setMinimumWidth(50)

		self.btn8 = QtGui.QPushButton(u'ñ')
		self.grid.addWidget(self.btn8, 5, 2, 1, 1)

		self.btn9 = QtGui.QPushButton(u'ü')
		self.grid.addWidget(self.btn9, 5, 3, 1, 1)

		self.btn10 = QtGui.QPushButton(u'¿')
		self.grid.addWidget(self.btn10, 5, 4, 1, 1)

		#creates text edit used to display list of wwords
		self.textEdit = QtGui.QTextEdit()
		self.textEdit.setReadOnly(True)
		self.grid.addWidget(self.textEdit, 1, 5, 5, 4)

		#when return is pressed on line edit, addWord fxn triggered
		self.word_le.returnPressed.connect(self.addWord)
		self.definition_le.returnPressed.connect(self.addDefinition)
		self.btn1.clicked.connect(self.addDefinition)
		self.btn2.clicked.connect(self.back_clicked)
		self.btn3.clicked.connect(self.accent_a)
		self.btn4.clicked.connect(self.accent_e)
		self.btn5.clicked.connect(self.accent_i)
		self.btn6.clicked.connect(self.accent_o)
		self.btn7.clicked.connect(self.accent_u)
		self.btn8.clicked.connect(self.accent_n)
		self.btn9.clicked.connect(self.accent_dot_u)
		self.btn10.clicked.connect(self.accent_question_mark)

		self.setWindowTitle(First_Window.text + '.txt')
		self.view_list()
		self.set_stylesheet()
		self.event = 1
		# self.word = self.word_le.text()
		# self.definition = self.definition_le.text()

	def accent_a(self):

		#if focus is on word line edit it places the accented character on the word edit line
		#the self event triggers the timing of where it is placed.
		#focus must be reset to the current line or it gets stuck on button and user must click back on line.
		if self.event == 1:
			self.word_le.insert(u'á')
			self.word_le.setFocus()

		if self.event == 2:
			self.definition_le.insert(u'á')
			self.definition_le.setFocus()

	def accent_e(self):

		if self.event == 1:
			self.word_le.insert(u'é')
			self.word_le.setFocus()

		if self.event == 2:
			self.definition_le.insert(u'é')
			self.definition_le.setFocus()

	def accent_i(self):

		if self.event == 1:
			self.word_le.insert(u'í')
			self.word_le.setFocus()

		if self.event == 2:
			self.definition_le.insert(u'í')
			self.definition_le.setFocus()

	def accent_o(self):

		if self.event == 1:
			self.word_le.insert(u'ó')
			self.word_le.setFocus()

		if self.event == 2:
			self.definition_le.insert(u'ó')
			self.definition_le.setFocus()

	def accent_u(self):

		if self.event == 1:
			self.word_le.insert(u'ú')
			self.word_le.setFocus()

		if self.event == 2:
			self.definition_le.insert(u'ú')
			self.definition_le.setFocus()

	def accent_n(self):

		if self.event == 1:
			self.word_le.insert(u'ñ')
			self.word_le.setFocus()

		if self.event == 2:
			self.definition_le.insert(u'ñ')
			self.definition_le.setFocus()

	def accent_dot_u(self):

		if self.event == 1:
			self.word_le.insert(u'ü')
			self.word_le.setFocus()

		if self.event == 2:
			self.definition_le.insert(u'ü')
			self.definition_le.setFocus()

	def accent_question_mark(self):

		if self.event == 1:
			self.word_le.insert(u'¿')
			self.word_le.setFocus()

		if self.event == 2:
			self.definition_le.insert(u'¿')
			self.definition_le.setFocus()

	def set_stylesheet(self):
		sheet = open('flashcard_style.css')
		sheet_read = sheet.read()
		self.setStyleSheet(sheet_read)
		sheet.close()
		
	def addWord(self):

		#adds word to list and saves to file
		self.word = self.word_le.text()

		#sets focus of computer to definition line edit, allowing for 
		#continous typing by pressing enter to change focus
		self.definition_le.setFocus()
		self.event = 2

	def addDefinition(self):

		if self.event == 1:
			self.addWord()

		elif self.event == 2:
			#adds and saves definition to list
			self.definition = self.definition_le.text()
			
			#clears both line edits and changes focus back to first
			self.definition_le.clear()
			self.word_le.clear()
			self.word_le.setFocus()

			#opens text, writes word and def, saves and closes
			new_document = open('%s' %First_Window.text + '.txt', 'a')
			new_document.write(self.word + ":" + self.definition + '\n')
			new_document.close()

			self.view_list()
			#resets variable in case continous enter is pressed only ':' appears
			self.word = ''
			self.event = 1

	def back_clicked(self):
		#Removes last word pair from word document

		new_document = open('%s' %First_Window.text + '.txt')
		lines = new_document.readlines()
		new_document.close()

		w = open('%s' %First_Window.text + '.txt','w')
		w.writelines([item for item in lines[:-1]])
		w.close()

		self.view_list()

		self.definition_le.clear()
		self.word_le.clear()
		self.word_le.setFocus()
		self.event = 1

	def view_list(self):
		#opens, reads document, clears from textedit and reprints updated list
		
		new_document = open('%s' %First_Window.text + '.txt')
		read_document = new_document.read()
		new_document.close()
		self.textEdit.clear()
		self.textEdit.append(read_document)

class Study_Flash(QtGui.QWidget):

	#Brings to app page to study flashcards
	#Some buttons are initally disabled to prevent user from using fxns that
	#can't be triggered yet

	def __init__(self):
		super(Study_Flash, self).__init__()
		self.new_window = None

		self.grid = QtGui.QGridLayout()
		self.setLayout(self.grid)
		self.words_right = []

		self.display_words = QtGui.QTextEdit('<br><br><br></br></br></br>Word')
		self.display_words.setAlignment(QtCore.Qt.AlignCenter)
		self.display_words.setStyleSheet('font-size: 20px')
		self.display_words.setReadOnly(True)
		self.grid.addWidget(self.display_words, 1, 1, 2, 4)

		self.display_definitions = QtGui.QTextEdit('<br><br><br></br></br></br>Definition')
		self.display_definitions.setStyleSheet('font-size: 20px')
		self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)
		self.display_definitions.setReadOnly(True)
		self.grid.addWidget(self.display_definitions, 1, 5, 2, 4)

		self.btn1 = QtGui.QPushButton('Correct', self)
		self.grid.addWidget(self.btn1, 4, 4, 1, 1)
		self.btn1.setObjectName('Correct_button')
		self.btn1.setEnabled(False)

		self.btn2 = QtGui.QPushButton('Incorrect', self)
		self.btn2.setObjectName('Incorrect_button')
		self.grid.addWidget(self.btn2, 4, 5, 1, 1)
		self.btn2.setEnabled(False)

		self.btn3 = QtGui.QPushButton('Back', self)
		self.grid.addWidget(self.btn3, 4, 6, 1, 1)
		self.btn3.setEnabled(False)

		#used to be btn5.  Combo box worked better and looked nicer for this.
		self.combo = QtGui.QComboBox(self)
		self.combo.addItem('Select from Options:')
		self.combo.addItem('5 Cards at a time')
		self.combo.addItem('10 Cards at a time')
		self.combo.addItem('All Cards')
		self.grid.addWidget(self.combo, 5, 3, 1, 2)

		self.btn4 = QtGui.QPushButton('Load', self)
		self.grid.addWidget(self.btn4, 5, 5, 1, 2)

		self.btn6 = QtGui.QPushButton('Directions', self)
		self.grid.addWidget(self.btn6, 5, 1, 1, 2)

		self.btn7 = QtGui.QPushButton('Start', self)
		self.grid.addWidget(self.btn7, 5, 7, 1, 2)
		self.btn7.setEnabled(False)

		self.btn8 = QtGui.QPushButton('Next', self)
		self.grid.addWidget(self.btn8, 4, 3, 1, 1)
		self.btn8.setEnabled(False)

		self.lcd_right = QtGui.QLCDNumber(self)
		#(have to set object name to specifically target in stylesheet with #'name')
		self.lcd_right.setObjectName("lcd_right")
		self.grid.addWidget(self.lcd_right, 4, 1, 1, 1)

		self.lcd_wrong = QtGui.QLCDNumber(self)
		self.lcd_wrong.setObjectName('lcd_wrong')
		self.grid.addWidget(self.lcd_wrong, 4, 2, 1, 1)

		self.lcd_left = QtGui.QLCDNumber(self)
		self.grid.addWidget(self.lcd_left, 4, 8, 1, 1)

		self.btn1.clicked.connect(self.correct)
		self.btn2.clicked.connect(self.wrong)
		self.btn3.clicked.connect(self.back)
		self.btn4.clicked.connect(self.load_file)
		self.combo.activated[str].connect(self.selected)
		self.btn6.clicked.connect(self.directions)
		self.btn7.clicked.connect(self.start_flash)
		self.btn8.clicked.connect(self.next) 

		self.setGeometry(800, 100, 700, 300)
		self.setWindowTitle("Study")
		self.set_stylesheet()

	# def showlcd(self):
	# 	text = len(self.words_right)
	# 	self.lcd.display(text)

	def set_stylesheet(self):
		sheet = open('flashcard_style.css')
		sheet_read = sheet.read()
		self.setStyleSheet(sheet_read)
		sheet.close()

	def keyPressEvent(self, e):

		#This section is coded such that keys are active only at certain times with the variable self.event
		#self.event = 2 is when word is displayed, 3 is after def is displayed and choice of right or wrong is needed
		#event 4 is after a choice has been made, event 1 is the creation of the dictionary for flashcards  (Has yet to need to be assigned to key.)
		if e.key() == QtCore.Qt.Key_Right:
			#arrow right key
			if self.event == 2 or self.event == 3 or self.event == 4:
				self.next()

		elif e.key() == QtCore.Qt.Key_Left:
			#arrow left key
			if self.event == 2 or self.event == 3 or self.event == 4:
				if self.check == False and self.i > 0:
					#this is a secondary check.  Stops back fxn from accessing list backwards list[-i]
					self.back()

		elif e.key() == QtCore.Qt.Key_Down:
			#arrow down key
			if self.event == 3:
				self.wrong()

		elif e.key() == QtCore.Qt.Key_Up:
			#arrow up key
			if self.event == 3:
				self.next()
	
	def selected(self, text):

		#places varible from combo box into self.items allowing for future choices to be made off of this choice
		self.items = text
		
	def directions(self):

		QtGui.QMessageBox.about(self, "Directions",

			'Load your file of flashcards that was created in Create Flashcards. <br><br></br></br>'
			'Select the Number of Flashcards you wished displayed at once. <br><br></br></br>'

			'Click start to begin.  Word will be displayed.  Click next to display definition. <br><br></br></br>'
			'Click the correct button if you got it right. <br><br></br></br>'
			'Click the "X" if you got it wrong. <br><br></br></br>'
			'Wrong cards will be stored and cycled through again. <br><br></br></br>'

			'The back function will go back one word:definition. <br><br></br></br>'
			'This is used in case you miscliked an answer. <br><br></br></br>'

			'The next button can be clicked after showing the definition to mean "Correct." <br><br></br></br>'

			'Good Luck with your Studying!')

	def next(self):

		if self.items == '5 Cards at a time':

			#starts function for combo box option '10 cards at a time'
			if self.i == len(self.words_5) and self.check == False:

				#most of this is the same as for combobox option "All Cards"
				#if explanation needed check the other combo box option below
				#most changes are explained in this combo box block, however
				self.words_5 = [x for x in self.words_5 if not x in self.words_right]
				self.definitions_5 = [x for x in self.definitions_5 if not x in self.definitions_right]

				self.total_words -= len(self.words_right)
				self.words_wrong = []
				self.definitions_wrong = []
				self.words_right = []
				self.words_wrong = []
				self.correct = []
				self.i = 0
				self.lcd_right.display(len(self.words_right))
				self.lcd_wrong.display(len(self.words_wrong))

				if len(self.words) == 0 and len(self.words_5) == 0:

					#if all cards are correct and all sets of 10 are finished, this is run, terminating program, displaying complete message
					self.display_definitions.clear()
					self.display_words.clear()
					self.display_words.append('<br><br><br></br></br></br>FlashCards Complete<br></br>Good Job!')
					self.display_words.setAlignment(QtCore.Qt.AlignCenter)
					self.display_definitions.append('<br><br><br></br></br></br>Press Start to redo current set<br></br>Press load to being new set')
					self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)

					self.btn1.setEnabled(False)
					self.btn2.setEnabled(False)
					self.btn3.setEnabled(False)
					self.btn8.setEnabled(False)
					self.combo.setEnabled(True)

				elif len(self.words_5) == 0:

					if len(self.words) >= 5:

						#if more than 10 words in list of total words left, then this slices the next ten to use
						self.words_5 = self.words[0:5]
						self.definitions_5 = self.definitions[0:5]

						del self.words[:5]
						del self.definitions[:5]

					else:

						#if less than 10 cards remaining, this will scoop up the rest of them and run them
						self.words_5 = self.words[0:len(self.words)]
						self.definitions_5 = self.definitions[0:len(self.definitions)]

						del self.words[:len(self.words)]
						del self.definitions[:len(self.definitions)]

					self.change_word_5()
					self.display_definitions.clear()
					
				else:

					#randomizes wrong words
					combined = zip(self.words_5, self.definitions_5)
					random.shuffle(combined)
					self.words_5[:], self.definitions_5[:] = zip(*combined)

					#beginning of new cycle displaying first word
					self.display_definitions.clear()
					self.display_words.clear()
					self.display_words.append('<br><br><br></br></br></br>' + self.words_5[self.i])
					self.display_words.setAlignment(QtCore.Qt.AlignCenter)			

			elif self.check == False:

				self.event = 3

				#Pressing button causes next word to be displayed.  Changes check to 'True'
				#so when 'next' button is pressed the next check, changing the word, is preformed
				self.display_definitions.append('<br><br><br></br></br></br>' + self.definitions_5[self.i])
				self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)
				self.check = True
				self.btn1.setEnabled(True)
				self.btn2.setEnabled(True)
				self.btn3.setEnabled(False)

			elif self.check == True:

				self.event = 4

				#Check ran after def shown.  Marks word pair right.
				self.correct.append(True)
				self.check = False
				# print(self.correct)

				self.words_right.append(self.words_5[self.i])
				self.definitions_right.append(self.definitions_5[self.i])
				# print('Words right: ', self.words_right)

				#placement of self.i is important.  Want to increase it after above lists are appended.
				self.i += 1
				self.btn1.setEnabled(False)
				self.btn2.setEnabled(False)
				self.btn3.setEnabled(True)

				#runs fxn to change word pair
				self.change_word_5()
				self.lcd_right.display(len(self.words_right))
				self.lcd_left.display(self.total_words - len(self.words_right))

		elif self.items == '10 Cards at a time':

			#starts function for combo box option '10 cards at a time'
			if self.i == len(self.words_10) and self.check == False:

				#most of this is the same as for combobox option "All Cards"
				#if explanation needed check the other combo box option below
				#most changes are explained in this combo box block, however
				self.words_10 = [x for x in self.words_10 if not x in self.words_right]
				self.definitions_10 = [x for x in self.definitions_10 if not x in self.definitions_right]

				self.total_words -= len(self.words_right)
				self.words_wrong = []
				self.definitions_wrong = []
				self.words_right = []
				self.words_wrong = []
				self.correct = []
				self.i = 0
				self.lcd_right.display(len(self.words_right))
				self.lcd_wrong.display(len(self.words_wrong))

				if len(self.words) == 0 and len(self.words_10) == 0:

					#if all cards are correct and all sets of 10 are finished, this is run, terminating program, displaying complete message
					self.display_definitions.clear()
					self.display_words.clear()
					self.display_words.append('<br><br><br></br></br></br>FlashCards Complete<br></br>Good Job!')
					self.display_words.setAlignment(QtCore.Qt.AlignCenter)
					self.display_definitions.append('<br><br><br></br></br></br>Press Start to redo current set<br></br>Press load to being new set')
					self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)

					self.btn1.setEnabled(False)
					self.btn2.setEnabled(False)
					self.btn3.setEnabled(False)
					self.btn8.setEnabled(False)
					self.combo.setEnabled(True)

				elif len(self.words_10) == 0:

					if len(self.words) >= 10:

						#if more than 10 words in list of total words left, then this slices the next ten to use
						self.words_10 = self.words[0:10]
						self.definitions_10 = self.definitions[0:10]

						del self.words[:10]
						del self.definitions[:10]

					else:

						#if less than 10 cards remaining, this will scoop up the rest of them and run them
						self.words_10 = self.words[0:len(self.words)]
						self.definitions_10 = self.definitions[0:len(self.definitions)]

						del self.words[:len(self.words)]
						del self.definitions[:len(self.definitions)]

					self.change_word_10()
					self.display_definitions.clear()
					
				else:

					#randomizes wrong words
					combined = zip(self.words_10, self.definitions_10)
					random.shuffle(combined)
					self.words_10[:], self.definitions_10[:] = zip(*combined)

					#beginning of new cycle displaying first word
					self.display_definitions.clear()
					self.display_words.clear()
					self.display_words.append('<br><br><br></br></br></br>' + self.words_10[self.i])
					self.display_words.setAlignment(QtCore.Qt.AlignCenter)			

			elif self.check == False:

				self.event = 3

				#Pressing button causes next word to be displayed.  Changes check to 'True'
				#so when 'next' button is pressed the next check, changing the word, is preformed
				self.display_definitions.append('<br><br><br></br></br></br>' + self.definitions_10[self.i])
				self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)
				self.check = True
				self.btn1.setEnabled(True)
				self.btn2.setEnabled(True)
				self.btn3.setEnabled(False)

			elif self.check == True:

				self.event = 4

				#Check ran after def shown.  Marks word pair right.
				self.correct.append(True)
				self.check = False
				# print(self.correct)

				self.words_right.append(self.words_10[self.i])
				self.definitions_right.append(self.definitions_10[self.i])
				# print('Words right: ', self.words_right)

				#placement of self.i is important.  Want to increase it after above lists are appended.
				self.i += 1
				self.btn1.setEnabled(False)
				self.btn2.setEnabled(False)
				self.btn3.setEnabled(True)

				#runs fxn to change word pair
				self.change_word_10()
				self.lcd_right.display(len(self.words_right))
				self.lcd_left.display(self.total_words - len(self.words_right))

		elif self.items == "All Cards":

			if self.i == len(self.words) and self.check == False:

				#run when all flash cards are cycled through.  Resets the self.words list
				#to include only the words that user got wrong.
				#self.check False is used so this is triggered at the right time  
				self.words = [x for x in self.words if not x in self.words_right]
				self.definitions = [x for x in self.definitions if not x in self.definitions_right]

				#resets variables for next loop of flashcard cycle.
				#self.correct stores a list of True and False used in the back fxn
				#total_words variable is used for lcd display calculations for remaining cards
				self.total_words -= len(self.words_right)
				self.words_right = []
				self.definitions_right = []
				self.words_wrong = []
				self.definitions_wrong = []
				self.correct = []
				self.i = 0

				if len(self.words) == 0:

							#if all cards are correct, this is run, terminating program, displaying complete message
							self.display_definitions.clear()
							self.display_words.clear()
							self.display_words.append('<br><br><br></br></br></br>FlashCards Complete<br></br>Good Job!')
							self.display_words.setAlignment(QtCore.Qt.AlignCenter)
							self.display_definitions.append('<br><br><br></br></br></br>Press Start to redo current set<br></br>Press load to being new set')
							self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)

							self.btn1.setEnabled(False)
							self.btn2.setEnabled(False)
							self.btn3.setEnabled(False)
							self.btn8.setEnabled(False)
							self.combo.setEnabled(True)

				else:

					#randomizes wrong words
					combined = zip(self.words, self.definitions)
					random.shuffle(combined)
					self.words[:], self.definitions[:] = zip(*combined)

					#beginning of new cycle displaying first word
					self.display_definitions.clear()
					self.display_words.clear()
					self.display_words.append('<br><br><br></br></br></br>' + self.words[self.i])
					self.display_words.setAlignment(QtCore.Qt.AlignCenter)
				
			elif self.check == False:

				self.event = 3

				#Pressing button causes next word to be displayed.  Changes check to 'True'
				#so when 'next' button is pressed the next check, changing the word, is preformed
				self.display_definitions.append('<br><br><br></br></br></br>' + self.definitions[self.i])
				self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)
				self.check = True
				self.btn1.setEnabled(True)
				self.btn2.setEnabled(True)
				self.btn3.setEnabled(False)


			elif self.check == True:

				self.event = 4

				#Check ran after def shown.  Marks word pair right.
				self.correct.append(True)
				self.check = False

				self.words_right.append(self.words[self.i])
				self.definitions_right.append(self.definitions[self.i])

				#placement of self.i is important.  Want to increase it after above lists are appended.
				self.i += 1
				self.btn1.setEnabled(False)
				self.btn2.setEnabled(False)
				self.btn3.setEnabled(True)

				#runs fxn to change word pair
				self.change_word()
				self.lcd_right.display(len(self.words_right))
				self.lcd_left.display(self.total_words - len(self.words_right))

	def change_word(self):
		self.event = 2

		if self.i == len(self.words):

			#creates list soley to read remaining cards to user before variables are wiped
			self.list_count = self.words
			self.list_count = [x for x in self.list_count if not x in self.words_right]
			
			#clears QTextEdit squares
			self.display_words.clear()
			self.display_definitions.clear()
			
			#Displays transition screen before restarting or finishing flashcards	
			self.display_words.append('<br></br><br></br><br></br>Done with round<br></br>Number of wrong cards: ' + str(len(self.list_count)))
			self.display_words.setAlignment(QtCore.Qt.AlignCenter)
			self.display_definitions.append('<br><br><br></br></br></br>Press Next to Continue')
			self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)
			
		else:

			#clears QTextEdits and displays next word in list
			self.display_words.clear()
			self.display_definitions.clear()
			self.display_words.append('<br><br><br></br></br></br>' + self.words[self.i])
			self.display_words.setAlignment(QtCore.Qt.AlignCenter)
	
	def change_word_5(self):

		self.event = 2

		if self.i == len(self.words_5):

			#creates list soley to read remaining cards to user before variables are wiped
			self.list_count = self.words_5
			self.list_count = [x for x in self.list_count if not x in self.words_right]
			
			#clears QTextEdit squares
			self.display_words.clear()
			self.display_definitions.clear()

			if len(self.words_wrong) != 0:

				self.display_words.append('<br><br><br></br></br></br>Recycling through wrong flashcards in current set of 5')
				self.display_words.setAlignment(QtCore.Qt.AlignCenter)
				self.display_definitions.append('<br><br><br></br></br></br>Press next to redo wrong ones')
				self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)

			elif len(self.words) > 5:

				#Displays transition screen before restarting or finishing flashcards	
				self.display_words.append('<br><br><br></br></br></br>Set of 5 complete<br></br>Good Job!')
				self.display_words.setAlignment(QtCore.Qt.AlignCenter)
				self.display_definitions.append('<br><br><br></br></br></br>Press next to move to next set of 5')
				self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)

			elif len(self.words) < 5 and len(self.words) != 0:

				#displays that its the last set of ten
				self.display_words.append('<br><br><br></br></br></br>Final set of 5')
				self.display_words.setAlignment(QtCore.Qt.AlignCenter)
				self.display_definitions.append('<br><br><br></br></br></br>Press next to move to final set')
				self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)

			else: 

				#displays message for flashcards complete
				self.next()
		else:

			#clears QTextEdits and displays next word in list
			self.display_words.clear()
			self.display_definitions.clear()
			self.display_words.append('<br><br><br></br></br></br>' + self.words_5[self.i])
			self.display_words.setAlignment(QtCore.Qt.AlignCenter)

	def change_word_10(self):

		self.event = 2

		if self.i == len(self.words_10):

			#creates list soley to read remaining cards to user before variables are wiped
			self.list_count = self.words_10
			self.list_count = [x for x in self.list_count if not x in self.words_right]
			
			#clears QTextEdit squares
			self.display_words.clear()
			self.display_definitions.clear()

			if len(self.words_wrong) != 0:

				self.display_words.append('<br><br><br></br></br></br>Recycling through wrong flashcards in current set of 10')
				self.display_words.setAlignment(QtCore.Qt.AlignCenter)
				self.display_definitions.append('<br><br><br></br></br></br>Press next to redo wrong ones')
				self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)

			elif len(self.words) > 10:

				#Displays transition screen before restarting or finishing flashcards	
				self.display_words.append('<br><br><br></br></br></br>Set of 10 complete<br></br>Good Job!')
				self.display_words.setAlignment(QtCore.Qt.AlignCenter)
				self.display_definitions.append('<br><br><br></br></br></br>Press next to move to next set of 10')
				self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)

			elif len(self.words) < 10 and len(self.words) != 0:

				#displays that its the last set of ten
				self.display_words.append('<br><br><br></br></br></br>Final set of 10')
				self.display_words.setAlignment(QtCore.Qt.AlignCenter)
				self.display_definitions.append('<br><br><br></br></br></br>Press next to move to final set')
				self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)

			else: 

				#displays message for flashcards complete
				self.next()
		else:

			#clears QTextEdits and displays next word in list
			self.display_words.clear()
			self.display_definitions.clear()
			self.display_words.append('<br><br><br></br></br></br>' + self.words_10[self.i])
			self.display_words.setAlignment(QtCore.Qt.AlignCenter)

	def correct(self):

		if self.items == '5 Cards at a time':

			#starts function for combo box option '10 cards at a time'
			if self.i == len(self.words_5) and self.check == False:

				#most of this is the same as for combobox option "All Cards"
				#if explanation needed check the other combo box option below
				#most changes are explained in this combo box block, however
				self.words_5 = [x for x in self.words_5 if not x in self.words_right]
				self.definitions_5 = [x for x in self.definitions_5 if not x in self.definitions_right]

				self.total_words -= len(self.words_right)
				self.words_wrong = []
				self.definitions_wrong = []
				self.words_right = []
				self.words_wrong = []
				self.correct = []
				self.i = 0
				self.lcd_right.display(len(self.words_right))
				self.lcd_wrong.display(len(self.words_wrong))

				if len(self.words) == 0 and len(self.words_5) == 0:

					#if all cards are correct and all sets of 10 are finished, this is run, terminating program, displaying complete message
					self.display_definitions.clear()
					self.display_words.clear()
					self.display_words.append('<br><br><br></br></br></br>FlashCards Complete<br></br>Good Job!')
					self.display_words.setAlignment(QtCore.Qt.AlignCenter)
					self.display_definitions.append('<br><br><br></br></br></br>Press Start to redo current set<br></br>Press load to being new set')
					self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)

					self.btn1.setEnabled(False)
					self.btn2.setEnabled(False)
					self.btn3.setEnabled(False)
					self.btn8.setEnabled(False)
					self.combo.setEnabled(True)

				elif len(self.words_5) == 0:

					if len(self.words) >= 5:

						#if more than 10 words in list of total words left, then this slices the next ten to use
						self.words_5 = self.words[0:5]
						self.definitions_5 = self.definitions[0:5]

						del self.words[:5]
						del self.definitions[:5]

					else:

						#if less than 10 cards remaining, this will scoop up the rest of them and run them
						self.words_5 = self.words[0:len(self.words)]
						self.definitions_5 = self.definitions[0:len(self.definitions)]

						del self.words[:len(self.words)]
						del self.definitions[:len(self.definitions)]

					self.change_word_5()
					self.display_definitions.clear()
					
				else:

					#randomizes wrong words
					combined = zip(self.words_5, self.definitions_5)
					random.shuffle(combined)
					self.words_5[:], self.definitions_5[:] = zip(*combined)

					#beginning of new cycle displaying first word
					self.display_definitions.clear()
					self.display_words.clear()
					self.display_words.append('<br><br><br></br></br></br>' + self.words_5[self.i])
					self.display_words.setAlignment(QtCore.Qt.AlignCenter)			


			elif self.check == True:

				self.event = 4

				#Check ran after def shown.  Marks word pair right.
				self.correct.append(True)
				self.check = False
				# print(self.correct)

				self.words_right.append(self.words_5[self.i])
				self.definitions_right.append(self.definitions_5[self.i])
				# print('Words right: ', self.words_right)

				#placement of self.i is important.  Want to increase it after above lists are appended.
				self.i += 1
				self.btn1.setEnabled(False)
				self.btn2.setEnabled(False)
				self.btn3.setEnabled(True)

				#runs fxn to change word pair
				self.change_word_5()
				self.lcd_right.display(len(self.words_right))
				self.lcd_left.display(self.total_words - len(self.words_right))

		elif self.items == '10 Cards at a time':

			#starts function for combo box option '10 cards at a time'
			if self.i ==len(self.words_10) and self.check == False:

				#most of this is the same as for combobox option "All Cards"
				#if explanation needed check the other combo box option below
				#most changes are explained in this combo box block, however
				self.words_10 = [x for x in self.words_10 if not x in self.words_right]
				self.definitions_10 = [x for x in self.definitions_10 if not x in self.definitions_right]

				self.words_wrong = []
				self.definitions_wrong = []
				self.words_right = []
				self.words_wrong = []
				self.correct = []
				self.i = 0

				if len(self.words) == 0 and len(self.words_10) == 0:

					#if all cards are correct and all sets of 10 are finished, this is run, terminating program, displaying complete message
					self.display_definitions.clear()
					self.display_words.clear()
					self.display_words.append('<br><br><br></br></br></br>FlashCards Complete<br></br>Good Job!')
					self.display_words.setAlignment(QtCore.Qt.AlignCenter)
					self.display_definitions.append('<br><br><br></br></br></br>Press Start to redo current set<br></br>Press load to being new set')
					self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)

					self.btn1.setEnabled(False)
					self.btn2.setEnabled(False)
					self.btn3.setEnabled(False)
					self.btn8.setEnabled(False)
					self.combo.setEnabled(True)

				elif len(self.words_10) == 0:

					if len(self.words) >= 10:

						#if more than 10 words in list of total words left, then this slices the next ten to use
						self.words_10 = self.words[0:10]
						self.definitions_10 = self.definitions[0:10]

						del self.words[:10]
						del self.definitions[:10]

					else:

						#if less than 10 cards remaining, this will scoop up the rest of them and run them
						self.words_10 = self.words[0:len(self.words)]
						self.definitions_10 = self.definitions[0:len(self.definitions)]

						del self.words[:len(self.words)]
						del self.definitions[:len(self.definitions)]

					self.change_word_10()
					self.total_words -= len(self.words_right)

				else:

					#randomizes wrong words
					combined = zip(self.words_10, self.definitions_10)
					random.shuffle(combined)
					self.words_10[:], self.definitions_10[:] = zip(*combined)

					#beginning of new cycle displaying first word
					self.display_definitions.clear()
					self.display_words.clear()
					self.display_words.append('<br><br><br></br></br></br>' + self.words_10[self.i])
					self.display_words.setAlignment(QtCore.Qt.AlignCenter)			

			elif self.check == True:

				self.event = 4

				#Check ran after def shown.  Marks word pair right.
				self.correct.append(True)
				self.check = False
				# print(self.correct)

				self.words_right.append(self.words_10[self.i])
				self.definitions_right.append(self.definitions_10[self.i])
				# print('Words right: ', self.words_right)

				#placement of self.i is important.  Want to increase it after above lists are appended.
				self.i += 1
				self.btn1.setEnabled(False)
				self.btn2.setEnabled(False)
				self.btn3.setEnabled(True)

				#runs fxn to change word pair
				self.change_word_10()
				self.lcd_right.display(len(self.words_right))
				self.lcd_left.display(self.total_words - len(self.words_right))

		elif self.items == "All Cards":

			if self.i == len(self.words) and self.check == False:

				#run when all flash cards are cycled through.  Resets the self.words list
				#to include only the words that user got wrong.
				#self.check False is used so this is triggered at the right time  
				self.words = [x for x in self.words if not x in self.words_right]
				self.definitions = [x for x in self.definitions if not x in self.definitions_right]

				#resets variables for next loop of flashcard cycle.
				#self.correct stores a list of True and False used in the back fxn
				total_words = total_words - len(words_right)
				self.words_right = []
				self.definitions_right = []
				self.words_wrong = []
				self.definitions_wrong = []
				self.correct = []
				self.i = 0

				if len(self.words) == 0:

							#if all cards are correct, this is run, terminating program, displaying complete message
							self.display_definitions.clear()
							self.display_words.clear()
							self.display_words.append('<br><br><br></br></br></br>FlashCards Complete<br></br>Good Job!')
							self.display_words.setAlignment(QtCore.Qt.AlignCenter)
							self.display_definitions.append('<br><br><br></br></br></br>Press Start to redo current set<br></br>Press load to being new set')
							self.display_definitions.setAlignment(QtCore.Qt.AlignCenter)

							self.btn1.setEnabled(False)
							self.btn2.setEnabled(False)
							self.btn3.setEnabled(False)
							self.btn8.setEnabled(False)
							self.combo.setEnabled(True)

				else:

					#randomizes wrong words
					combined = zip(self.words, self.definitions)
					random.shuffle(combined)
					self.words[:], self.definitions[:] = zip(*combined)

					#beginning of new cycle displaying first word
					self.display_definitions.clear()
					self.display_words.clear()
					self.display_words.append('<br><br><br></br></br></br>' + self.words[self.i])
					self.display_words.setAlignment(QtCore.Qt.AlignCenter)

			elif self.check == True:

				self.event = 4

				#Check ran after def shown.  Marks word pair right.
				self.correct.append(True)
				self.check = False

				self.words_right.append(self.words[self.i])
				self.definitions_right.append(self.definitions[self.i])

				#placement of self.i is important.  Want to increase it after above lists are appended.
				self.i += 1
				self.btn1.setEnabled(False)
				self.btn2.setEnabled(False)
				self.btn3.setEnabled(True)

				#runs fxn to change word pair
				self.change_word()
				self.lcd_right.display(len(self.words_right))
				self.lcd_left.display(self.total_words - len(self.words_right))

	def wrong(self):

		self.event = 4

		#appends wrong words to list wrong used for back fxn
		#ERRRORR using the wrong list maybe.  set if perhaps.  drawing from words
		#needs to draw from words_wrong.  if combobox 10 cards: .append(self.words_10)
		if self.items == '5 Cards at a time':
			self.words_wrong.append(self.words_5[self.i])
			self.definitions_wrong.append(self.words_5[self.i])
		if self.items == '10 Cards at a time':
			self.words_wrong.append(self.words_10[self.i])
			self.definitions_wrong.append(self.words_10[self.i])
		if self.items == 'All Cards':
			self.words_wrong.append(self.words[self.i])
			self.definitions_wrong.append(self.definitions[self.i])
		# print('Words wrong: ', self.words_wrong)

		#adds False to self.correct
		self.i +=1
		self.check = False
		self.correct.append(False)
		
		#runs fxn to change the word
		self.btn1.setEnabled(False)
		self.btn2.setEnabled(False)
		self.btn3.setEnabled(True)

		self.lcd_wrong.display(len(self.words_wrong))
		
		if self.items == 'All Cards':
			self.change_word()

		elif self.items == '10 Cards at a time':
			self.change_word_10()

		elif self.items == '5 Cards at a time':
			self.change_word_5()

	def load_file(self):

		#opens directory tree to select and file and stores file to a variable
		self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
		self.btn7.setEnabled(True)

	def start_flash(self):

		#set variables and initiate creation of flashcards
		self.i = 0
		self.check = False
		self.words_right = []
		self.definitions_right = []
		self.words_wrong = []
		self.definitions_wrong = []
		self.correct =[]
		self.btn8.setEnabled(True)
		self.create_flash_dictionary()
		self.total_words = len(self.words)
		self.lcd_left.display(self.total_words)
		#disable combo box while running program running.  Helps avoid errors of changing combo box mid combo
		self.combo.setEnabled(False)

		if self.items == '5 Cards at a time':

			self.words_5 = self.words[0:5]
			self.definitions_5 = self.definitions[0:5]
			del self.words[:5]
			del self.definitions[:5]

			self.event = 2

			self.display_definitions.clear()
			self.display_words.clear()
			self.display_words.append('<br><br><br></br></br></br>' + self.words_5[self.i])
			self.display_words.setAlignment(QtCore.Qt.AlignCenter)
			self.setFocus()

		if self.items == '10 Cards at a time':

			self.words_10 = self.words[0:10]
			self.definitions_10 = self.definitions[0:10]
			del self.words[:10]
			del self.definitions[:10]

			self.event = 2

			self.display_definitions.clear()
			self.display_words.clear()
			self.display_words.append('<br><br><br></br></br></br>' + self.words_10[self.i])
			self.display_words.setAlignment(QtCore.Qt.AlignCenter)
			self.setFocus()

		if self.items == 'All Cards':

			self.event = 2

			#Sets first word to display
			self.display_definitions.clear()
			self.display_words.clear()
			self.display_words.append('<br><br><br></br></br></br>' + self.words[self.i])
			self.display_words.setAlignment(QtCore.Qt.AlignCenter)
			#removes focus from combo box allowing for use of arrows right away
			self.setFocus()

	def create_flash_dictionary(self):

		self.event = 1

		d = {}
		with open(self.filename) as f:
			for line in f:
				splitLine = line.replace('\n', '').split(':')
				#removes returns and splits word at ':' creating lists out of the two sides of ':'
				d[splitLine[0]] = ",".join(splitLine[1:])
				#creates dictionary

		#creates lists form dictionary keys and values corresponding to words and definitions for flashcards
		self.words = list(d.keys())
		self.definitions = list(d.values())

		#zips list together, randomizes them, and unpacks them.  This randomizes order of flashcards.
		combined = zip(self.words, self.definitions)
		random.shuffle(combined)
		self.words[:], self.definitions[:] = zip(*combined)

	def back(self):

		self.event = 2

		if self.i > 0:
			#doesn't allow back button to be hit more than once.  
			#it shouldn't have to be hit more than once.
			#this helps avoiding the last button from reading the list backwards

			#setting self.i back one allows for the last flashcard to be displayed
			self.i -= 1

			#if the last flashpair was correct and back is clicked this will remove the pair from right list
			#if they were wrong no list appending neeeded
			
			if self.correct[self.i] == True:
				self.words_right.pop()
				self.definitions_right.pop()
				self.correct.pop()
				# print('Words right: ', self.words_right)
				# print(self.correct)

			elif self.correct[self.i] == False:
				self.words_wrong.pop()
				self.definitions_wrong.pop()
				self.correct.pop()
				# print('Words wrong: ', self.definitions_wrong)
				# print(self.correct)

			#clears QTextEdits and displays next word in list
			self.display_words.clear()
			self.display_definitions.clear()

			self.lcd_right.display(len(self.words_right))
			self.lcd_wrong.display(len(self.words_wrong))
			self.lcd_left.display(self.total_words - len(self.words_right))

			if self.items == 'All Cards':
				self.display_words.append('<br><br><br></br></br></br>' + self.words[self.i])

			elif self.items == '10 Cards at a time':
				self.display_words.append('<br><br><br></br></br></br>' + self.words_10[self.i])

			elif self.items == '5 Cards at a time':
				self.display_words.append('<br><br><br></br></br></br>' + self.words_5[self.i])

			self.display_words.setAlignment(QtCore.Qt.AlignCenter)

class First_Window(QtGui.QWidget):

	def __init__(self):
		super(First_Window, self).__init__()

		self.new_window = None
		# self.setStyleSheet('First_Window {background-color: blue}')

		#create grid layout
		self.grid = QtGui.QGridLayout()
		self.setLayout(self.grid)

		#Sets flashcard image to app on row2, col1, spanning all 3 col
		self.label = Label('flashcards.png')
		self.grid.addWidget(self.label, 2, 1, 1, 3)

		#creates 3 buttons, colored white, that link to fxns
		self.btn1 = QtGui.QPushButton('Create', self)
		#self.btn1.setStyleSheet('background-color: white')
		self.grid.addWidget(self.btn1, 3, 1)

		self.btn2 = QtGui.QPushButton('Directions', self)
		#self.btn2.setStyleSheet('background-color: white')
		self.grid.addWidget(self.btn2, 3, 2)

		self.btn3 = QtGui.QPushButton('Study', self)
		#self.btn3.setStyleSheet('background-color: white')
		self.grid.addWidget(self.btn3, 3, 3)

		#connects buttons to functions when clicked
		self.btn1.clicked.connect(self.createFlash)
		self.btn2.clicked.connect(self.directions)
		self.btn3.clicked.connect(self.studyFlash)

		#set window size and title.
		self.setGeometry(800, 100, 500, 400)
		self.setWindowTitle('Flashcards')
		self.set_stylesheet()

	def set_stylesheet(self):
		sheet = open('flashcard_style.css')
		sheet_read = sheet.read()
		self.setStyleSheet(sheet_read)
		sheet.close()

	def createFlash(self):

		Enter_file_name = QtGui.QInputDialog
		#Opens dialog text block with title being input2 and words displayed by text being input3
		First_Window.text, ok = Enter_file_name.getText(self, 'Create Flashcards', 
			'<Font color = #DCD8CF>Enter file name:</Font>')

		# QtGui.QInputDialog.setStyleSheet("QLineEdit {background-color: yellow; color: white}")

		if ok:
			#when ok is pressed, send to create_flash page and 
			#variable placed in lineEdit is stored
			#creates file for adding words and definitions 
			new_document = open('%s' %First_Window.text + '.txt', 'a')
			new_document.close()
			self.new_window = Create_Flash()
	 		self.new_window.show()
	 		
	def directions(self):

		QtGui.QMessageBox.about(self, "Directions",
			
			'<Font color = #DCD8CF>Click "Create" to create files of flashcrards. <br><br></br></br>'
			'When "Create" is clicked, a popup will ask for a filename.<br><br></br></br>'
			'If creating a new file, type the name of the flashcard set. <br><br></br></br>'
			'If you want to append an old file, type the name of that file. <br><br></br></br>'
			'(That file must be located in the same directory as this app) <br><br></br></br>'

			'Click study to load a flashcard set and enter display screen.</font>'
			)
		
	def studyFlash(self):

		#open window to study flashcards
		self.new_window = Study_Flash()
		self.new_window.show()

if __name__ == '__main__':
	app = QtGui.QApplication([])
	gui = First_Window()
	gui.show()
	app.exec_()