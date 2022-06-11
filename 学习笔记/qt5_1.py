import sys
from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QLineEdit,QApplication
from test import *
class Win(QWidget):
    def __init__(self):
        super(Win, self).__init__()
        self.resize(600,600)
        self.setWindowTitle('测试用')
        self.func_list()
        self.pare=Cjj()
    def func_list(self):
        self.func1()
        self.func2()
        self.func3()

    def func1(self):
        a=QLabel(self)
        a.setText('请输入用户名：')
        a.move(100,100)
        self.result2=a
    def func2(self):
        a=QPushButton(self)
        a.setText('登录')
        a.move(100,200)
        a.clicked.connect(self.login)
    def login(self):

        self.child.show()

    def func3(self):
        a=QLineEdit(self)
        a.setPlaceholderText('请输入用户名')
        a.move(300,100)
        self.result=a

class Cjj(Win):
    def __init__(self):
        super(Cjj, self).__init__()
        self.setWindowTitle('第二个窗口')
        self.pare=None




if __name__=='__main__':
    app=QApplication(sys.argv)
    win=Win()
    win.show()
    sys.exit(app.exec_())