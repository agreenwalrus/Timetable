# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maininfo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 618)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget_day = QtWidgets.QTableWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tableWidget_day.sizePolicy().hasHeightForWidth())
        self.tableWidget_day.setSizePolicy(sizePolicy)
        self.tableWidget_day.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_day.setRowCount(0)
        self.tableWidget_day.setColumnCount(0)
        self.tableWidget_day.setObjectName("tableWidget_day")
        self.tableWidget_day.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_day.horizontalHeader().setHighlightSections(True)
        self.tableWidget_day.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_day.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget_day.verticalHeader().setStretchLastSection(False)
        self.gridLayout_2.addWidget(self.tableWidget_day, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidget_time = QtWidgets.QTableWidget(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tableWidget_time.sizePolicy().hasHeightForWidth())
        self.tableWidget_time.setSizePolicy(sizePolicy)
        self.tableWidget_time.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_time.setObjectName("tableWidget_time")
        self.tableWidget_time.setColumnCount(0)
        self.tableWidget_time.setRowCount(0)
        self.tableWidget_time.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_time.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.tableWidget_time, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableWidget_subject = QtWidgets.QTableWidget(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tableWidget_subject.sizePolicy().hasHeightForWidth())
        self.tableWidget_subject.setSizePolicy(sizePolicy)
        self.tableWidget_subject.setObjectName("tableWidget_subject")
        self.tableWidget_subject.setColumnCount(0)
        self.tableWidget_subject.setRowCount(0)
        self.tableWidget_subject.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_subject.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_5.addWidget(self.tableWidget_subject, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_room = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_room.setGeometry(QtCore.QRect(10, 10, 753, 328))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tableWidget_room.sizePolicy().hasHeightForWidth())
        self.tableWidget_room.setSizePolicy(sizePolicy)
        self.tableWidget_room.setObjectName("tableWidget_room")
        self.tableWidget_room.setColumnCount(0)
        self.tableWidget_room.setRowCount(0)
        self.tableWidget_room.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_room.horizontalHeader().setStretchLastSection(True)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tableWidget_form = QtWidgets.QTableWidget(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tableWidget_form.sizePolicy().hasHeightForWidth())
        self.tableWidget_form.setSizePolicy(sizePolicy)
        self.tableWidget_form.setObjectName("tableWidget_form")
        self.tableWidget_form.setColumnCount(0)
        self.tableWidget_form.setRowCount(0)
        self.tableWidget_form.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_form.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_7.addWidget(self.tableWidget_form, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_13)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget_teacher = QtWidgets.QTableWidget(self.tab_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tableWidget_teacher.sizePolicy().hasHeightForWidth())
        self.tableWidget_teacher.setSizePolicy(sizePolicy)
        self.tableWidget_teacher.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_teacher.setObjectName("tableWidget_teacher")
        self.tableWidget_teacher.setColumnCount(0)
        self.tableWidget_teacher.setRowCount(0)
        self.tableWidget_teacher.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget_teacher, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_13, "")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.button_edit = QtWidgets.QPushButton(self.splitter)
        self.button_edit.setObjectName("button_edit")
        self.button_add = QtWidgets.QPushButton(self.splitter)
        self.button_add.setObjectName("button_add")
        self.button_delete = QtWidgets.QPushButton(self.splitter)
        self.button_delete.setObjectName("button_delete")
        self.button_next = QtWidgets.QPushButton(self.splitter_2)
        self.button_next.setObjectName("button_next")
        self.progressBar = QtWidgets.QProgressBar(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.progressBar.setFont(font)
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.progressBar.setMaximum(99)
        self.progressBar.setProperty("value", 33)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.splitter_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget_day.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Дни"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Время"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Предметы"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Аудитории"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Классы"))
        self.tableWidget_teacher.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), _translate("MainWindow", "Преподаватель"))
        self.button_edit.setText(_translate("MainWindow", "Редактировать"))
        self.button_add.setText(_translate("MainWindow", "Добавить"))
        self.button_delete.setText(_translate("MainWindow", "Удалить"))
        self.button_next.setText(_translate("MainWindow", "Далее"))
        self.progressBar.setFormat(_translate("MainWindow", "1 из 3"))
