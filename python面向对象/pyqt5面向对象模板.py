from PyQt5.Qt import *
import sys
class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('软件名称')
        self.resize(600,500)
        self.func_list()
    def func_list(self):
        self.func()
    def func(self):
        btn=QPushButton(self)
        btn.setText('按钮内容')
        btn.resize(120,30)
        btn.move(100,100)
        btn.setStyleSheet('background-color:green;font-size:20ppx;')

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())
    #app.exec_()进行循环