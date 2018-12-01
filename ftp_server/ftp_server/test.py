import sys
from server import Ui_Dialog_server
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
from create import *
from ftp_server import *
from change import *

class createwindow(QtWidgets.QWidget, Ui_Dialog_create):
    def __init__(self):
        super(createwindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def create(self):
        print ("hahahanima")

class changewindow(QtWidgets.QWidget, Ui_Dialog_change):
    def __init__(self):
        super(changewindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def change(self):
        self.userName=self.lineEdit.text()
        self.userPasscode=self.lineEdit_2.text()
        self.data = ''
        self.array=[]
        file = open('userinfo.ini','r',encoding = 'UTF-8')
        self.information=file.readlines()
        file.close()
        file_new=open('userinfo.ini','w',encoding='UTF-8')
        for line in self.information:
                self.array= line.split()
                if((self.userName in self.array) and (self.userPasscode in self.array)):
                    if(self.checkBox.isChecked()):
                        self.array[0]=self.lineEdit_3.text()
                    if(self.checkBox_2.isChecked()):
                        self.array[1]=self.lineEdit_4.text()
                    if(self.checkBox_3.isChecked()):
                        self.authority=""
                        if (self.checkBox_5.isChecked()):
                            self.authority=self.authority+"e"
                        if (self.checkBox_6.isChecked()):
                            self.authority=self.authority+"l"
                        if (self.checkBox_7.isChecked()):
                            self.authority=self.authority+"r"
                        if (self.checkBox_8.isChecked()):
                            self.authority=self.authority+"d"
                        if (self.checkBox_9.isChecked()):
                            self.authority=self.authority+"a"
                        if (self.checkBox_10.isChecked()):
                            self.authority=self.authority+"m"
                        if (self.checkBox_11.isChecked()):
                            self.authority=self.authority+"f"
                        if (self.checkBox_12.isChecked()):
                            self.authority=self.authority+"w"
                        self.array[2]=self.authority
                    if(self.checkBox_4.isChecked()):
                        self.array[3]=self.lineEdit_5.text()
                    #print(self.array[0])
                    #print(self.array[1])
                    #print(self.array[2])
                    #print(self.array[3])
                    self.data=self.array[0]+" "+self.array[1]+" "+self.array[2]+" "+self.array[3]+"\n"
                    line=self.data
                file_new.write(line)
        file_new.close()

class mywindow(QtWidgets.QWidget, Ui_Dialog_server):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def newuser(self):
         self.create_app = QtWidgets.QApplication(sys.argv)
         self.create_show = createwindow()
         self.create_show.show()
       

    def changeuser(self):
         self.change_app = QtWidgets.QApplication(sys.argv)
         self.change_show = changewindow()
         self.change_show.show()

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
    
    
