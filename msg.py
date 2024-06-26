# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msg.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(930, 612)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 921, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 200, 911, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 901, 321))
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
        self.btn_stop = QtWidgets.QPushButton(self.tab)
        self.btn_stop.setGeometry(QtCore.QRect(380, 150, 141, 41))
        self.btn_stop.setObjectName("btn_stop")
        self.lbl_cookie = QtWidgets.QLabel(self.tab)
        self.lbl_cookie.setGeometry(QtCore.QRect(190, 50, 681, 31))
        self.lbl_cookie.setStyleSheet("")
        self.lbl_cookie.setObjectName("lbl_cookie")
        self.btn_run = QtWidgets.QPushButton(self.tab)
        self.btn_run.setGeometry(QtCore.QRect(30, 150, 141, 41))
        self.btn_run.setObjectName("btn_run")
        self.btn_cookie = QtWidgets.QPushButton(self.tab)
        self.btn_cookie.setGeometry(QtCore.QRect(30, 40, 141, 41))
        self.btn_cookie.setObjectName("btn_cookie")
        self.lbl_notification = QtWidgets.QLabel(self.tab)
        self.lbl_notification.setGeometry(QtCore.QRect(200, 10, 571, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_notification.sizePolicy().hasHeightForWidth())
        self.lbl_notification.setSizePolicy(sizePolicy)
        self.lbl_notification.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0)")
        self.lbl_notification.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_notification.setObjectName("lbl_notification")
        self.btn_export = QtWidgets.QPushButton(self.tab)
        self.btn_export.setGeometry(QtCore.QRect(730, 150, 141, 41))
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
        self.txt_thread = QtWidgets.QLineEdit(self.tab)
        self.txt_thread.setGeometry(QtCore.QRect(30, 111, 141, 31))
        self.txt_thread.setObjectName("txt_thread")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(50, 90, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.btn_export_2 = QtWidgets.QPushButton(self.tab_3)
        self.btn_export_2.setGeometry(QtCore.QRect(720, 360, 141, 41))
        self.btn_export_2.setStyleSheet("\n"
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
        self.btn_export_2.setObjectName("btn_export_2")
        self.tableWidget_page = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_page.setGeometry(QtCore.QRect(10, 240, 901, 321))
        self.tableWidget_page.setObjectName("tableWidget_page")
        self.tableWidget_page.setColumnCount(1)
        self.tableWidget_page.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setHorizontalHeaderItem(0, item)
        self.btn_run_page = QtWidgets.QPushButton(self.tab_3)
        self.btn_run_page.setGeometry(QtCore.QRect(20, 170, 141, 41))
        self.btn_run_page.setObjectName("btn_run_page")
        self.btn_stop_page = QtWidgets.QPushButton(self.tab_3)
        self.btn_stop_page.setGeometry(QtCore.QRect(350, 170, 141, 41))
        self.btn_stop_page.setObjectName("btn_stop_page")
        self.btn_cookie_page = QtWidgets.QPushButton(self.tab_3)
        self.btn_cookie_page.setGeometry(QtCore.QRect(20, 30, 141, 41))
        self.btn_cookie_page.setObjectName("btn_cookie_page")
        self.lbl_cookie_page = QtWidgets.QLabel(self.tab_3)
        self.lbl_cookie_page.setGeometry(QtCore.QRect(170, 30, 681, 31))
        self.lbl_cookie_page.setStyleSheet("")
        self.lbl_cookie_page.setObjectName("lbl_cookie_page")
        self.btn_export_page = QtWidgets.QPushButton(self.tab_3)
        self.btn_export_page.setGeometry(QtCore.QRect(690, 170, 141, 41))
        self.btn_export_page.setStyleSheet("\n"
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
        self.btn_export_page.setObjectName("btn_export_page")
        self.txt_group_page = QtWidgets.QTextEdit(self.tab_3)
        self.txt_group_page.setGeometry(QtCore.QRect(170, 100, 731, 31))
        self.txt_group_page.setObjectName("txt_group_page")
        self.lbl_notification_5 = QtWidgets.QLabel(self.tab_3)
        self.lbl_notification_5.setGeometry(QtCore.QRect(20, 100, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_notification_5.sizePolicy().hasHeightForWidth())
        self.lbl_notification_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_notification_5.setFont(font)
        self.lbl_notification_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0)")
        self.lbl_notification_5.setObjectName("lbl_notification_5")
        self.lbl_notification_page = QtWidgets.QLabel(self.tab_3)
        self.lbl_notification_page.setGeometry(QtCore.QRect(220, 0, 541, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_notification_page.sizePolicy().hasHeightForWidth())
        self.lbl_notification_page.setSizePolicy(sizePolicy)
        self.lbl_notification_page.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0)")
        self.lbl_notification_page.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_notification_page.setObjectName("lbl_notification_page")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lbl_tab_2 = QtWidgets.QLabel(self.tab_2)
        self.lbl_tab_2.setGeometry(QtCore.QRect(560, 220, 121, 30))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_tab_2.setFont(font)
        self.lbl_tab_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_tab_2.setObjectName("lbl_tab_2")
        self.txt_msg = QtWidgets.QTextEdit(self.tab_2)
        self.txt_msg.setGeometry(QtCore.QRect(320, 270, 571, 231))
        self.txt_msg.setObjectName("txt_msg")
        self.btn_import_cookie = QtWidgets.QPushButton(self.tab_2)
        self.btn_import_cookie.setGeometry(QtCore.QRect(90, 76, 121, 41))
        self.btn_import_cookie.setStyleSheet("\n"
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
        self.btn_import_cookie.setObjectName("btn_import_cookie")
        self.btn_stop_msg = QtWidgets.QPushButton(self.tab_2)
        self.btn_stop_msg.setGeometry(QtCore.QRect(90, 350, 121, 41))
        self.btn_stop_msg.setObjectName("btn_stop_msg")
        self.btn_image = QtWidgets.QPushButton(self.tab_2)
        self.btn_image.setGeometry(QtCore.QRect(90, 140, 121, 41))
        self.btn_image.setStyleSheet("\n"
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
        self.btn_image.setObjectName("btn_image")
        self.btn_run_msg = QtWidgets.QPushButton(self.tab_2)
        self.btn_run_msg.setGeometry(QtCore.QRect(90, 290, 121, 41))
        self.btn_run_msg.setObjectName("btn_run_msg")
        self.lbl_notification_msg = QtWidgets.QLabel(self.tab_2)
        self.lbl_notification_msg.setGeometry(QtCore.QRect(10, 410, 301, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_notification_msg.sizePolicy().hasHeightForWidth())
        self.lbl_notification_msg.setSizePolicy(sizePolicy)
        self.lbl_notification_msg.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0)")
        self.lbl_notification_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_notification_msg.setObjectName("lbl_notification_msg")
        self.btn_import_list_member = QtWidgets.QPushButton(self.tab_2)
        self.btn_import_list_member.setGeometry(QtCore.QRect(90, 20, 121, 41))
        self.btn_import_list_member.setStyleSheet("\n"
"                        QPushButton {\n"
"                            background-color: #abdbe3; /* Red */\n"
"                            color: black;\n"
"                            border-radius: 5px;\n"
"                            border: 2px solid #abdbe3;\n"
"                        }\n"
"\n"
"                        QPushButton:hover {\n"
"                            background-color: #76b5c5; /* Darker Red */\n"
"                            border: 2px solid #76b5c5;\n"
"                        }\n"
"                    ")
        self.btn_import_list_member.setObjectName("btn_import_list_member")
        self.lbl_members_link = QtWidgets.QLabel(self.tab_2)
        self.lbl_members_link.setGeometry(QtCore.QRect(230, 30, 681, 31))
        self.lbl_members_link.setStyleSheet("")
        self.lbl_members_link.setObjectName("lbl_members_link")
        self.lbl_cookie_link = QtWidgets.QLabel(self.tab_2)
        self.lbl_cookie_link.setGeometry(QtCore.QRect(230, 80, 681, 31))
        self.lbl_cookie_link.setStyleSheet("")
        self.lbl_cookie_link.setObjectName("lbl_cookie_link")
        self.lbl_images_msg = QtWidgets.QLabel(self.tab_2)
        self.lbl_images_msg.setGeometry(QtCore.QRect(230, 140, 681, 31))
        self.lbl_images_msg.setStyleSheet("")
        self.lbl_images_msg.setObjectName("lbl_images_msg")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(100, 219, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_thread_msg = QtWidgets.QLineEdit(self.tab_2)
        self.txt_thread_msg.setGeometry(QtCore.QRect(90, 240, 121, 31))
        self.txt_thread_msg.setObjectName("txt_thread_msg")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Pass"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Cookie"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Status Cookie"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Status"))
        self.btn_stop.setStyleSheet(_translate("Form", "\n"
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
        self.btn_stop.setText(_translate("Form", "Stop"))
        self.lbl_cookie.setText(_translate("Form", "TextLabel"))
        self.btn_run.setStyleSheet(_translate("Form", "\n"
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
        self.btn_run.setText(_translate("Form", "Run"))
        self.btn_cookie.setStyleSheet(_translate("Form", "\n"
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
        self.btn_cookie.setText(_translate("Form", "Import Cookie"))
        self.lbl_notification.setText(_translate("Form", "TextLabel"))
        self.btn_export.setText(_translate("Form", "Export Excel"))
        self.label.setText(_translate("Form", "Number Thread"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.btn_export_2.setText(_translate("Form", "Export Excel"))
        item = self.tableWidget_page.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Link Member"))
        self.btn_run_page.setStyleSheet(_translate("Form", "\n"
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
        self.btn_run_page.setText(_translate("Form", "Run"))
        self.btn_stop_page.setStyleSheet(_translate("Form", "\n"
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
        self.btn_stop_page.setText(_translate("Form", "Stop"))
        self.btn_cookie_page.setStyleSheet(_translate("Form", "\n"
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
        self.btn_cookie_page.setText(_translate("Form", "Import Cookie"))
        self.lbl_cookie_page.setText(_translate("Form", "TextLabel"))
        self.btn_export_page.setText(_translate("Form", "Export Excel"))
        self.lbl_notification_5.setText(_translate("Form", "Nhập link group"))
        self.lbl_notification_page.setText(_translate("Form", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Tab 2"))
        self.lbl_tab_2.setText(_translate("Form", "Message"))
        self.btn_import_cookie.setText(_translate("Form", "Import Cookie"))
        self.btn_stop_msg.setStyleSheet(_translate("Form", "\n"
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
        self.btn_stop_msg.setText(_translate("Form", "Stop"))
        self.btn_image.setText(_translate("Form", "Import Image"))
        self.btn_run_msg.setStyleSheet(_translate("Form", "\n"
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
        self.btn_run_msg.setText(_translate("Form", "Run"))
        self.lbl_notification_msg.setText(_translate("Form", "TextLabel"))
        self.btn_import_list_member.setText(_translate("Form", "Import Member"))
        self.lbl_members_link.setText(_translate("Form", "TextLabel"))
        self.lbl_cookie_link.setText(_translate("Form", "TextLabel"))
        self.lbl_images_msg.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "Number Thread"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
