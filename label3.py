import typing
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QWidget

#define window 
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):#, parent: QWidget | None = ..., flags: WindowFlags | WindowType = ...) -> None: #initialized the class

        super().__init__() # giving access to the Qmainwindow
        #self.resize(1000,600)
        self.setMinimumSize(QtCore.QSize(800,400))
        #self.setMaximumSize(QtCore.QSize())
        self.main_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.setStyleSheet('background-color : red ')
        self.horizontal_layout = QtWidgets.QHBoxLayout(self.main_widget)
        self.label = QtWidgets.QLabel('Endevour',self.main_widget)
        self.label.setObjectName('Title_Label')
        self.label.setStyleSheet('color : white')

        self.frame = QtWidgets.QFrame(self.main_widget)
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setLineWidth(3)
        self.horizontal_layout.addWidget(self.frame)

        self.frame2 = QtWidgets.QFrame(self.main_widget)
        self.horizontal_layout.addWidget(self.frame2)
        self.frame2.setLineWidth(3)
        self.frame2.setFrameShape(QtWidgets.QFrame.Box)


#if  this is a top level Python script

if __name__ == '__main__' :
    app = QtWidgets.QApplication([]) #create an application
    app.setApplicationDisplayName('Endevour Team App!!')
    ui = MainWindow() #create window instance
    ui.show() #show window
    app.exec_() #start the event handling loop
