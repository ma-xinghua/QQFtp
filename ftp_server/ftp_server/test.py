import sys
import os
from server import Ui_Dialog_server
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from create import *
from ftp_server import *

class createwindow(QtWidgets.QWidget, Ui_Dialog_create):
    def __init__(self):
        super(createwindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def create(self):
        self.userName=self.lineEdit.text()
        self.userPasscode=self.lineEdit_2.text()
        self.userPasscodeAgain=self.lineEdit_3.text()
        self.Docupass=self.lineEdit_4.text()
        #print (self.userName)
        #print (self.userPasscode)
        #print (self.userPasscodeAgain)
        #print (self.Docupass)
        self.authority=""
        if (self.checkBox.isChecked()):
            self.authority=self.authority+"e"
        if (self.checkBox_2.isChecked()):
            self.authority=self.authority+"l"
        if (self.checkBox_3.isChecked()):
            self.authority=self.authority+"r"
        if (self.checkBox_4.isChecked()):
            self.authority=self.authority+"d"
        if (self.checkBox_5.isChecked()):
            self.authority=self.authority+"a"
        if (self.checkBox_6.isChecked()):
            self.authority=self.authority+"m"
        if (self.checkBox_7.isChecked()):
            self.authority=self.authority+"f"
        if (self.checkBox_8.isChecked()):
            self.authority=self.authority+"w"
        #print (self.authority)
        if (self.userName==""):
            warning3=QMessageBox.warning(self,"警告","用户名不能为空")
            return
        if (self.userPasscode!=self.userPasscodeAgain):
            warning1=QMessageBox.warning(self,"警告","两次输入密码不一致")
            return
        if (self.authority==""):
            warning2=QMessageBox.warning(self,"警告","必须选择一个权限")
            return
        if not os.path.exists(self.Docupass):
               os.makedirs(self.Docupass) #如果不存在这个文件夹，就创建一个
        file = open('userinfo.ini', 'a')
        self.word = '\n'+self.userName+' '+self.userPasscode+' '+self.authority+' '+self.Docupass
        file.write(self.word)
        file.close()
        information=QMessageBox.information(self,"提示","新用户成功创建")

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
    
    