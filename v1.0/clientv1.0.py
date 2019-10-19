import socket
import threading
import sys
from encrypt_module import create_pair
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTextEdit, QMessageBox
import win32console

server = 'skopcovs1.fvds.ru', 9090
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))

class Messager(QMainWindow):
    def send_msg(self):
        msg = self.message.text()
        self.message.setText('')
        self.browser.append(f"You: {msg}")
        sor.sendto(('[' + alias + ']: ' + msg).encode('utf-8'), server)

    def read(self):
        while 1:
            data = sor.recv(1024).decode()
            self.browser.append(data)

    def enter_alias(self):
        alias = self.nick.text()
        sor.sendto((f'\n-------------------{alias} connected to server-------------------\n').encode('utf-8'), server)
        self.destroy()
    
    def __init__(self):
        super().__init__()

        uic.loadUi('msg.ui', self)
        self.send.clicked.connect(self.send_msg)
        self.send.setAutoDefault(True)
        self.message.returnPressed.connect(self.send.click)

        read_thread = threading.Thread(target=self.read)
        read_thread.start()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        super().__init__()
        uic.loadUi('name_input.ui', Dialog)
        ex.message.setReadOnly(True)
        Dialog.enter.clicked.connect(self.send_alias_info)
    
    def send_alias_info(self):
        global alias
        alias = Dialog.nick.text()
        sor.sendto((f'\n-------------------{alias} connected to server-------------------\n').encode('utf-8'), server)
        ex.message.setReadOnly(False)
        Dialog.destroy()


app = QApplication(sys.argv)
ex = Messager()

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

ex.show()
sys.exit(app.exec_())
