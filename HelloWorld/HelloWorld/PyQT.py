
# from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtWidgets,QtCore 
from QTGUI import Ui_MainWindow     
from AboutGUI import Ui_AboutDialog

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent=parent)  
        self.setupUi(self)
        self.child=ChildrenForm()

        self.actionAbout.triggered.connect(self.childShow)

    def childShow(self):  
#        self.MaingridLayout.addWidget(self.child)      
        self.child.setModal(True)
        self.child.show()

class ChildrenForm(QtWidgets.QDialog,Ui_AboutDialog):  
    def __init__(self,parent=MainWindow):  
        super(ChildrenForm,self).__init__()  
        self.setupUi(self)  
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)    #Disable WhatsThis button
        
if __name__=="__main__":  
    import sys   
    app=QtWidgets.QApplication(sys.argv)  
    myshow=MainWindow()  
    myshow.show()  
    sys.exit(app.exec_())  

