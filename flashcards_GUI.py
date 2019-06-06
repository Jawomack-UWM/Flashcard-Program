#Create a front page for Flashcard Gui


import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class Label(QtGui.QLabel):
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



class First_Window(QtGui.QWidget):

	def __init__(self):
		super(First_Window, self).__init__()

		self.initUI()

	def initUI(self):

		# w = QtGui.QMainWindow()
		self.setStyleSheet('QWidget {background-color: blue}')


		grid = QtGui.QGridLayout()
		self.setLayout(grid)

		label = Label('flashcards.png')
		grid.addWidget(label, 2, 1, 1, 3)


		btn1 = QtGui.QPushButton('Create', self)
		btn1.setStyleSheet('background-color: white')

		grid.addWidget(btn1, 3, 1)

		btn2 = QtGui.QPushButton('Path', self)
		btn2.setStyleSheet('background-color: white')
		grid.addWidget(btn2, 3, 2)

		btn3 = QtGui.QPushButton('Study', self)
		btn3.setStyleSheet('background-color: white')
		grid.addWidget(btn3, 3, 3)
		

		# btn1.clicked.connect(self.createFlash)
		# btn2.clicked.connect(self.openFlash)
		# btn3.clicked.connect(self.studyFlash)

		self.setGeometry(300, 300, 500, 400)
		self.setWindowTitle('Flashcards')
		self.show()

	def createFlash(self):
		#open window to create flash cards
		pass

	def openFlash(self):
		#store value to load in study cards
		pass

	def studyFlash(self):
		#open window to study flashcards
		pass

def main():

	app = QtGui.QApplication(sys.argv)
	start_screen = First_Window()	
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()