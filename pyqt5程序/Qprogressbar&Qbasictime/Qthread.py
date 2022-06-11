from PyQt5.QtCore import QThread,pyqtSignal,QBasicTimer
import time
class MyThread(QThread):
    mysignal=pyqtSignal(int)
    def __init__(self,index=0):
        super(MyThread, self).__init__()
        self.index=index

        self.number=0
        self.isRunning=True
    def run(self):
        while 1:
            self.number+=1
            if self.number==101:
                self.number=0
            self.mysignal.emit(self.number)
            time.sleep(0.01)



