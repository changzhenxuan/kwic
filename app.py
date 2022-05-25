from PySide6 import QtWidgets
from Components import KwicMainWindow

import sys
class a:
    def __init__(self):
        self.name = 'czx'
    def geyName(self):
        return self.name

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = KwicMainWindow() #实例化窗口
    window.show()#显示

    sys.exit(app.exec())