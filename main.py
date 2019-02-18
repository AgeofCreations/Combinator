from ui import *
from PyQt5.Qt import *

#-------------------Обработка исключений--------------------------

def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Error', text)
    quit()

    import sys
    sys.excepthook = log_uncaught_exceptions

#---------------------------Thread---------------------------------
class MyCheckUrlThread(QThread):
    generating = pyqtSignal(list)
    result = pyqtSignal(str)
    
    lcd_value = pyqtSignal(int)
    def __init__(self,list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12):
        super().__init__()
        self.list1 = list1
        self.list2 = list2
        self.list3 = list3
        self.list4 = list4
        self.list5 = list5
        self.list6 = list6
        self.list7 = list7
        self.list8 = list8
        self.list9 = list9
        self.list10 = list10
        self.list11 = list11
        self.list12 = list12
    def run(self):
        fulllen = len(self.list1) * len(self.list2) * len(self.list3) * len(self.list4) * len(self.list5) *\
        len(self.list6) * len(self.list7) * len(self.list8) * len(self.list9) * len(self.list10) * len(self.list11) *\
            len(self.list12)
        if fulllen < 10000000:
            results = ['{} {} {} {} {} {} {} {} {} {} {} {}'.format(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12)
                        for x1 in self.list1
                            for x2 in self.list2
                                for x3 in self.list3
                                    for x4 in self.list4
                                        for x5 in self.list5
                                            for x6 in self.list6
                                                for x7 in self.list7
                                                    for x8 in self.list8
                                                        for x9 in self.list9
                                                            for x10 in self.list10
                                                                for x11 in self.list11
                                                                    for x12 in self.list12]
            with open("results.txt", "w") as file:
                print(*results, file=file, sep="\n")
            self.result.emit('Готово. Результат сохранён в файл. Всего получилось: '+ str(len(results)) + ' значений')
        else:
            self.result.emit('Ошибка. Нельзя создать такое количество пересечений. Текущий результат: ' +str(fulllen))

class FastLenCalculating(QThread):
    fulllen_val = pyqtSignal(str)
    lenval = pyqtSignal(str)
    def __init__(self,list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12):
        super().__init__()
        self.list1 = list1
        self.list2 = list2
        self.list3 = list3
        self.list4 = list4
        self.list5 = list5
        self.list6 = list6
        self.list7 = list7
        self.list8 = list8
        self.list9 = list9
        self.list10 = list10
        self.list11 = list11
        self.list12 = list12

    def run(self):
        fulllen = len(self.list1) * len(self.list2) * len(self.list3) * len(self.list4) * len(self.list5) *\
        len(self.list6) * len(self.list7) * len(self.list8) * len(self.list9) * len(self.list10) * len(self.list11) *\
            len(self.list12)
        self.lenval.emit('Текущее значение:' + str(int(fulllen)))
#-------------------Объявление UI-----------------------

class MyWin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.list1 = self.ui.textEdit
        self.list2 = self.ui.textEdit_2
        self.list3 = self.ui.textEdit_3
        self.list4 = self.ui.textEdit_4
        self.list5 = self.ui.textEdit_6
        self.list6 = self.ui.textEdit_5
        self.list7 = self.ui.textEdit_7
        self.list8 = self.ui.textEdit_8
        self.list9 = self.ui.textEdit_9
        self.list10 = self.ui.textEdit_10
        self.list11 = self.ui.textEdit_11
        self.list12 = self.ui.textEdit_12
        self.result = self.ui.textBrowser
        self.lcd = self.ui.lcdNumber

        self.ui.pushButton.clicked.connect(self._generating)
        self.ui.pushButton_2.clicked.connect(self._len)
        self.ui.pushButton_3.clicked.connect(self._erase_fields)

#----------------------------------Thread--------------------------------------------
        self.thread = MyCheckUrlThread(list1=[],list2=[],list3=[],list4=[],list5=[],list6=[],
                                       list7=[],list8=[],list9=[],list10=[],list11=[],list12=[])
        self.thread2 = FastLenCalculating(list1=[],list2=[],list3=[],list4=[],list5=[],list6=[],
                                          list7=[],list8=[],list9=[],list10=[],list11=[],list12=[])
        self.thread.generating.connect(self._generating)
        self.thread.result.connect(self._result)
        self.thread2.fulllen_val.connect(self._len)
        self.thread2.lenval.connect(self._lenvalue)


#-----------------------------Функции интерфейса------------------------------------
    def _generating(self):
        self.result.setText('')
        self.thread.list1 = self.list1.toPlainText().strip().split('\n')
        self.thread.list2 = self.list2.toPlainText().strip().split('\n')
        self.thread.list3 = self.list3.toPlainText().strip().split('\n')
        self.thread.list4 = self.list4.toPlainText().strip().split('\n')
        self.thread.list5 = self.list5.toPlainText().strip().split('\n')
        self.thread.list6 = self.list6.toPlainText().strip().split('\n')
        self.thread.list7 = self.list7.toPlainText().strip().split('\n')
        self.thread.list8 = self.list8.toPlainText().strip().split('\n')
        self.thread.list9 = self.list9.toPlainText().strip().split('\n')
        self.thread.list10 = self.list10.toPlainText().strip().split('\n')
        self.thread.list11 = self.list11.toPlainText().strip().split('\n')
        self.thread.list12 = self.list12.toPlainText().strip().split('\n')
        self.thread.start()

    def _result(self,text):
        self.result.append(text)

    def _len(self):
        self.thread2.list1 = self.list1.toPlainText().strip().split('\n')
        self.thread2.list2 = self.list2.toPlainText().strip().split('\n')
        self.thread2.list3 = self.list3.toPlainText().strip().split('\n')
        self.thread2.list4 = self.list4.toPlainText().strip().split('\n')
        self.thread2.list5 = self.list5.toPlainText().strip().split('\n')
        self.thread2.list6 = self.list6.toPlainText().strip().split('\n')
        self.thread2.list7 = self.list7.toPlainText().strip().split('\n')
        self.thread2.list8 = self.list8.toPlainText().strip().split('\n')
        self.thread2.list9 = self.list9.toPlainText().strip().split('\n')
        self.thread2.list10 = self.list10.toPlainText().strip().split('\n')
        self.thread2.list11 = self.list11.toPlainText().strip().split('\n')
        self.thread2.list12 = self.list12.toPlainText().strip().split('\n')
        self.thread2.start()

    def _lenvalue(self,text):
        self.result.append(text)

    def _erase_fields(self):
        self.ui.textBrowser.setText('')
        self.ui.textEdit.setText('')
        self.ui.textEdit_2.setText('')
        self.ui.textEdit_3.setText('')
        self.ui.textEdit_4.setText('')
        self.ui.textEdit_5.setText('')
        self.ui.textEdit_6.setText('')
        self.ui.textEdit_7.setText('')
        self.ui.textEdit_8.setText('')
        self.ui.textEdit_9.setText('')
        self.ui.textEdit_10.setText('')
        self.ui.textEdit_11.setText('')
        self.ui.textEdit_12.setText('')



#-------------UI запуск------------------

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    myapp = MyWin()
    myapp.show()
    app.exec()

