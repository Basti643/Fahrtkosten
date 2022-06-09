

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
        self.label.setGeometry(QtCore.QRect(310, 10, 381, 111))
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
        self.strecke_zieleingabe = QtWidgets.QPushButton(self.main_widget)
        self.strecke_zieleingabe.setGeometry(QtCore.QRect(110, 140, 381, 81))
        self.strecke_zieleingabe.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.strecke_zieleingabe.setStyleSheet("border-radius: 40px;\n"
        
"background-color:rgb(181, 181, 181);\n"
"font: 14pt \"Arial\";\n"
"color: white;")
        self.strecke_zieleingabe.setObjectName("strecke_zieleingabe")
        self.fahrtenbuch = QtWidgets.QPushButton(self.main_widget)
        self.fahrtenbuch.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.fahrtenbuch.setGeometry(QtCore.QRect(60, 280, 381, 81))
        self.fahrtenbuch.setStyleSheet("border-radius: 40px;\n"
"background-color:rgb(181, 181, 181);\n"
"font: 14pt \"Arial\";\n"
"color: white;")
        self.fahrtenbuch.setObjectName("fahrtenbuch")
        self.spritkosten = QtWidgets.QPushButton(self.main_widget)
        self.spritkosten.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.spritkosten.setGeometry(QtCore.QRect(100, 430, 381, 81))
        self.spritkosten.setStyleSheet("border-radius: 40px;\n"
"background-color:rgb(181, 181, 181);\n"
"font: 14pt \"Arial\";\n"
"color: white;")
        self.spritkosten.setObjectName("spritkosten")
        self.spritkosten_2 = QtWidgets.QPushButton(self.main_widget)
        self.spritkosten_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.spritkosten_2.setGeometry(QtCore.QRect(150, 600, 381, 81))
        self.spritkosten_2.setStyleSheet("border-radius: 40px;\n"
"background-color:rgb(181, 181, 181);\n"
"font: 14pt \"Arial\";\n"
"color: white;")
        self.spritkosten_2.setObjectName("spritkosten_2")
        self.label_2 = QtWidgets.QLabel(self.main_widget)
        self.label_2.setGeometry(QtCore.QRect(480, 160, 501, 481))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.main_widget.setWhatsThis(_translate("Dialog", "<html>\"/><img src=\":/newPrefix/oil.png\"/></p></body></html>"))
        self.label.setText(_translate("Dialog", "Wähle deinen Menüpunkt!"))
        self.strecke_zieleingabe.setText(_translate("Dialog", "Strecke/Zieleingabe"))
        self.fahrtenbuch.setText(_translate("Dialog", "Fahrtenbuch/-Historie"))
        self.spritkosten.setText(_translate("Dialog", "Spritkosten kumuliert"))
        self.spritkosten_2.setText(_translate("Dialog", "Mein Fahrzeug"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><img src=fuel_2.png/></p></body></html>"))

#import fuel_2.qrc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
