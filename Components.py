import re

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from Package.UI.MainWindow import Ui_MainWindow_kwic
from Package.UI.Help import Ui_Dialog_help
from Package.UI.Setting import Ui_Dialog_setting

from Package.KwicClass.Line import Line
from Package.KwicClass.Text import Text

class KwicMainWindow(QtWidgets.QMainWindow):#继承QMainWindow
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_kwic()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon('./assets/logo.png'))

        self.help_dialog = HelpDialog()
        self.setting_dialog = SettingDialog()

        self.ui_ButtonActivate()
        self.ui_ActionActivate()

        self.text = Text()
        self.cyclicshift_text = Text()
        self.searched_text = Text()
        self.input_plaintext = ''
        self.output_plaintext = ''
        #算法设置
        self.sort_rule = self.setting_dialog.ui.comboBox_sort.currentText()
        print("当前排序算法: "+self.sort_rule)
        self.search_rule = self.setting_dialog.ui.comboBox_search.currentText()
        print("当前搜索算法: "+self.search_rule)
        
    def ui_ButtonActivate(self):
        self.ui.pushButton_cyclicshift.clicked.connect(self.cyclicShift)
        self.ui.pushButton_sort.clicked.connect(self.sort)
        self.ui.pushButton_search.clicked.connect(self.search)

    def ui_ActionActivate(self):
        self.ui.action_setting.triggered.connect(self.getSettingDialog)
        self.ui.action_help.triggered.connect(self.getHelpDialog)
        self.ui.action_inputfile.triggered.connect(self.inputFile)
        self.ui.action_outputfile.triggered.connect(self.outputFile)

    """打开子窗口"""
    def getHelpDialog(self):
        """帮助"""
        self.help_dialog.show()
        
    def getSettingDialog(self):
        """设置"""
        self.setting_dialog.show()

    """导入文件,有待完善"""
    def readTxt(self,file_path):
        with open(file_path, encoding='utf-8') as f:
            return f.read()

    def inputFile(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, "选择文件",'','Text files (*.txt);; All files (*)')[0]
        file_type = file_path.split('.')[1]
        #类型判断暂时没什么软用
        if file_type == 'txt' or 1==1 :                
            self.input_plaintext = self.readTxt(file_path)
            self.ui.plainTextEdit_input.setPlainText(self.input_plaintext)

    """导出文件"""
    def outputFile(self):
        self.output_plaintext = self.ui.plainTextEdit_output.toPlainText()
        file_path = QtWidgets.QFileDialog.getSaveFileName(self,'保存文件','','Text files (*.txt);; All files (*)')[0]
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(self.output_plaintext)
        except:
            pass

    """getText|updateText,有待优化"""
    def updateText(self):
        self.text.clear()
        text = self.ui.plainTextEdit_input.toPlainText()
        for sentence in text.split('\n'):
            line = Line(sentence)
            self.text.addLine(line)

    """按钮功能函数"""
    def cyclicShift(self):
        """self.text ---> self.cyclicshift_text"""
        self.updateText()       #更新self.text
        self.text.cyclicShift() #调用循环移位
        #结果输出到plainTextEdit_output,后面可以尝试实现实时更新
        self.output_plaintext = ''
        self.cyclicshift_text.clear()
        for line in self.text.lines:
            for sentence in line.shift_sentences:
                self.cyclicshift_text.addLine(Line(sentence))
        self.ui.plainTextEdit_output.setPlainText(self.cyclicshift_text.toString())

    def sort(self):
        if self.cyclicshift_text.toString() == '':
            self.cyclicShift()

        self.sort_rule = self.setting_dialog.ui.comboBox_sort.currentText()
        self.cyclicshift_text.setSortRule(self.sort_rule)
        self.cyclicshift_text.sort()
        self.ui.plainTextEdit_output.setPlainText(self.cyclicshift_text.toString())

    def search(self):
        keywords = re.split(r'[ ]+',self.ui.lineEdit_keywords.text())

        self.search_rule = self.setting_dialog.ui.comboBox_search.currentText()
        self.cyclicshift_text.setSearchRule(self.search_rule)
        searched_lines = self.cyclicshift_text.search(keywords)

        self.searched_text.lines = searched_lines
        self.ui.plainTextEdit_output.setPlainText(self.searched_text.toString())

#改成单例模式？？不用，pyside自动支持了
class HelpDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Dialog_help()
        self.setWindowIcon(QIcon('./assets/help.png'))
        self.ui.setupUi(self)

class SettingDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Dialog_setting()
        self.setWindowIcon(QIcon('./assets/setting.png'))
        self.ui.setupUi(self)
