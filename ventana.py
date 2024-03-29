# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_venPrincipal(object):
    def setupUi(self, venPrincipal):
        venPrincipal.setObjectName("venPrincipal")
        venPrincipal.resize(1150, 886)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(venPrincipal.sizePolicy().hasHeightForWidth())
        venPrincipal.setSizePolicy(sizePolicy)
        venPrincipal.setMinimumSize(QtCore.QSize(1150, 0))
        venPrincipal.setAutoFillBackground(False)
        venPrincipal.setStyleSheet("text-align: center;")
        self.centralwidget = QtWidgets.QWidget(venPrincipal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lblstatusdate = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblstatusdate.sizePolicy().hasHeightForWidth())
        self.lblstatusdate.setSizePolicy(sizePolicy)
        self.lblstatusdate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblstatusdate.setObjectName("lblstatusdate")
        self.gridLayout_7.addWidget(self.lblstatusdate, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 1, 4, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1000, 600))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.panelCli = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.panelCli.sizePolicy().hasHeightForWidth())
        self.panelCli.setSizePolicy(sizePolicy)
        self.panelCli.setObjectName("panelCli")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.panelCli)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridFormabajo = QtWidgets.QGridLayout()
        self.gridFormabajo.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridFormabajo.setObjectName("gridFormabajo")
        self.chkTar = QtWidgets.QCheckBox(self.panelCli)
        self.chkTar.setObjectName("chkTar")
        self.grpbtnPay = QtWidgets.QButtonGroup(venPrincipal)
        self.grpbtnPay.setObjectName("grpbtnPay")
        self.grpbtnPay.setExclusive(False)
        self.grpbtnPay.addButton(self.chkTar)
        self.gridFormabajo.addWidget(self.chkTar, 0, 11, 1, 1)
        self.rbtFem = QtWidgets.QRadioButton(self.panelCli)
        self.rbtFem.setObjectName("rbtFem")
        self.grpbtnSex = QtWidgets.QButtonGroup(venPrincipal)
        self.grpbtnSex.setObjectName("grpbtnSex")
        self.grpbtnSex.addButton(self.rbtFem)
        self.gridFormabajo.addWidget(self.rbtFem, 0, 1, 1, 1)
        self.lblSexo = QtWidgets.QLabel(self.panelCli)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblSexo.setFont(font)
        self.lblSexo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblSexo.setObjectName("lblSexo")
        self.gridFormabajo.addWidget(self.lblSexo, 0, 0, 1, 1)
        self.rbtMasc = QtWidgets.QRadioButton(self.panelCli)
        self.rbtMasc.setObjectName("rbtMasc")
        self.grpbtnSex.addButton(self.rbtMasc)
        self.gridFormabajo.addWidget(self.rbtMasc, 0, 2, 1, 1)
        self.lblPago = QtWidgets.QLabel(self.panelCli)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPago.setFont(font)
        self.lblPago.setObjectName("lblPago")
        self.gridFormabajo.addWidget(self.lblPago, 0, 9, 1, 1)
        self.chkEfec = QtWidgets.QCheckBox(self.panelCli)
        self.chkEfec.setObjectName("chkEfec")
        self.grpbtnPay.addButton(self.chkEfec)
        self.gridFormabajo.addWidget(self.chkEfec, 0, 10, 1, 1)
        self.chkTrans = QtWidgets.QCheckBox(self.panelCli)
        self.chkTrans.setObjectName("chkTrans")
        self.grpbtnPay.addButton(self.chkTrans)
        self.gridFormabajo.addWidget(self.chkTrans, 0, 12, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(310, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridFormabajo.addItem(spacerItem3, 0, 5, 1, 1)
        self.lblEdad = QtWidgets.QLabel(self.panelCli)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblEdad.setFont(font)
        self.lblEdad.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEdad.setObjectName("lblEdad")
        self.gridFormabajo.addWidget(self.lblEdad, 0, 3, 1, 1)
        self.spinEdad = QtWidgets.QSpinBox(self.panelCli)
        self.spinEdad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinEdad.setObjectName("spinEdad")
        self.gridFormabajo.addWidget(self.spinEdad, 0, 4, 1, 1)
        self.gridLayout_8.addLayout(self.gridFormabajo, 3, 0, 1, 1)
        self.gridFormdatos = QtWidgets.QGridLayout()
        self.gridFormdatos.setObjectName("gridFormdatos")
        self.editNome = QtWidgets.QLineEdit(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editNome.sizePolicy().hasHeightForWidth())
        self.editNome.setSizePolicy(sizePolicy)
        self.editNome.setStyleSheet("background-color: rgb(255, 255, 229);")
        self.editNome.setObjectName("editNome")
        self.gridFormdatos.addWidget(self.editNome, 0, 4, 1, 1)
        self.lblNome = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNome.sizePolicy().hasHeightForWidth())
        self.lblNome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("lblNome")
        self.gridFormdatos.addWidget(self.lblNome, 0, 3, 1, 1)
        self.lblApel = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblApel.sizePolicy().hasHeightForWidth())
        self.lblApel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblApel.setFont(font)
        self.lblApel.setObjectName("lblApel")
        self.gridFormdatos.addWidget(self.lblApel, 0, 0, 1, 1)
        self.editApel = QtWidgets.QLineEdit(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editApel.sizePolicy().hasHeightForWidth())
        self.editApel.setSizePolicy(sizePolicy)
        self.editApel.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.editApel.setWhatsThis("")
        self.editApel.setAccessibleName("")
        self.editApel.setAccessibleDescription("")
        self.editApel.setStyleSheet("background-color: rgb(255, 255, 229);")
        self.editApel.setInputMethodHints(QtCore.Qt.ImhNone)
        self.editApel.setInputMask("")
        self.editApel.setText("")
        self.editApel.setObjectName("editApel")
        self.gridFormdatos.addWidget(self.editApel, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridFormdatos.addItem(spacerItem4, 0, 2, 1, 1)
        self.gridLayout_8.addLayout(self.gridFormdatos, 1, 0, 1, 1)
        self.gridFormdir = QtWidgets.QGridLayout()
        self.gridFormdir.setObjectName("gridFormdir")
        self.lblProv = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblProv.sizePolicy().hasHeightForWidth())
        self.lblProv.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblProv.setFont(font)
        self.lblProv.setObjectName("lblProv")
        self.gridFormdir.addWidget(self.lblProv, 0, 3, 1, 1)
        self.editDir = QtWidgets.QLineEdit(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editDir.sizePolicy().hasHeightForWidth())
        self.editDir.setSizePolicy(sizePolicy)
        self.editDir.setStyleSheet("background-color: rgb(255, 255, 229);")
        self.editDir.setObjectName("editDir")
        self.gridFormdir.addWidget(self.editDir, 0, 1, 1, 1)
        self.lblDir = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDir.sizePolicy().hasHeightForWidth())
        self.lblDir.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDir.setFont(font)
        self.lblDir.setObjectName("lblDir")
        self.gridFormdir.addWidget(self.lblDir, 0, 0, 1, 1)
        self.cmbProv = QtWidgets.QComboBox(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbProv.sizePolicy().hasHeightForWidth())
        self.cmbProv.setSizePolicy(sizePolicy)
        self.cmbProv.setSizeIncrement(QtCore.QSize(30, 0))
        self.cmbProv.setObjectName("cmbProv")
        self.gridFormdir.addWidget(self.cmbProv, 0, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridFormdir.addItem(spacerItem5, 0, 2, 1, 1)
        self.gridLayout_8.addLayout(self.gridFormdir, 2, 0, 1, 1)
        self.gridBoton = QtWidgets.QGridLayout()
        self.gridBoton.setObjectName("gridBoton")
        self.line_2 = QtWidgets.QFrame(self.panelCli)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridBoton.addWidget(self.line_2, 4, 0, 1, 1)
        self.griBotonCli = QtWidgets.QGridLayout()
        self.griBotonCli.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.griBotonCli.setContentsMargins(250, 0, 250, 0)
        self.griBotonCli.setObjectName("griBotonCli")
        self.btnAltaCli = QtWidgets.QPushButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAltaCli.sizePolicy().hasHeightForWidth())
        self.btnAltaCli.setSizePolicy(sizePolicy)
        self.btnAltaCli.setObjectName("btnAltaCli")
        self.griBotonCli.addWidget(self.btnAltaCli, 0, 0, 1, 1)
        self.btnModifCli = QtWidgets.QPushButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnModifCli.sizePolicy().hasHeightForWidth())
        self.btnModifCli.setSizePolicy(sizePolicy)
        self.btnModifCli.setObjectName("btnModifCli")
        self.griBotonCli.addWidget(self.btnModifCli, 0, 1, 1, 1)
        self.btnLimpiarCli = QtWidgets.QPushButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLimpiarCli.sizePolicy().hasHeightForWidth())
        self.btnLimpiarCli.setSizePolicy(sizePolicy)
        self.btnLimpiarCli.setObjectName("btnLimpiarCli")
        self.griBotonCli.addWidget(self.btnLimpiarCli, 0, 3, 1, 1)
        self.btnSalir = QtWidgets.QPushButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSalir.sizePolicy().hasHeightForWidth())
        self.btnSalir.setSizePolicy(sizePolicy)
        self.btnSalir.setObjectName("btnSalir")
        self.griBotonCli.addWidget(self.btnSalir, 0, 4, 1, 1)
        self.btnBajaCli = QtWidgets.QPushButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBajaCli.sizePolicy().hasHeightForWidth())
        self.btnBajaCli.setSizePolicy(sizePolicy)
        self.btnBajaCli.setObjectName("btnBajaCli")
        self.griBotonCli.addWidget(self.btnBajaCli, 0, 2, 1, 1)
        self.gridBoton.addLayout(self.griBotonCli, 2, 0, 1, 1)
        self.tableCli = QtWidgets.QTableWidget(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableCli.sizePolicy().hasHeightForWidth())
        self.tableCli.setSizePolicy(sizePolicy)
        self.tableCli.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableCli.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableCli.setAutoScroll(True)
        self.tableCli.setAlternatingRowColors(True)
        self.tableCli.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableCli.setGridStyle(QtCore.Qt.DotLine)
        self.tableCli.setObjectName("tableCli")
        self.tableCli.setColumnCount(3)
        self.tableCli.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCli.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCli.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCli.setHorizontalHeaderItem(2, item)
        self.tableCli.horizontalHeader().setDefaultSectionSize(280)
        self.tableCli.horizontalHeader().setMinimumSectionSize(20)
        self.tableCli.verticalHeader().setStretchLastSection(False)
        self.gridBoton.addWidget(self.tableCli, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridBoton, 4, 0, 1, 1)
        self.gridFormsup = QtWidgets.QGridLayout()
        self.gridFormsup.setObjectName("gridFormsup")
        self.btnCalendar = QtWidgets.QPushButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCalendar.sizePolicy().hasHeightForWidth())
        self.btnCalendar.setSizePolicy(sizePolicy)
        self.btnCalendar.setMaximumSize(QtCore.QSize(32, 32))
        self.btnCalendar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCalendar.setIcon(icon)
        self.btnCalendar.setIconSize(QtCore.QSize(30, 30))
        self.btnCalendar.setObjectName("btnCalendar")
        self.gridFormsup.addWidget(self.btnCalendar, 1, 17, 1, 1)
        self.editDni = QtWidgets.QLineEdit(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editDni.sizePolicy().hasHeightForWidth())
        self.editDni.setSizePolicy(sizePolicy)
        self.editDni.setStyleSheet("background-color: rgb(255, 255, 229);")
        self.editDni.setAlignment(QtCore.Qt.AlignCenter)
        self.editDni.setObjectName("editDni")
        self.gridFormsup.addWidget(self.editDni, 1, 4, 1, 1)
        self.btnReloadCli = QtWidgets.QPushButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReloadCli.sizePolicy().hasHeightForWidth())
        self.btnReloadCli.setSizePolicy(sizePolicy)
        self.btnReloadCli.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReloadCli.setIcon(icon1)
        self.btnReloadCli.setIconSize(QtCore.QSize(24, 24))
        self.btnReloadCli.setObjectName("btnReloadCli")
        self.gridFormsup.addWidget(self.btnReloadCli, 1, 8, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(443, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridFormsup.addItem(spacerItem6, 1, 11, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridFormsup.addItem(spacerItem7, 1, 3, 1, 1)
        self.lblClialta = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblClialta.sizePolicy().hasHeightForWidth())
        self.lblClialta.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblClialta.setFont(font)
        self.lblClialta.setObjectName("lblClialta")
        self.gridFormsup.addWidget(self.lblClialta, 1, 13, 1, 1)
        self.editClialta = QtWidgets.QLineEdit(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editClialta.sizePolicy().hasHeightForWidth())
        self.editClialta.setSizePolicy(sizePolicy)
        self.editClialta.setMinimumSize(QtCore.QSize(0, 0))
        self.editClialta.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.editClialta.setStyleSheet("background-color: rgb(255, 255, 229);")
        self.editClialta.setAlignment(QtCore.Qt.AlignCenter)
        self.editClialta.setObjectName("editClialta")
        self.gridFormsup.addWidget(self.editClialta, 1, 14, 1, 1)
        self.lblCodcli = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCodcli.sizePolicy().hasHeightForWidth())
        self.lblCodcli.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblCodcli.setFont(font)
        self.lblCodcli.setStyleSheet("background-color: rgb(225, 255, 253);")
        self.lblCodcli.setText("")
        self.lblCodcli.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCodcli.setObjectName("lblCodcli")
        self.gridFormsup.addWidget(self.lblCodcli, 1, 1, 1, 1)
        self.lblValidar = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblValidar.sizePolicy().hasHeightForWidth())
        self.lblValidar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblValidar.setFont(font)
        self.lblValidar.setText("")
        self.lblValidar.setObjectName("lblValidar")
        self.gridFormsup.addWidget(self.lblValidar, 1, 6, 1, 1)
        self.lblDNI = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDNI.sizePolicy().hasHeightForWidth())
        self.lblDNI.setSizePolicy(sizePolicy)
        self.lblDNI.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDNI.setFont(font)
        self.lblDNI.setStyleSheet("")
        self.lblDNI.setObjectName("lblDNI")
        self.gridFormsup.addWidget(self.lblDNI, 1, 2, 1, 1)
        self.btnBuscarCli = QtWidgets.QPushButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBuscarCli.sizePolicy().hasHeightForWidth())
        self.btnBuscarCli.setSizePolicy(sizePolicy)
        self.btnBuscarCli.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscarCli.setIcon(icon2)
        self.btnBuscarCli.setIconSize(QtCore.QSize(24, 24))
        self.btnBuscarCli.setObjectName("btnBuscarCli")
        self.gridFormsup.addWidget(self.btnBuscarCli, 1, 7, 1, 1)
        self.gridLayout_8.addLayout(self.gridFormsup, 0, 0, 1, 1)
        self.tabWidget.addTab(self.panelCli, "")
        self.panelFac = QtWidgets.QWidget()
        self.panelFac.setObjectName("panelFac")
        self.label = QtWidgets.QLabel(self.panelFac)
        self.label.setGeometry(QtCore.QRect(380, 340, 351, 101))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.panelFac, "")
        self.panelPro = QtWidgets.QWidget()
        self.panelPro.setObjectName("panelPro")
        self.label_2 = QtWidgets.QLabel(self.panelPro)
        self.label_2.setGeometry(QtCore.QRect(310, 240, 351, 101))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.panelPro, "")
        self.gridLayout_7.addWidget(self.tabWidget, 1, 2, 1, 2)
        self.lblstatus = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblstatus.sizePolicy().hasHeightForWidth())
        self.lblstatus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblstatus.setFont(font)
        self.lblstatus.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblstatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblstatus.setObjectName("lblstatus")
        self.gridLayout_7.addWidget(self.lblstatus, 2, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 140, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_7.addItem(spacerItem8, 2, 3, 1, 1)
        venPrincipal.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(venPrincipal)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1150, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuArchivo = QtWidgets.QMenu(self.menuBar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuInformes = QtWidgets.QMenu(self.menuBar)
        self.menuInformes.setObjectName("menuInformes")
        self.menuAcerca_de = QtWidgets.QMenu(self.menuBar)
        self.menuAcerca_de.setObjectName("menuAcerca_de")
        venPrincipal.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(venPrincipal)
        self.statusbar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.statusbar.setFont(font)
        self.statusbar.setStyleSheet("background-color: rgb(235, 254, 255);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"text-align:center;")
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        venPrincipal.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(venPrincipal)
        self.toolBar.setObjectName("toolBar")
        venPrincipal.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubarSalir = QtWidgets.QAction(venPrincipal)
        self.menubarSalir.setObjectName("menubarSalir")
        self.toolbarSalir = QtWidgets.QAction(venPrincipal)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/iconsalir.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.toolbarSalir.setIcon(icon3)
        self.toolbarSalir.setObjectName("toolbarSalir")
        self.toolbarBackup = QtWidgets.QAction(venPrincipal)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/backup32.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/backup32.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.toolbarBackup.setIcon(icon4)
        self.toolbarBackup.setObjectName("toolbarBackup")
        self.toolbarAbrirDir = QtWidgets.QAction(venPrincipal)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/abrircarpeta.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.toolbarAbrirDir.setIcon(icon5)
        self.toolbarAbrirDir.setObjectName("toolbarAbrirDir")
        self.actionAbrir = QtWidgets.QAction(venPrincipal)
        self.actionAbrir.setObjectName("actionAbrir")
        self.toolbarPrinter = QtWidgets.QAction(venPrincipal)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/printer.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.toolbarPrinter.setIcon(icon6)
        self.toolbarPrinter.setObjectName("toolbarPrinter")
        self.actionImprimer = QtWidgets.QAction(venPrincipal)
        self.actionImprimer.setIcon(icon6)
        self.actionImprimer.setObjectName("actionImprimer")
        self.menubarReportCli = QtWidgets.QAction(venPrincipal)
        self.menubarReportCli.setObjectName("menubarReportCli")
        self.actionImprimir_Factura = QtWidgets.QAction(venPrincipal)
        self.actionImprimir_Factura.setObjectName("actionImprimir_Factura")
        self.actionListado_Productos = QtWidgets.QAction(venPrincipal)
        self.actionListado_Productos.setObjectName("actionListado_Productos")
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionImprimer)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.menubarSalir)
        self.menuInformes.addAction(self.menubarReportCli)
        self.menuInformes.addAction(self.actionImprimir_Factura)
        self.menuInformes.addAction(self.actionListado_Productos)
        self.menuBar.addAction(self.menuArchivo.menuAction())
        self.menuBar.addAction(self.menuInformes.menuAction())
        self.menuBar.addAction(self.menuAcerca_de.menuAction())
        self.toolBar.addAction(self.toolbarAbrirDir)
        self.toolBar.addAction(self.toolbarPrinter)
        self.toolBar.addAction(self.toolbarBackup)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toolbarSalir)

        self.retranslateUi(venPrincipal)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(venPrincipal)

    def retranslateUi(self, venPrincipal):
        _translate = QtCore.QCoreApplication.translate
        venPrincipal.setWindowTitle(_translate("venPrincipal", "Proyecto Uno"))
        self.lblstatusdate.setText(_translate("venPrincipal", "TextLabel"))
        self.chkTar.setText(_translate("venPrincipal", "Tarjeta"))
        self.rbtFem.setText(_translate("venPrincipal", "Femenino"))
        self.lblSexo.setText(_translate("venPrincipal", "Sexo:  "))
        self.rbtMasc.setText(_translate("venPrincipal", "Masculino"))
        self.lblPago.setText(_translate("venPrincipal", "Métodos de Pago:  "))
        self.chkEfec.setText(_translate("venPrincipal", "Efectivo"))
        self.chkTrans.setText(_translate("venPrincipal", "Transferencia"))
        self.lblEdad.setText(_translate("venPrincipal", "Edad:"))
        self.lblNome.setText(_translate("venPrincipal", "Nombre: "))
        self.lblApel.setText(_translate("venPrincipal", "Apellidos: "))
        self.lblProv.setText(_translate("venPrincipal", "Provincia:"))
        self.lblDir.setText(_translate("venPrincipal", "Dirección: "))
        self.btnAltaCli.setText(_translate("venPrincipal", "Grabar"))
        self.btnModifCli.setText(_translate("venPrincipal", "Modificar"))
        self.btnLimpiarCli.setText(_translate("venPrincipal", "Limpiar"))
        self.btnSalir.setText(_translate("venPrincipal", "Salir"))
        self.btnBajaCli.setText(_translate("venPrincipal", "Eliminar"))
        item = self.tableCli.horizontalHeaderItem(0)
        item.setText(_translate("venPrincipal", "DNI"))
        item = self.tableCli.horizontalHeaderItem(1)
        item.setText(_translate("venPrincipal", "APELLIDOS"))
        item = self.tableCli.horizontalHeaderItem(2)
        item.setText(_translate("venPrincipal", "NOMBRE"))
        self.lblClialta.setText(_translate("venPrincipal", "Fecha de Alta:"))
        self.lblDNI.setText(_translate("venPrincipal", "DNI: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.panelCli), _translate("venPrincipal", "Clientes"))
        self.label.setText(_translate("venPrincipal", "PANEL DE FACTURACIÓN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.panelFac), _translate("venPrincipal", "Facturación"))
        self.label_2.setText(_translate("venPrincipal", "PANEL DE Productos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.panelPro), _translate("venPrincipal", "Productos"))
        self.lblstatus.setText(_translate("venPrincipal", "TextLabel"))
        self.menuArchivo.setTitle(_translate("venPrincipal", "Archivo"))
        self.menuInformes.setTitle(_translate("venPrincipal", "Informes"))
        self.menuAcerca_de.setTitle(_translate("venPrincipal", "Acerca de"))
        self.toolBar.setWindowTitle(_translate("venPrincipal", "toolBar"))
        self.menubarSalir.setText(_translate("venPrincipal", "Salir"))
        self.menubarSalir.setShortcut(_translate("venPrincipal", "Alt+S"))
        self.toolbarSalir.setText(_translate("venPrincipal", "Salir"))
        self.toolbarSalir.setToolTip(_translate("venPrincipal", "<html><head/><body><p><img src=\":/newPrefix/iconsalir.png\"/></p></body></html>"))
        self.toolbarSalir.setShortcut(_translate("venPrincipal", "Alt+S"))
        self.toolbarBackup.setText(_translate("venPrincipal", "Backup"))
        self.toolbarBackup.setToolTip(_translate("venPrincipal", "<html><head/><body><p><img src=\":/newPrefix/backup32.png\"/></p></body></html>"))
        self.toolbarBackup.setShortcut(_translate("venPrincipal", "Alt+B"))
        self.toolbarAbrirDir.setText(_translate("venPrincipal", "abrirDirectorio"))
        self.toolbarAbrirDir.setToolTip(_translate("venPrincipal", "<html><head/><body><p><img src=\":/newPrefix/abrircarpeta.png\"/></p></body></html>"))
        self.actionAbrir.setText(_translate("venPrincipal", "Abrir..."))
        self.toolbarPrinter.setText(_translate("venPrincipal", "printer"))
        self.toolbarPrinter.setToolTip(_translate("venPrincipal", "<html><head/><body><p><img src=\":/newPrefix/printer.png\"/></p></body></html>"))
        self.toolbarPrinter.setShortcut(_translate("venPrincipal", "Alt+P"))
        self.actionImprimer.setText(_translate("venPrincipal", "Imprimir"))
        self.menubarReportCli.setText(_translate("venPrincipal", "Listado Clientes"))
        self.actionImprimir_Factura.setText(_translate("venPrincipal", "Imprimir Factura"))
        self.actionListado_Productos.setText(_translate("venPrincipal", "Listado Productos"))
import abrirdirectorio_rc
import logo_rc
import toolbarbackup_rc
import toolbarprinter_rc
import toolbarsalir_rc
