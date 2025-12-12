from PyQt5.QtWidgets import QMainWindow, QApplication
from .main import Ui_MainWindow
from foldersync.backend.operations import *

class MainWindow(QMainWindow):
    operations = SyncOperations()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.src_button.clicked.connect(self.srcclick)
        self.ui.dst_button.clicked.connect(self.dstclick)
        self.ui.sync_button.clicked.connect(self.syncclick)

    def srcclick(self):
        print("Source selection button clicked!")
        self.operations.select_sources()

    def dstclick(self):
        print("Destination selection button clicked!")
        self.operations.select_dst()

    def syncclick(self):
        self.operations.press_sync()
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())