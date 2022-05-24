from PySide6 import QtWidgets
from MainWindow import Ui_MainWindow_kwic
from Help import Ui_Dialog_help
from Setting import Ui_Dialog_setting
class KwicMainWindow(QtWidgets.QMainWindow):#继承QMainWindow
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_kwic()

        self.ui.setupUi(self)

        self.ui_ButtonActivate()
        self.ui_ActionActivate()
    
    def ui_ButtonActivate(self):
        pass

    def ui_ActionActivate(self):
        self.ui.action_setting.triggered.connect(self.getSettingDialog)
        self.ui.action_help.triggered.connect(self.getHelpDialog)
        self.ui.action_inputfile.triggered.connect(self.inputFile)
        self.ui.action_outputfile.triggered.connect(self.outputFile)

    """打开子窗口"""
    def getHelpDialog(self):
        """帮助"""
        self.help_dialog = HelpDialog()
        self.help_dialog.show()
        
    def getSettingDialog(self):
        """设置"""
        self.setting_dialog = SettingDialog()
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

    """按钮功能函数"""
    def cyclicShift(self):
        pass

    def sort(self):
        pass

    def search(self):
        pass

#改成单例模式？？
class HelpDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Dialog_help()
        self.ui.setupUi(self)

class SettingDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Dialog_setting()
        self.ui.setupUi(self)



