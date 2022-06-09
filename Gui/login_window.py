


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor


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
        self.label.setGeometry(QtCore.QRect(450, 40, 151, 111))
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
        self.label_2.setGeometry(QtCore.QRect(400, 150, 191, 51))
        self.label_2.setStyleSheet("font: italic 11pt \"Arial\";\n"
"color: white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.main_widget)
        self.label_3.setGeometry(QtCore.QRect(20, 760, 311, 51))
        self.label_3.setStyleSheet("font: 8pt \"Arial\";\n"
"color:rgb(0, 0, 255)")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.main_widget)
        self.pushButton.setGeometry(QtCore.QRect(340, 560, 381, 81))
        self.pushButton.setStyleSheet("border-radius: 40px;\n"
"background-color:rgb(181, 181, 181);\n"
"font: 14pt \"Arial\";\n"
"color: white;")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.main_widget)
        self.lineEdit.setGeometry(QtCore.QRect(350, 460, 361, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.main_widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 340, 361, 61))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.main_widget)
        self.label_4.setGeometry(QtCore.QRect(350, 312, 91, 21))
        self.label_4.setStyleSheet("color: white;\n"
"font: 75 11pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.main_widget)
        self.label_5.setGeometry(QtCore.QRect(350, 430, 91, 21))
        self.label_5.setStyleSheet("color: white;\n"
"font: 75 11pt \"Arial\";")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "Halte deine Kosten im Blick!"))
        self.label_3.setWhatsThis(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "Sponsored by: Tim, Sebastian ,Maxim, Hendrik, Damien"))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.label_4.setText(_translate("Dialog", "Username:"))
        self.label_5.setText(_translate("Dialog", "Passwort:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
