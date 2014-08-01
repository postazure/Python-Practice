import sys
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("tempconv_menu.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btnCtoF.clicked.connect(self.btn_CtoF_clicked)
        self.btnFtoC.clicked.connect(self.btn_FtoC_clicked)
        self.actionCtoF.triggered.connect(self.btn_CtoF_clicked)
        self.actionFtoC.triggered.connect(self.btn_FtoC_clicked)
        self.actionExit.triggered.connect(self.menuExit_selected)
        
    def btn_CtoF_clicked(self):
        cel = float(self.editCel.text())
        fahr = cel * 9.0 / 5 +32
        self.spinFahr.setValue(int(fahr +.5))

    def btn_FtoC_clicked(self):
        fahr = self.spinFahr.value()
        cel = (fahr - 32) * 5.0 / 9
        cel_text = '%.2f' % cel
        self.editCel.setText(str(cel_text))

    def menuExit_selected(self):
        self.close()
#this is for you GitHub

app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.show()

app.exec_()


#fahr = cel * 9.0 / 5 + 32
