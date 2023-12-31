# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 702)
        MainWindow.setMaximumSize(QtCore.QSize(1280, 704))
        MainWindow.setStyleSheet("background-color: rgb(235, 228, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 101, 901))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.view = QtWidgets.QPushButton(self.frame)
        self.view.setGeometry(QtCore.QRect(0, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.view.setFont(font)
        self.view.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.view.setObjectName("view")
        self.add = QtWidgets.QPushButton(self.frame)
        self.add.setGeometry(QtCore.QRect(0, 60, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add.setFont(font)
        self.add.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.add.setObjectName("add")
        self.update = QtWidgets.QPushButton(self.frame)
        self.update.setGeometry(QtCore.QRect(0, 100, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.update.setFont(font)
        self.update.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"")
        self.update.setObjectName("update")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(90, 20, 1181, 681))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.table = QtWidgets.QTableWidget(self.page)
        self.table.setGeometry(QtCore.QRect(10, 50, 1161, 611))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table.setFont(font)
        self.table.setAutoFillBackground(True)
        self.table.setStyleSheet("background-color: rgb(255, 234, 254);")
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setObjectName("table")
        self.table.setColumnCount(11)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(10, item)
        self.comboBox = QtWidgets.QComboBox(self.page)
        self.comboBox.setGeometry(QtCore.QRect(1090, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.num = QtWidgets.QLabel(self.page)
        self.num.setGeometry(QtCore.QRect(12, 15, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.num.setFont(font)
        self.num.setStyleSheet("color: rgb(255, 0, 0);")
        self.num.setText("")
        self.num.setObjectName("num")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(320, 60, 561, 508))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.phone = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.phone.setFont(font)
        self.phone.setMaxLength(15)
        self.phone.setClearButtonEnabled(True)
        self.phone.setObjectName("phone")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.phone)
        self.chassis = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chassis.setFont(font)
        self.chassis.setMaxLength(30)
        self.chassis.setClearButtonEnabled(True)
        self.chassis.setObjectName("chassis")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.chassis)
        self.date = QtWidgets.QDateEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.date.setFont(font)
        self.date.setCalendarPopup(True)
        self.date.setObjectName("date")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.date)
        self.submit = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submit.setFont(font)
        self.submit.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(170, 0, 0);")
        self.submit.setObjectName("submit")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.submit)
        self.msg = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.msg.setFont(font)
        self.msg.setText("")
        self.msg.setObjectName("msg")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.msg)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(85, 0, 0);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label)
        self.name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name.setFont(font)
        self.name.setText("")
        self.name.setMaxLength(100)
        self.name.setClearButtonEnabled(True)
        self.name.setObjectName("name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.name)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(85, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(85, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(85, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.nmsg = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nmsg.setFont(font)
        self.nmsg.setStyleSheet("color: rgb(255, 0, 0);")
        self.nmsg.setText("")
        self.nmsg.setObjectName("nmsg")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.nmsg)
        self.pmsg = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pmsg.setFont(font)
        self.pmsg.setStyleSheet("color: rgb(255, 0, 0);")
        self.pmsg.setText("")
        self.pmsg.setObjectName("pmsg")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pmsg)
        self.cmsg = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmsg.setFont(font)
        self.cmsg.setStyleSheet("color: rgb(255, 0, 0);")
        self.cmsg.setText("")
        self.cmsg.setObjectName("cmsg")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.cmsg)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.search = QtWidgets.QLineEdit(self.page_3)
        self.search.setGeometry(QtCore.QRect(10, 20, 341, 31))
        self.search.setClearButtonEnabled(True)
        self.search.setObjectName("search")
        self.table2 = QtWidgets.QTableWidget(self.page_3)
        self.table2.setGeometry(QtCore.QRect(10, 60, 1161, 601))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table2.setFont(font)
        self.table2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table2.setStyleSheet("background-color: rgb(255, 234, 254);")
        self.table2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table2.setObjectName("table2")
        self.table2.setColumnCount(13)
        self.table2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(12, item)
        self.stackedWidget.addWidget(self.page_3)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.frame_2.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.view.setText(_translate("MainWindow", "View"))
        self.add.setText(_translate("MainWindow", "Add"))
        self.update.setText(_translate("MainWindow", "Modify"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "S.NO"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NAME"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PHONE NUMBER"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CHASSIS NUMBER"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "DATE OF SALE"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "1ST SERVICE"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "DAYS"))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "2ND SERVICE"))
        item = self.table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "DAYS"))
        item = self.table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "3RD  SERVICE"))
        item = self.table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "DAYS"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox.setItemText(9, _translate("MainWindow", "10"))
        self.date.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.submit.setText(_translate("MainWindow", "SAVE"))
        self.label.setText(_translate("MainWindow", "CUSTOMER NAME"))
        self.label_2.setText(_translate("MainWindow", "PHONE NUMBER"))
        self.label_3.setText(_translate("MainWindow", "CHASSIS NUMBER"))
        self.label_4.setText(_translate("MainWindow", "DATE OF SALE"))
        self.search.setPlaceholderText(_translate("MainWindow", "Search: name or phone  or chassis number"))
        item = self.table2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "S.NO"))
        item = self.table2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NAME"))
        item = self.table2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PHONE NUMBER"))
        item = self.table2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CHASSIS NUMBER"))
        item = self.table2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "DATE OF SALE"))
        item = self.table2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "1ST SERVICE"))
        item = self.table2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "DAYS"))
        item = self.table2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "2ND SERVICE"))
        item = self.table2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "DAYS"))
        item = self.table2.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "3RD  SERVICE"))
        item = self.table2.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "DAYS"))
        item = self.table2.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "EDIT"))
        item = self.table2.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "DELETE"))
