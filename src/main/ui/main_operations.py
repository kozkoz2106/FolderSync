from PyQt5.QtWidgets import QMainWindow, QApplication
from main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.select_src.clicked.connect(self.srcclick)
        self.ui.select_dst.clicked.connect(self.dstclick)

    def srcclick(self):
        print("Source selection button clicked!")

    def dstclick(self):
        print("Destination selection button clicked!")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())