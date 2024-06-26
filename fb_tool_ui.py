# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\fb_tool_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(961, 578)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_cookie = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cookie.setGeometry(QtCore.QRect(50, 90, 141, 25))
        self.btn_cookie.setObjectName("btn_cookie")
        self.btn_id = QtWidgets.QPushButton(self.centralwidget)
        self.btn_id.setGeometry(QtCore.QRect(50, 130, 141, 25))
        self.btn_id.setStyleSheet("\n"
"                        QPushButton {\n"
"                            background-color: #3498db; /* Red */\n"
"                            color: white;\n"
"                            border-radius: 5px;\n"
"                            border: 2px solid #3498db;\n"
"                        }\n"
"\n"
"                        QPushButton:hover {\n"
"                            background-color: #2980b9; /* Darker Red */\n"
"                            border: 2px solid #2980b9;\n"
"                        }\n"
"                    ")
        self.btn_id.setObjectName("btn_id")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 200, 891, 341))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 11, 921, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.lbl_cookie = QtWidgets.QLabel(self.centralwidget)
        self.lbl_cookie.setGeometry(QtCore.QRect(210, 90, 681, 31))
        self.lbl_cookie.setStyleSheet("")
        self.lbl_cookie.setObjectName("lbl_cookie")
        self.lbl_id = QtWidgets.QLabel(self.centralwidget)
        self.lbl_id.setGeometry(QtCore.QRect(210, 130, 681, 31))
        self.lbl_id.setStyleSheet("")
        self.lbl_id.setObjectName("lbl_id")
        self.btn_run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run.setGeometry(QtCore.QRect(50, 170, 141, 25))
        self.btn_run.setObjectName("btn_run")
        self.lbl_tab = QtWidgets.QLabel(self.centralwidget)
        self.lbl_tab.setGeometry(QtCore.QRect(60, 10, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_tab.setFont(font)
        self.lbl_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_tab.setObjectName("lbl_tab")
        self.txt_tab = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_tab.setGeometry(QtCore.QRect(50, 40, 141, 31))
        self.txt_tab.setObjectName("txt_tab")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(410, 170, 141, 25))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_export = QtWidgets.QPushButton(self.centralwidget)
        self.btn_export.setGeometry(QtCore.QRect(750, 170, 141, 25))
        self.btn_export.setStyleSheet("\n"
"                        QPushButton {\n"
"                            background-color: #3498db; /* Red */\n"
"                            color: white;\n"
"                            border-radius: 5px;\n"
"                            border: 2px solid #3498db;\n"
"                        }\n"
"\n"
"                        QPushButton:hover {\n"
"                            background-color: #2980b9; /* Darker Red */\n"
"                            border: 2px solid #2980b9;\n"
"                        }\n"
"                    ")
        self.btn_export.setObjectName("btn_export")
        self.lbl_notification = QtWidgets.QLabel(self.centralwidget)
        self.lbl_notification.setGeometry(QtCore.QRect(410, 40, 271, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_notification.sizePolicy().hasHeightForWidth())
        self.lbl_notification.setSizePolicy(sizePolicy)
        self.lbl_notification.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0)")
        self.lbl_notification.setObjectName("lbl_notification")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FB Add Friend"))
        self.btn_cookie.setStyleSheet(_translate("MainWindow", "\n"
"                        QPushButton {\n"
"                            background-color: #3498db; /* Blue */\n"
"                            color: white;\n"
"                            border-radius: 5px;\n"
"                            border: 2px solid #3498db;\n"
"                        }\n"
"\n"
"                        QPushButton:hover {\n"
"                            background-color: #2980b9; /* Darker Blue */\n"
"                            border: 2px solid #2980b9;\n"
"                        }\n"
"                    "))
        self.btn_cookie.setText(_translate("MainWindow", "Import Cookie"))
        self.btn_id.setText(_translate("MainWindow", "Import Friend"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pass"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cookie"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status Cookie"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status"))
        self.lbl_cookie.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_id.setText(_translate("MainWindow", "TextLabel"))
        self.btn_run.setStyleSheet(_translate("MainWindow", "\n"
"                        QPushButton {\n"
"                            background-color: #2ecc71; /* Green */\n"
"                            color: white;\n"
"                            border-radius: 5px;\n"
"                            border: 2px solid #2ecc71;\n"
"                        }\n"
"\n"
"                        QPushButton:hover {\n"
"                            background-color: #27ae60; /* Darker Green */\n"
"                            border: 2px solid #27ae60;\n"
"                        }\n"
"                    "))
        self.btn_run.setText(_translate("MainWindow", "Run"))
        self.lbl_tab.setText(_translate("MainWindow", "Tab number"))
        self.btn_stop.setStyleSheet(_translate("MainWindow", "\n"
"                        QPushButton {\n"
"                            background-color: #e74c3c; /* Red */\n"
"                            color: white;\n"
"                            border-radius: 5px;\n"
"                            border: 2px solid #e74c3c;\n"
"                        }\n"
"\n"
"                        QPushButton:hover {\n"
"                            background-color: #c0392b; /* Darker Red */\n"
"                            border: 2px solid #c0392b;\n"
"                        }\n"
"                    "))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.btn_export.setText(_translate("MainWindow", "Export Excel"))
        self.lbl_notification.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
