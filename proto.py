import sys

from PyQt4 import QtCore, QtGui, uic


class MyWindow(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = uic.loadUi("proto.ui")
        
        self.connect(self.ui.radioYes, QtCore.SIGNAL("toggled(bool)"), self.add_car)
        self.connect(self.ui.car_button, QtCore.SIGNAL("clicked()"), self.add_car)
        
        

        
        self.ui.show()


        self.count = 0


    def reacttoradio(self):    
        self.ui.labelReaction.setText(kukkuu)
        print self.ui.labelReaction.text()    
    
    def add_car(self):
        self.count += 1
        self.ui.car_count.setText(str(self.count))
        print self.ui.palaute.toPlainText()


#Get information from the system




app = QtGui.QApplication(sys.argv)
window = MyWindow()
app.exec_()
