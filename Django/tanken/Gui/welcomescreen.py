import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QDialog, QApplication,QWidget



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1042, 835)
        self.main_widget = QtWidgets.QWidget(Dialog)
        self.main_widget.setGeometry(QtCore.QRect(0, 0, 1051, 841))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.main_widget.setFont(font)
        self.main_widget.setStyleSheet("\n"
"QWidget#main_widget{\n"
"background-color:qlineargradient(spread:reflect, x1:1, y1:1, x2:0.149417, y2:0.261, stop:0 \n"
"rgba(170, 255, 255, 255), stop:1 rgba(0, 191, 255, 255));}")
        self.main_widget.setObjectName("main_widget")
        self.label = QtWidgets.QLabel(self.main_widget)
        self.label.setGeometry(QtCore.QRect(300, 40, 481, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"font: 75 22pt \"Arial\";\n"
"color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.main_widget)
        self.label_2.setGeometry(QtCore.QRect(420, 120, 191, 51))
        self.label_2.setStyleSheet("font: italic 11pt \"Arial\";\n"
"color: white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.main_widget)
        self.label_3.setGeometry(QtCore.QRect(20, 760, 311, 51))
        self.label_3.setStyleSheet("font: 8pt \"Arial\";\n"
"color:rgb(0, 0, 255)")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.main_widget)
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setGeometry(QtCore.QRect(320, 710, 381, 91))
        self.pushButton.setStyleSheet("border-radius: 40px;\n"
"background-color:rgb(181, 181, 181);\n"
"font: 14pt \"Arial\";\n"
"color: white;")
        self.pushButton.setObjectName("pushButton")
        self.login_button_1 = QtWidgets.QPushButton(self.main_widget)
        self.login_button_1.setGeometry(QtCore.QRect(320, 600, 381, 91))
        self.login_button_1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.login_button_1.setStyleSheet("border-radius: 40px;\n"
"background-color:rgb(181, 181, 181);\n"
"font: 14pt \"Arial\";\n"
"color: white;")
        self.login_button_1.setObjectName("login_button_1")
        self.label_4 = QtWidgets.QLabel(self.main_widget)
        self.label_4.setGeometry(QtCore.QRect(260, -10, 531, 641))
        self.label_4.setMinimumSize(QtCore.QSize(531, 0))
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.login_button_1.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Willkommen bei der Spritpreisapp!"))
        self.label_2.setText(_translate("Dialog", "Halte deine Kosten im Blick!"))
        self.label_3.setWhatsThis(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "Sponsored by: Tim, Sebastian ,Maxim, Hendrik, Damien"))
        self.pushButton.setText(_translate("Dialog", "Registrierung"))
        self.login_button_1.setText(_translate("Dialog", "Login"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><img src=Tankbild.png/></p></body></html>"))

#import logo1.qrc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

