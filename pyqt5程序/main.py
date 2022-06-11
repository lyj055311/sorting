import sys
from PyQt5.QtWidgets import QApplication
import index_function
if __name__=='__main__':
    app=QApplication(sys.argv)
    ui=index_function.MainWindow()
    ui.show()
    sys.exit(app.exec())