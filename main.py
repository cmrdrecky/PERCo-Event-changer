# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 480)
        MainWindow.setMinimumSize(QtCore.QSize(619, 473))
        MainWindow.setMaximumSize(QtCore.QSize(620, 486))
        MainWindow.setStyleSheet("QFrame {    \n"
"    background-color: rgb(56, 58, 89);    \n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setGeometry(QtCore.QRect(0, -10, 651, 501))
        self.dropShadowFrame.setStyleSheet("QFrame {    \n"
"    background-color: rgb(56, 58, 89);    \n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.frame_grip = QtWidgets.QFrame(self.dropShadowFrame)
        self.frame_grip.setGeometry(QtCore.QRect(50, 470, 581, 25))
        self.frame_grip.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_grip.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_grip.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_label_bottom = QtWidgets.QFrame(self.frame_grip)
        self.frame_label_bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_bottom.setObjectName("frame_label_bottom")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_size_grip = QtWidgets.QFrame(self.frame_label_bottom)
        self.frame_size_grip.setMaximumSize(QtCore.QSize(13, 20))
        self.frame_size_grip.setStyleSheet("QSizeGrip {\n"
"    background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_size_grip.setObjectName("frame_size_grip")
        self.horizontalLayout_7.addWidget(self.frame_size_grip)
        self.label_credits = QtWidgets.QLabel(self.frame_label_bottom)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_credits.setObjectName("label_credits")
        self.horizontalLayout_7.addWidget(self.label_credits)
        self.label_version = QtWidgets.QLabel(self.frame_label_bottom)
        self.label_version.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_version.setFont(font)
        self.label_version.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_version.setObjectName("label_version")
        self.horizontalLayout_7.addWidget(self.label_version)
        self.label_version.raise_()
        self.label_credits.raise_()
        self.frame_size_grip.raise_()
        self.horizontalLayout_6.addWidget(self.frame_label_bottom)
        self.frame_back_menu = QtWidgets.QFrame(self.dropShadowFrame)
        self.frame_back_menu.setGeometry(QtCore.QRect(-10, 10, 71, 491))
        self.frame_back_menu.setStyleSheet("background-color: rgb(28, 31, 37);\n"
"border-radius: 0px;")
        self.frame_back_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_back_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_back_menu.setObjectName("frame_back_menu")
        self.frame_toggle = QtWidgets.QFrame(self.frame_back_menu)
        self.frame_toggle.setGeometry(QtCore.QRect(10, 20, 61, 41))
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_toggle.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_toggle_menu = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet("QPushButton {\n"
"    background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    border: none;\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_toggle_menu.setText("")
        self.btn_toggle_menu.setObjectName("btn_toggle_menu")
        self.verticalLayout_3.addWidget(self.btn_toggle_menu)
        self.frame_extra_menus = QtWidgets.QFrame(self.frame_back_menu)
        self.frame_extra_menus.setGeometry(QtCore.QRect(10, 350, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy)
        self.frame_extra_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_extra_menus.setObjectName("frame_extra_menus")
        self.layout_menu_bottom = QtWidgets.QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName("layout_menu_bottom")
        self.label_user_icon = QtWidgets.QLabel(self.frame_back_menu)
        self.label_user_icon.setGeometry(QtCore.QRect(10, 420, 60, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy)
        self.label_user_icon.setMinimumSize(QtCore.QSize(60, 60))
        self.label_user_icon.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_user_icon.setFont(font)
        self.label_user_icon.setStyleSheet("QLabel {\n"
"    border-radius: 30px;\n"
"    background-color: rgb(44, 49, 60);\n"
"    border: 3px solid rgb(39, 44, 54);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"QLabel:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}")
        self.label_user_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user_icon.setObjectName("label_user_icon")
        self.frame_div_content_1 = QtWidgets.QFrame(self.dropShadowFrame)
        self.frame_div_content_1.setGeometry(QtCore.QRect(70, 40, 541, 110))
        self.frame_div_content_1.setMinimumSize(QtCore.QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QtCore.QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet("background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_div_content_1.setObjectName("frame_div_content_1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_title_wid_1 = QtWidgets.QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setMaximumSize(QtCore.QSize(16777215, 33))
        self.frame_title_wid_1.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title_wid_1.setObjectName("frame_title_wid_1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.labelBoxBlenderInstalation = QtWidgets.QLabel(self.frame_title_wid_1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet("")
        self.labelBoxBlenderInstalation.setObjectName("labelBoxBlenderInstalation")
        self.verticalLayout_8.addWidget(self.labelBoxBlenderInstalation)
        self.verticalLayout_7.addWidget(self.frame_title_wid_1)
        self.frame_content_wid_1 = QtWidgets.QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_wid_1.setObjectName("frame_content_wid_1")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_content_wid_1)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.frame_content_wid_1)
        self.dateEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(27, 29, 35);\n"
"border: 2px solid rgb(91, 101, 124);")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 2, 1, 1, 1)
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())  # ????????, ?????? ?????????? ???????????????????? ?????? ????????????
        self.dateEdit.setMaximumDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime.currentDateTime().addDays(-40))
        #self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 10, 11), QtCore.QTime(0, 0, 0)))
        self.labelBoxBlenderInstalation_3 = QtWidgets.QLabel(self.frame_content_wid_1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_3.setFont(font)
        self.labelBoxBlenderInstalation_3.setStyleSheet("")
        self.labelBoxBlenderInstalation_3.setObjectName("labelBoxBlenderInstalation_3")
        self.gridLayout.addWidget(self.labelBoxBlenderInstalation_3, 2, 0, 1, 1)
        self.horizontalLayout_9.addLayout(self.gridLayout)
        self.pushButton = QtWidgets.QPushButton(self.frame_content_wid_1)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"\n"
"    color: rgb(255,255,255);\n"
"    border: 1px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/20x20/icons/20x20/cil-check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_9.addWidget(self.pushButton)
        self.verticalLayout_7.addWidget(self.frame_content_wid_1)
        self.frame_title_wid_2 = QtWidgets.QFrame(self.dropShadowFrame)
        self.frame_title_wid_2.setGeometry(QtCore.QRect(70, 160, 541, 221))
        self.frame_title_wid_2.setMaximumSize(QtCore.QSize(16777215, 350))
        self.frame_title_wid_2.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title_wid_2.setObjectName("frame_title_wid_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_title_wid_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.labelBoxBlenderInstalation_2 = QtWidgets.QLabel(self.frame_title_wid_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_2.setFont(font)
        self.labelBoxBlenderInstalation_2.setStyleSheet("")
        self.labelBoxBlenderInstalation_2.setObjectName("labelBoxBlenderInstalation_2")
        self.verticalLayout_9.addWidget(self.labelBoxBlenderInstalation_2)
        self.tableWidget = QtWidgets.QTableWidget(self.frame_title_wid_2)
        self.tableWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setStyleSheet("color: rgb(255, 0, 0);\n"
"QTableWidget {\n"
"    background-color: rgb(39, 44, 54);\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.verticalLayout_9.addWidget(self.tableWidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.dropShadowFrame)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 390, 150, 30))
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255,255,255);\n"
"    border: 1px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/20x20/icons/20x20/cil-pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PERCo-S-20 Event changer"))
        self.label_credits.setText(_translate("MainWindow", "?????????????? ?? ?????????????? ?????????????? ?? ?????????????????? ?? ???????????? ?????????????????????? ???????? ???? ???????? ??????????????????????"))
        self.label_version.setText(_translate("MainWindow", "v1.0.0"))
        self.label_user_icon.setText(_translate("MainWindow", "????????????"))
        self.labelBoxBlenderInstalation.setText(_translate("MainWindow", "?????????????? ???????? ????????????:"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "??????????????"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "??????"))
        self.labelBoxBlenderInstalation_3.setText(_translate("MainWindow", "???????????????? ???????? ??????????????????:"))
        self.pushButton.setText(_translate("MainWindow", "???????????? ????????????"))
        self.labelBoxBlenderInstalation_2.setText(_translate("MainWindow", "???????????????? ?????????????? ????????, ?????????????? ???????????????????? ??????????????????:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "????????"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "?????????? ??????????????"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ID ????????????????????"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "??????????????"))
        self.pushButton_2.setText(_translate("MainWindow", "???????????????? ??????????????"))
import files
