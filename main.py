import os
import sys
import shutil
import sqlite3

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QDialog, QMessageBox, QAbstractItemView, QMenu,\
    QLineEdit, QDialogButtonBox, QFormLayout, QAction, QLabel
from design import Ui_MainWindow
from datetime import date, datetime, timedelta

# set path
if os.path.exists('D:'):
    if not os.path.exists('D:/ServiceReminder'):
        os.makedirs('D:/ServiceReminder')
        shutil.copy(sys.argv[0], 'D:/ServiceReminder')
    conn = sqlite3.connect('D:/ServiceReminder/test.db')
elif os.path.exists('E:'):  
    if not os.path.exists('E:/ServiceReminder'):
        os.makedirs('E:/ServiceReminder')
        shutil.copy(sys.argv[0], 'E:/ServiceReminder')
    conn = sqlite3.connect('E:/ServiceReminder/test.db')
else:
    if not os.path.exists('C:/ServiceReminder'):
        os.makedirs('C:/ServiceReminder')
        shutil.copy(sys.argv[0], 'C:/ServiceReminder')
    conn = sqlite3.connect('C:/ServiceReminder/test.db')

today = date.today()
key = ""
menuflag = 1
conn.execute("CREATE TABLE IF NOT EXISTS CUSTOMER(NAME VARCHAR(100), PHONE CHAR(15) ,"
             "CHASSIS VARCHAR(30) NOT NULL PRIMARY KEY, DATE DATE)")
conn.execute("CREATE TABLE IF NOT EXISTS COMBO(NUMBER INTEGER)")
dbc = conn.execute("SELECT NUMBER FROM COMBO")
result = dbc.fetchone()
if result is not None:
    combo = result[0]
else:
    conn.execute("INSERT INTO COMBO VALUES(10)")
    conn.commit()
    combo = 10


class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        global key

        self.name = QLineEdit(self)
        self.nmsg = QLabel(self)
        self.name.setMaxLength(100)
        self.phone = QLineEdit(self)
        self.pmsg = QLabel(self)
        self.phone.setMaxLength(15)
        self.date = QtWidgets.QDateEdit(calendarPopup=True)
        self.date.setMaximumDate(today)
        self.date.setDisplayFormat("yyyy-MM-dd")
        self.nmsg.setStyleSheet("color:red")
        self.pmsg.setStyleSheet("color:red")
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("Customer name", self.name)
        layout.addRow(" ", self.nmsg)
        layout.addRow("Phone number", self.phone)
        layout.addRow(" ", self.pmsg)
        layout.addRow("Date of sale", self.date)
        layout.addWidget(self.buttonBox)

        c = conn.execute("SELECT * from CUSTOMER where CHASSIS = ?", (key,))

        for r in c:
            self.name.setText(r[0])
            self.phone.setText(r[1])
            dd = datetime.strptime(str(r[3]), "%Y-%m-%d")
            self.date.setDate(dd)

        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.accepted.connect(self.accept)

    def accept(self):
        name = self.name.text()
        phone = self.phone.text()
        name = name.replace(" ", "")
        name = name.replace(".", "")
        if name == "":
            self.nmsg.setText("Name is empty.")
        elif not name.isalpha() or len(name) < 3:
            self.nmsg.setText("Name is invalid.")
        else:
            self.nmsg.setText("")
            phone = phone.replace("+", "")
            phone = phone.replace("(", "")
            phone = phone.replace(")", "")
            if phone == "":
                self.pmsg.setText("Phone number is empty.")
            elif not phone.isnumeric() or len(phone) < 4:
                self.pmsg.setText("phone number is invalid.")
            else:
                self.pmsg.setText("")
                conn.execute("UPDATE CUSTOMER SET NAME = ? , PHONE = ? , DATE = ? WHERE CHASSIS = ?",
                             (name, phone, self.date.date().toPyDate(), key,))
                conn.commit()
                self.close()


