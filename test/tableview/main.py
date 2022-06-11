import sys
from PyQt5.QtWidgets import QApplication
import test
if __name__=='__main__':
    app=QApplication(sys.argv)
    ui= test.MainWindow()
    ui.show()

    sys.exit(app.exec_())