# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Kasir.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 899)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 180, 1131, 421))
        self.label_3.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 261, 181))
        self.label_4.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, -20, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 110, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 60, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(550, 0, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.txtnama = QtWidgets.QLineEdit(self.centralwidget)
        self.txtnama.setGeometry(QtCore.QRect(370, 60, 521, 22))
        self.txtnama.setObjectName("txtnama")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(280, 120, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(770, 170, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(770, 120, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(280, 170, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(540, 170, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(520, 120, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.btntambah = QtWidgets.QPushButton(self.centralwidget)
        self.btntambah.setGeometry(QtCore.QRect(470, 220, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btntambah.setFont(font)
        self.btntambah.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.btntambah.setObjectName("btntambah")
        self.btnedit = QtWidgets.QPushButton(self.centralwidget)
        self.btnedit.setGeometry(QtCore.QRect(610, 220, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnedit.setFont(font)
        self.btnedit.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnedit.setObjectName("btnedit")
        self.btnhapus = QtWidgets.QPushButton(self.centralwidget)
        self.btnhapus.setGeometry(QtCore.QRect(750, 220, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnhapus.setFont(font)
        self.btnhapus.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnhapus.setObjectName("btnhapus")
        self.btncari = QtWidgets.QPushButton(self.centralwidget)
        self.btncari.setGeometry(QtCore.QRect(890, 220, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btncari.setFont(font)
        self.btncari.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.btncari.setObjectName("btncari")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 330, 1111, 511))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridBarang = QtWidgets.QTableWidget(self.groupBox)
        self.gridBarang.setGeometry(QtCore.QRect(0, 0, 1111, 511))
        self.gridBarang.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:black;")
        self.gridBarang.setRowCount(13)
        self.gridBarang.setColumnCount(8)
        self.gridBarang.setObjectName("gridBarang")
        item = QtWidgets.QTableWidgetItem()
        self.gridBarang.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridBarang.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridBarang.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridBarang.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridBarang.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridBarang.setHorizontalHeaderItem(2, item)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(500, 280, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.btnclear = QtWidgets.QPushButton(self.centralwidget)
        self.btnclear.setGeometry(QtCore.QRect(330, 220, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnclear.setFont(font)
        self.btnclear.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnclear.setObjectName("btnclear")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1131, 661))
        self.label_2.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.txthrgbeli = QtWidgets.QLineEdit(self.centralwidget)
        self.txthrgbeli.setGeometry(QtCore.QRect(360, 120, 141, 22))
        self.txthrgbeli.setObjectName("txthrgbeli")
        self.txtjual = QtWidgets.QLineEdit(self.centralwidget)
        self.txtjual.setGeometry(QtCore.QRect(600, 120, 141, 22))
        self.txtjual.setObjectName("txtjual")
        self.txtasal = QtWidgets.QLineEdit(self.centralwidget)
        self.txtasal.setGeometry(QtCore.QRect(840, 120, 141, 22))
        self.txtasal.setObjectName("txtasal")
        self.txttanggal = QtWidgets.QLineEdit(self.centralwidget)
        self.txttanggal.setGeometry(QtCore.QRect(380, 170, 141, 22))
        self.txttanggal.setObjectName("txttanggal")
        self.txtqt = QtWidgets.QLineEdit(self.centralwidget)
        self.txtqt.setGeometry(QtCore.QRect(610, 170, 141, 22))
        self.txtqt.setObjectName("txtqt")
        self.txtkode = QtWidgets.QLineEdit(self.centralwidget)
        self.txtkode.setGeometry(QtCore.QRect(860, 170, 141, 22))
        self.txtkode.setObjectName("txtkode")
        self.txtid = QtWidgets.QLineEdit(self.centralwidget)
        self.txtid.setGeometry(QtCore.QRect(940, 60, 141, 22))
        self.txtid.setObjectName("txtid")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(920, 60, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(10, 660, 1131, 661))
        self.label_18.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_18.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_6.raise_()
        self.label_9.raise_()
        self.txtnama.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.btntambah.raise_()
        self.btnedit.raise_()
        self.btnhapus.raise_()
        self.btncari.raise_()
        self.groupBox.raise_()
        self.label_16.raise_()
        self.btnclear.raise_()
        self.txthrgbeli.raise_()
        self.txtjual.raise_()
        self.txtasal.raise_()
        self.txttanggal.raise_()
        self.txtqt.raise_()
        self.txtkode.raise_()
        self.txtid.raise_()
        self.label_17.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1129, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", " Aplikasi Kasir Sederhana"))
        self.label_7.setText(_translate("MainWindow", "Toko Buku & Alat Tulis"))
        self.label_8.setText(_translate("MainWindow", "Laksana"))
        self.label_6.setText(_translate("MainWindow", "Nama Barang"))
        self.label_9.setText(_translate("MainWindow", "Form Input Barang"))
        self.label_10.setText(_translate("MainWindow", "Harga Beli"))
        self.label_11.setText(_translate("MainWindow", "Kode Barang"))
        self.label_12.setText(_translate("MainWindow", "Dari Toko"))
        self.label_13.setText(_translate("MainWindow", "Tanggal Masuk"))
        self.label_14.setText(_translate("MainWindow", "QT Barang"))
        self.label_15.setText(_translate("MainWindow", "Harga Jual"))
        self.btntambah.setText(_translate("MainWindow", "Tambahkan"))
        self.btnedit.setText(_translate("MainWindow", "Edit"))
        self.btnhapus.setText(_translate("MainWindow", "Hapus"))
        self.btncari.setText(_translate("MainWindow", "Cari"))
        item = self.gridBarang.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.gridBarang.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "3"))
        item = self.gridBarang.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "2"))
        item = self.gridBarang.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.gridBarang.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.gridBarang.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        self.label_16.setText(_translate("MainWindow", "Data Barang"))
        self.btnclear.setText(_translate("MainWindow", "Clear"))
        self.label_17.setText(_translate("MainWindow", "ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
