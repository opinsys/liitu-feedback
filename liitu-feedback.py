import sys
import datetime  # to get current date
import socket  # to get the hostname
import urllib  # for the http post request
import urllib2 # for the http post request
import commands # to execute whoami to get username information

# All the QT gui stuff
from PyQt4 import QtCore, QtGui, uic


class MyWindow(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

# Load the UI-file created with QT designer
        self.ui = uic.loadUi("liitu-feedback.ui")

        # Create QButtonGroup for the radiobuttons
        bg = self.buttongroup = QtGui.QButtonGroup()
        # Add buttons to the group
        bg.addButton(self.ui.radio1, 1)
        bg.addButton(self.ui.radio2, 2)
        bg.addButton(self.ui.radio3, 3)
        bg.addButton(self.ui.radio4, 4)

        # When Send button is clicked, execute the sendPostRequestToServer function
        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.sendPostRequestToServer)
        
        self.ui.show()
 
        # Get all the necessary information from the current user, hostname and time       
        self.hostname=socket.gethostname()
        (self.a,self.username) = commands.getstatusoutput('whoami')
        #username=os.system("whoami")
        self.date = datetime.datetime.now()

    # Executed when Send button is clicked
    def sendPostRequestToServer(self):
        print self.buttongroup.checkedButton()
        print self.ui.plainTextEdit.toPlainText()

        # HTTP Post to defined url
        query_args = { 'username':str(self.username), 'hostname':str(self.hostname), 'date':str(self.date), 'feedback':self.ui.plainTextEdit.toPlainText(), 'value':str(self.buttongroup.checkedButton)}
        encoded_args = urllib.urlencode(query_args)
        url = 'http://localhost:4567/'
        print urllib2.urlopen(url, encoded_args).read()    


app = QtGui.QApplication(sys.argv)
window = MyWindow()
app.exec_()
