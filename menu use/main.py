import sys
from PyQt5.QtWidgets import QApplication
from index import MainWindow

class main(MainWindow):
    def __init__(self):
        super().__init__()




if __name__=='__main__':
    app=QApplication(sys.argv)
    ui=main()
    ui.show()
    sys.exit(app.exec_())