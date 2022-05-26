from PySide6 import QtWidgets
from Components import KwicMainWindow

import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    #app.setStyle(QtWidgets.QStyleFactory.create("Fusion")) # 体验差
    window = KwicMainWindow() #实例化窗口
    window.show()#显示

    sys.exit(app.exec())