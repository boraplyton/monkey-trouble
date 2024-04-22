# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'init.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 900, 800))
        self.stackedWidget.setObjectName("stackedWidget")
        self.init_menu = QtWidgets.QWidget()
        self.init_menu.setObjectName("init_menu")
        self.gridLayoutWidget = QtWidgets.QWidget(self.init_menu)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 901, 801))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        self.btn_setings_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.btn_setings_2.setFont(font)
        self.btn_setings_2.setObjectName("btn_setings_2")
        self.gridLayout.addWidget(self.btn_setings_2, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(50, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 4, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(50, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 3, 1, 2)
        self.btn_play_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.btn_play_2.setFont(font)
        self.btn_play_2.setObjectName("btn_play_2")
        self.gridLayout.addWidget(self.btn_play_2, 1, 1, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 2, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 0, 2, 1, 1)
        self.stackedWidget.addWidget(self.init_menu)
        self.level = QtWidgets.QWidget()
        self.level.setObjectName("level")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.level)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 901, 801))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 2, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 2, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem9, 0, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem10, 3, 1, 1, 1)
        self.label_scope = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_scope.setFont(font)
        self.label_scope.setObjectName("label_scope")
        self.gridLayout_3.addWidget(self.label_scope, 1, 1, 1, 1)
        self.tableView = QtWidgets.QTableView(self.gridLayoutWidget_2)
        self.tableView.setObjectName("tableView")
        self.gridLayout_3.addWidget(self.tableView, 2, 1, 1, 1)
        self.btn_back_level = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.btn_back_level.setFont(font)
        self.btn_back_level.setObjectName("btn_back_level")
        self.gridLayout_3.addWidget(self.btn_back_level, 3, 2, 1, 1)
        self.stackedWidget.addWidget(self.level)
        self.setings = QtWidgets.QWidget()
        self.setings.setObjectName("setings")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.setings)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 901, 801))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem11, 2, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem12, 2, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem13, 3, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem14, 0, 1, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.gridLayoutWidget_3)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_4.addWidget(self.horizontalSlider, 2, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btn_back_setings = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.btn_back_setings.setFont(font)
        self.btn_back_setings.setObjectName("btn_back_setings")
        self.gridLayout_5.addWidget(self.btn_back_setings, 1, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem15, 0, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem16, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 3, 2, 1, 1)
        self.stackedWidget.addWidget(self.setings)
        self.win = QtWidgets.QWidget()
        self.win.setObjectName("win")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.win)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 901, 801))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem17 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem17, 0, 0, 1, 1)
        self.btn_reset = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(21)
        self.btn_reset.setFont(font)
        self.btn_reset.setObjectName("btn_reset")
        self.gridLayout_8.addWidget(self.btn_reset, 0, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem18, 0, 2, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(250, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_8.addItem(spacerItem19, 1, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_8, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.win)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_setings_2.setText(_translate("MainWindow", "Setings"))
        self.btn_play_2.setText(_translate("MainWindow", "Play"))
        self.label_scope.setText(_translate("MainWindow", "Scope:"))
        self.btn_back_level.setText(_translate("MainWindow", "Back"))
        self.label_2.setText(_translate("MainWindow", "Music"))
        self.btn_back_setings.setText(_translate("MainWindow", "Back"))
        self.label_3.setText(_translate("MainWindow", "Вы победили!!!"))
        self.btn_reset.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
