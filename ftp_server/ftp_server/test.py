import sys
from server import Ui_Dialog_server
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
from create import *
from ftp_server import *

class createwindow(QtWidgets.QWidget, Ui_Dialog_create):
    def __init__(self):
        super(createwindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def create(self):
        print ("hahahanima")

class mywindow(QtWidgets.QWidget, Ui_Dialog_server):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def newuser(self):
         self.create_app = QtWidgets.QApplication(sys.argv)
         self.create_show = createwindow()
         self.create_show.show()
       

    def button2(self):
        print ("button2")

    def button3(self):
        print ("button2")

    def start(self):
        self.close()
        ftp()
        
    
    
    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
    
    