class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.view.clicked.connect(self.fnview)
        self.ui.add.clicked.connect(self.fnadd)
        self.ui.update.clicked.connect(self.fnupdate)
        self.ui.submit.clicked.connect(self.submit)
        self.fnview()
        self.ui.comboBox.currentTextChanged.connect(self.on_combobox_changed)
        self.ui.search.textChanged.connect(self.showCurrentText)
        self.ui.name.textChanged.connect(self.validatename)
        self.ui.phone.textChanged.connect(self.validatephone)
        self.ui.chassis.textChanged.connect(self.validatechassis)
        self.ui.date.setMaximumDate(today)

        self.ui.submit.setStyleSheet("QPushButton"
                                     "{"
                                     "background-color : rgb(170, 170, 127)"
                                     "}"
                                     "QPushButton::pressed"
                                     "{"
                                     "background-color : green;color: white"
                                     "}"
                                     "QPushButton::hover"
                                     "{"
                                     "background-color : brown;"
                                     "}"
                                     )

    def showCurrentText(self):
        text = self.ui.search.text()
        self.loadProducts2(text)

    def validatename(self):
        name = self.ui.name.text()
        name = name.replace(" ", "")
        name = name.replace(".", "")
        if name == "":
            self.ui.nmsg.setText("Name is empty.")
            return False
        elif not name.isalpha() or len(name) < 3:
            self.ui.nmsg.setText("Name is invalid.")
            return False
        else:
            self.ui.nmsg.setText("")
            return True

    def validatephone(self):
        phone = self.ui.phone.text()
        phone = phone.replace("+","")
        phone = phone.replace("(", "")
        phone = phone.replace(")", "")
        if phone == "":
            self.ui.pmsg.setText("Phone number is empty.")
            return False
        elif not phone.isnumeric() or len(phone) < 4:
            self.ui.pmsg.setText("phone number is invalid.")
            return False
        else:
            self.ui.pmsg.setText("")
            return True

    def validatechassis(self):
        chassis = self.ui.chassis.text()
        if chassis == "":
            self.ui.cmsg.setText("Chassis number is empty.")
            return False
        elif not chassis.isalnum() or len(chassis) < 8:
            self.ui.cmsg.setText("Chassis number is invalid.")
            return False
        else:
            self.ui.cmsg.setText("")
            return True

    def fnview(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.loadProducts()
        self.ui.view.setStyleSheet("background-color: brown;color:white")
        self.ui.add.setStyleSheet("background-color: rgb(170, 170, 127)")
        self.ui.update.setStyleSheet("background-color: rgb(170, 170, 127)")

    def on_combobox_changed(self, value):
        global combo
        combo = int(value)
        conn.execute("UPDATE COMBO SET NUMBER = ? ", (combo,))
        conn.commit()
        self.loadProducts()

    def fnadd(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        self.ui.date.setDate(today)
        self.ui.msg.setText("")
        self.ui.view.setStyleSheet("background-color: rgb(170, 170, 127)")
        self.ui.add.setStyleSheet("background-color: brown;color:white")
        self.ui.update.setStyleSheet("background-color: rgb(170, 170, 127)")
        self.ui.name.setText("")
        self.ui.phone.setText("")
        self.ui.chassis.setText("")
        self.ui.msg.setText("")
        self.ui.nmsg.setText("")
        self.ui.pmsg.setText("")
        self.ui.cmsg.setText("")

    def fnupdate(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        self.ui.view.setStyleSheet("background-color: rgb(170, 170, 127)")
        self.ui.add.setStyleSheet("background-color: rgb(170, 170, 127)")
        self.ui.update.setStyleSheet("background-color: brown;color:white")
        self.loadProducts2("")

    def submit(self):
        boool1 = self.validatename()
        boool2 = self.validatechassis()
        boool3 = self.validatephone()
        if boool1 and boool2 and boool3:
            name = self.ui.name.text()
            phone = self.ui.phone.text()
            cn = self.ui.chassis.text()
            cn = cn.upper()
            d = self.ui.date.date()
            xdate = d.toPyDate()
            try:
                conn.execute("INSERT INTO CUSTOMER VALUES(?,?,?,?)", (name, phone, cn, xdate))
                conn.commit()
                self.ui.msg.setText("successfully saved.")
                self.ui.msg.setStyleSheet("color:green")
                self.ui.name.setText("")
                self.ui.phone.setText("")
                self.ui.chassis.setText("")
                self.ui.nmsg.setText("")
                self.ui.pmsg.setText("")
                self.ui.cmsg.setText("")
            except:
                self.ui.msg.setText("Error : Chassis number already exist !")
                self.ui.msg.setStyleSheet("color:red")

        else:
            self.ui.msg.setText("")

    def loadProducts(self):

        self.ui.comboBox.setCurrentIndex(combo - 1)
        tablelist = []
        self.ui.table.setColumnCount(11)
        self.ui.table.setColumnWidth(0, 50)
        self.ui.table.setColumnWidth(1, 170)
        self.ui.table.setColumnWidth(2, 150)
        self.ui.table.setColumnWidth(3, 220)
        self.ui.table.setColumnWidth(6, 50)
        self.ui.table.setColumnWidth(8, 50)
        self.ui.table.setColumnWidth(10, 50)
        self.ui.table.verticalHeader().setVisible(0)
        self.ui.table.horizontalHeader().setStyleSheet("color:brown")

        row_index = 0
        c = conn.execute("SELECT NAME,PHONE,CHASSIS,DATE from CUSTOMER WHERE julianday('now') - JULIANDAY(DATE)<361")

        for r in c:

            Begindate = datetime.strptime(str(r[3]), "%Y-%m-%d")

            date1 = Begindate.date() + timedelta(days=60)
            date2 = Begindate.date() + timedelta(days=180)
            date3 = Begindate.date() + timedelta(days=360)

            day1 = date1 - today
            day2 = date2 - today
            day3 = date3 - today

            d1 = day1.days
            d2 = day2.days
            d3 = day3.days

            dd1 = day1.days
            dd2 = day2.days
            dd3 = day3.days

            if day1.days < 0:
                d1 = 10000
            if day2.days < 0:
                d2 = 10000
            if day3.days < 0:
                d3 = 10000

            minday = min(d1, d2, d3)

            if day1.days < 0:
                d1 = dd1
            if day2.days < 0:
                d2 = dd2
            if day3.days < 0:
                d3 = dd3

            tablelist.append(
                [str(r[0]), str(r[1]), str(r[2]), str(r[3]), str(date1), d1, str(date2), d2, str(date3), d3, minday])
        s = sorted(tablelist, key=lambda v: v[10])
        count = len(s)
        self.ui.table.setRowCount(count)
        z = 0
        for i in s:

            self.ui.table.setItem(row_index, 0, QTableWidgetItem(str(row_index + 1)))
            for o in range(0, 10):
                self.ui.table.setItem(row_index, o + 1, QTableWidgetItem(str(i[o])))

            if i[10] <= combo:
                z += 1
                for o in range(0, 11):
                    self.ui.table.item(row_index, o).setBackground(QtGui.QColor(255, 255, 0))

            if i[5] >= 0:
                self.ui.table.item(row_index, 5).setBackground(QtGui.QColor(195, 234, 247))
            elif i[7] >= 0:
                self.ui.table.item(row_index, 7).setBackground(QtGui.QColor(195, 234, 247))
            elif i[9] >= 0:
                self.ui.table.item(row_index, 9).setBackground(QtGui.QColor(195, 234, 247))

            row_index += 1
        if z == 0:
            self.ui.num.setText("No services within " + str(combo) + " day(s)")
        else:
            self.ui.num.setText(str(z) + " services within " + str(combo) + " day(s)")
        self.ui.table.setAlternatingRowColors(1)
        self.ui.table.setRowCount(row_index)

    def loadProducts2(self, text):

        self.ui.table2.setColumnCount(11)
        self.ui.table2.setColumnWidth(0, 50)
        self.ui.table2.setColumnWidth(1, 200)
        self.ui.table2.setColumnWidth(2, 120)
        self.ui.table2.setColumnWidth(3, 220)
        self.ui.table2.setColumnWidth(6, 50)
        self.ui.table2.setColumnWidth(8, 50)
        self.ui.table2.setColumnWidth(10, 50)
        self.ui.table2.verticalHeader().setVisible(0)
        self.ui.table2.horizontalHeader().setStyleSheet("color:brown")

        db = conn.execute("SELECT COUNT(*) from CUSTOMER")
        rslt = db.fetchone()
        self.ui.table2.setRowCount(rslt[0])
        row_index = 0
        if text == "":
            c = conn.execute("SELECT * from CUSTOMER ORDER BY DATE DESC")
        else:
            text = text + "%"
            c = conn.execute("SELECT * from CUSTOMER where NAME like ? OR PHONE LIKE ? "
                             "OR CHASSIS LIKE ? ORDER BY DATE DESC", (text, text, text,))

        for r in c:
            Begindate = datetime.strptime(str(r[3]), "%Y-%m-%d")

            date1 = Begindate.date() + timedelta(days=60)
            date2 = Begindate.date() + timedelta(days=180)
            date3 = Begindate.date() + timedelta(days=360)

            day1 = date1 - today
            day2 = date2 - today
            day3 = date3 - today

            d1 = day1.days
            d2 = day2.days
            d3 = day3.days

            self.ui.table2.setItem(row_index, 0, QTableWidgetItem(str(row_index + 1)))
            self.ui.table2.setItem(row_index, 1, QTableWidgetItem(str(r[0])))
            self.ui.table2.setItem(row_index, 2, QTableWidgetItem(str(r[1])))
            self.ui.table2.setItem(row_index, 3, QTableWidgetItem(str(r[2])))
            self.ui.table2.setItem(row_index, 4, QTableWidgetItem(str(r[3])))
            self.ui.table2.setItem(row_index, 5, QTableWidgetItem(str(date1)))
            self.ui.table2.setItem(row_index, 6, QTableWidgetItem(str(d1)))
            self.ui.table2.setItem(row_index, 7, QTableWidgetItem(str(date2)))
            self.ui.table2.setItem(row_index, 8, QTableWidgetItem(str(d2)))
            self.ui.table2.setItem(row_index, 9, QTableWidgetItem(str(date3)))
            self.ui.table2.setItem(row_index, 10, QTableWidgetItem(str(d3)))
            row_index += 1

        self.ui.table2.setAlternatingRowColors(1)
        self.ui.table2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.table2.setRowCount(row_index)
        self.ui.table2.customContextMenuRequested.connect(self.generateMenu)
        self.ui.table2.viewport().installEventFilter(self)

    def eventFilter(self, source, event):
        global menuflag, key
        if (event.type() == QtCore.QEvent.MouseButtonPress and
                event.buttons() == QtCore.Qt.RightButton and
                source is self.ui.table2.viewport()):
            try:
                mousePosition = event.pos()
                row = self.ui.table2.rowAt(mousePosition.y())
                if row >= 0:
                    menuflag = 1
                    key = self.ui.table2.item(row, 3).text()
                    d = QAction('Delete', self)
                    d.triggered.connect(lambda: self.delete(key))
                    e = QAction('Edit', self)
                    e.triggered.connect(lambda: self.edit(key))
                    self.menu = QMenu(self)
                    self.menu.addAction(d)
                    self.menu.addAction(e)
                else:
                    menuflag = 0
            except:
                pass
        return super(window, self).eventFilter(source, event)

    def generateMenu(self, pos):
        global menuflag
        if menuflag == 1:
            self.menu.exec_(self.ui.table2.mapToGlobal(pos))

    def delete(self, key):
        self.menu.clear()
        self.showDialog(key)

    def edit(self, key):
        self.menu.clear()
        x = InputDialog()
        x.setWindowTitle("Edit")
        icon = resource_path("icon.ico")
        x.setWindowIcon(QtGui.QIcon(icon))
        x.exec_()
        self.loadProducts2("")

    def showDialog(self, key):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        icon = resource_path("icon.ico")
        msgBox.setWindowIcon(QtGui.QIcon(icon))
        msgBox.setWindowTitle("Confirm deletion")
        msgBox.setText("Are you sure you want to delete this item ?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            query = 'delete from CUSTOMER where CHASSIS=?'
            conn.execute(query, (key.strip(),))
            conn.commit()
            self.loadProducts2("")


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.setWindowTitle("ServiceReminder")
    icon = resource_path("icon.ico")
    win.setWindowIcon(QtGui.QIcon(icon))
    win.show()
    sys.exit(app.exec_())


create_app()
