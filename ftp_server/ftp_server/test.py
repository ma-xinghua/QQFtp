import sys
from server import Ui_Dialog
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog


class mywindow(QtWidgets.QWidget, Ui_Dialog):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def button1(self):
        print ("button1")

    def button2(self):
        print ("button2")

    def button3(self):
        print ("button2")

    def start(self):
        print ("start")

    def close(self):
        print ("close")


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
