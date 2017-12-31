# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog

from GLWidget import GLWidget

from OpenGL import GL


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setFixedSize(1000, 600)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1001, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.sceneOpenGLWidget = GLWidget(self.layoutWidget,
                                          self.layoutWidget.frameGeometry().width(),
                                          self.layoutWidget.frameGeometry().height())
        self.sceneOpenGLWidget.setEnabled(True)
        self.sceneOpenGLWidget.setObjectName("sceneOpenGLWidget")

        self.gridLayout_2.addWidget(self.sceneOpenGLWidget, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 410, 1001, 161))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem5, 0, 0, 1, 1)

        self.graphObjectComboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.graphObjectComboBox.setObjectName("graphObjectComboBox")
        self.gridLayout_4.addWidget(self.graphObjectComboBox, 1, 0, 1, 1)

        self.graphObjectLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.graphObjectLabel.setObjectName("graphObjectLabel")
        self.gridLayout_4.addWidget(self.graphObjectLabel, 2, 0, 1, 1)

        spacerItem6 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem6, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget1)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 0, 2, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.objectXDial = QtWidgets.QDial(self.layoutWidget1)
        self.objectXDial.setObjectName("objectXDial")
        self.gridLayout_5.addWidget(self.objectXDial, 0, 0, 1, 1)

        self.objectXLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.objectXLabel.setObjectName("objectXLabel")
        self.gridLayout_5.addWidget(self.objectXLabel, 1, 0, 1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_5, 0, 3, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")

        self.objectYDial = QtWidgets.QDial(self.layoutWidget1)
        self.objectYDial.setObjectName("objectYDial")
        self.gridLayout_6.addWidget(self.objectYDial, 0, 0, 1, 1)

        self.objectYLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.objectYLabel.setObjectName("objectYLabel")
        self.gridLayout_6.addWidget(self.objectYLabel, 1, 0, 1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_6, 0, 4, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")

        self.objectZDial = QtWidgets.QDial(self.layoutWidget1)
        self.objectZDial.setObjectName("objectZDial")
        self.gridLayout_7.addWidget(self.objectZDial, 0, 0, 1, 1)

        self.objectZLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.objectZLabel.setObjectName("objectZLabel")
        self.gridLayout_7.addWidget(self.objectZLabel, 1, 0, 1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_7, 0, 5, 1, 1)
        self.line = QtWidgets.QFrame(self.layoutWidget1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 0, 6, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem7 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_8.addItem(spacerItem7, 0, 0, 1, 1)

        self.hidePushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.hidePushButton.setObjectName("hidePushButton")
        self.gridLayout_8.addWidget(self.hidePushButton, 1, 0, 1, 1)
        self.modifyPushButton = QtWidgets.QPushButton(self.layoutWidget1)

        self.modifyPushButton.setObjectName("modifyPushButton")
        self.gridLayout_8.addWidget(self.modifyPushButton, 2, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

        self.gridLayout_8.addItem(spacerItem8, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_8, 0, 7, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget1)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 0, 9, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setSpacing(6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_12.setSpacing(6)
        self.gridLayout_12.setObjectName("gridLayout_12")
        spacerItem9 = QtWidgets.QSpacerItem(15, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_12.addItem(spacerItem9, 2, 0, 1, 1)
        self.zoomVerticalSlider = QtWidgets.QSlider(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomVerticalSlider.sizePolicy().hasHeightForWidth())

        self.zoomVerticalSlider.setSizePolicy(sizePolicy)
        self.zoomVerticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.zoomVerticalSlider.setObjectName("zoomVerticalSlider")
        self.gridLayout_12.addWidget(self.zoomVerticalSlider, 1, 0, 1, 1)

        spacerItem10 = QtWidgets.QSpacerItem(15, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_12.addItem(spacerItem10, 0, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem11, 1, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_12, 0, 1, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName("gridLayout_9")

        self.povFieldLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.povFieldLabel.setObjectName("povFieldLabel")
        self.gridLayout_9.addWidget(self.povFieldLabel, 6, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem12, 0, 0, 1, 1)

        self.zoomLcdNumber = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.zoomLcdNumber.setObjectName("zoomLcdNumber")
        self.gridLayout_9.addWidget(self.zoomLcdNumber, 1, 0, 1, 1)

        self.zoomLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.zoomLabel.setObjectName("zoomLabel")
        self.gridLayout_9.addWidget(self.zoomLabel, 3, 0, 1, 1)

        spacerItem13 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem13, 8, 0, 1, 1)
        self.povFieldLcdNumber = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.povFieldLcdNumber.setObjectName("povFieldLcdNumber")

        self.gridLayout_9.addWidget(self.povFieldLcdNumber, 5, 0, 1, 1)
        self.povFieldHorizontalSlider = QtWidgets.QSlider(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.povFieldHorizontalSlider.sizePolicy().hasHeightForWidth())

        self.povFieldHorizontalSlider.setSizePolicy(sizePolicy)
        self.povFieldHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.povFieldHorizontalSlider.setObjectName("povFieldHorizontalSlider")

        self.gridLayout_9.addWidget(self.povFieldHorizontalSlider, 7, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_9.addItem(spacerItem14, 4, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_9.addLayout(self.gridLayout_10, 9, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_11, 0, 10, 1, 1)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuLoad = QtWidgets.QMenu(self.menuFile)
        self.menuLoad.setObjectName("menuLoad")
        self.menuSave = QtWidgets.QMenu(self.menuFile)
        self.menuSave.setObjectName("menuSave")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setWhatsThis("")
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.triggered.connect(self.closeMainWindow)

        self.actionObject = QtWidgets.QAction(MainWindow)
        self.actionObject.setObjectName("actionObject")
        self.actionObject.setShortcut('Ctrl+O')
        self.actionObject.triggered.connect(self.openFileNamesDialog)

        self.actionModel = QtWidgets.QAction(MainWindow)
        self.actionModel.setObjectName("actionModel")

        self.actionObject_2 = QtWidgets.QAction(MainWindow)
        self.actionObject_2.setObjectName("actionObject_2")
        self.actionObject_2.setShortcut('Ctrl+S')
        self.actionObject_2.triggered.connect(self.saveFileDialog)

        self.actionModel_2 = QtWidgets.QAction(MainWindow)
        self.actionModel_2.setObjectName("actionModel_2")
        self.actionPredefined_Forms = QtWidgets.QAction(MainWindow)
        self.actionPredefined_Forms.setObjectName("actionPredefined_Forms")
        self.actionPredefined_Scenes = QtWidgets.QAction(MainWindow)
        self.actionPredefined_Scenes.setObjectName("actionPredefined_Scenes")
        self.actionObject_3 = QtWidgets.QAction(MainWindow)
        self.actionObject_3.setObjectName("actionObject_3")
        self.actionModel_3 = QtWidgets.QAction(MainWindow)
        self.actionModel_3.setObjectName("actionModel_3")
        self.actionScene_POV = QtWidgets.QAction(MainWindow)
        self.actionScene_POV.setObjectName("actionScene_POV")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuLoad.addAction(self.actionObject)
        self.menuLoad.addAction(self.actionModel)
        self.menuSave.addAction(self.actionObject_2)
        self.menuSave.addAction(self.actionModel_2)
        self.menuFile.addAction(self.menuLoad.menuAction())
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionObject_3)
        self.menuEdit.addAction(self.actionModel_3)
        self.menuTools.addAction(self.actionPredefined_Forms)
        self.menuTools.addAction(self.actionPredefined_Scenes)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "G2-F"))
        self.graphObjectLabel.setText(_translate("MainWindow", "Object on Scene"))
        self.objectXLabel.setText(_translate("MainWindow", "Rotate   X"))
        self.objectYLabel.setText(_translate("MainWindow", "Rotate   Y"))
        self.objectZLabel.setText(_translate("MainWindow", "Rotate   Z"))
        self.hidePushButton.setText(_translate("MainWindow", "Hide"))
        self.modifyPushButton.setText(_translate("MainWindow", "Modify"))
        self.povFieldLabel.setText(_translate("MainWindow", "POV Field"))
        self.zoomLabel.setText(_translate("MainWindow", "Zoom Ratio"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuLoad.setTitle(_translate("MainWindow", "Load"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionObject.setText(_translate("MainWindow", "Object"))
        self.actionModel.setText(_translate("MainWindow", "Model"))
        self.actionObject_2.setText(_translate("MainWindow", "Object"))
        self.actionModel_2.setText(_translate("MainWindow", "Model"))
        self.actionPredefined_Forms.setText(_translate("MainWindow", "Predefined Objects"))
        self.actionPredefined_Scenes.setText(_translate("MainWindow", "Predefined Scenes"))
        self.actionObject_3.setText(_translate("MainWindow", "Object"))
        self.actionModel_3.setText(_translate("MainWindow", "Model"))
        self.actionScene_POV.setText(_translate("MainWindow", "Scene POV"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def closeMainWindow(self):
        exit()

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(None, "Abrir", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(None, "Guardar", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

