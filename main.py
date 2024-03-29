from PyQt5 import QtWidgets, QtGui, QtCore, QtPrintSupport
from ventana import *
from vensalir import *
from venavisos import *
from vencalendar import *
from datetime import datetime, date
import sys, var, events, clients, conexion, printer
import locale
# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es-ES')

class DialogAvisos(QtWidgets.QDialog):
    def __init__(self):
        super(DialogAvisos, self).__init__()
        var.dlgaviso = Ui_dlgAvisos()
        var.dlgaviso.setupUi(self)
        var.dlgaviso.btnAceptaviso.clicked.connect(events.Eventos.Confirmar)
        var.dlgaviso.btnCancelaviso.clicked.connect(events.Eventos.Anular)

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgsalir = Ui_dlgSalir()
        var.dlgsalir.setupUi(self)
        var.dlgsalir.btnAceptar.clicked.connect(events.Eventos.Salir)
        var.dlgsalir.btnCancelar.clicked.connect(events.Eventos.closeSalir)
        #var.dlgsalir.btnBoxSalir(var.dlgsalir.btnAceptar).clicked.connect(events.Eventos.Salir)

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_dlgCalendar()
        var.dlgcalendar.setupUi(self)
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate((QtCore.QDate(anoactual, mesactual, diaactual)))
        var.dlgcalendar.Calendar.clicked.connect(clients.Clientes.cargarFecha)

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()
        self.setWindowTitle('Abrir Archivo')
        self.setModal(True)

class PrintDialogAbrir(QtPrintSupport.QPrintDialog):
    def __init__(self):
        super(PrintDialogAbrir, self).__init__()

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)
        var.dlgsalir = DialogSalir()
        var.dlgcalendar = DialogCalendar()
        var.filedlgabrir = FileDialogAbrir()
        var.dlgImprimir = PrintDialogAbrir()
        var.dlgaviso = DialogAvisos()

        '''
        colección de datos
        '''
        var.rbtsex = (var.ui.rbtFem, var.ui.rbtMasc)
        var.chkpago = (var.ui.chkEfec, var.ui.chkTar, var.ui.chkTrans)
        '''
        conexion de eventos con los objetos
        estamos conectando el código con la interfaz gráfico
        botones formulario cliente
        '''
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.menubarSalir.triggered.connect(events.Eventos.Salir)
        var.ui.toolbarSalir.triggered.connect(events.Eventos.Salir)
        var.ui.toolbarBackup.triggered.connect(events.Eventos.Backup)
        var.ui.toolbarAbrirDir.triggered.connect(events.Eventos.AbrirDir)
        var.ui.toolbarPrinter.triggered.connect(events.Eventos.AbrirPrinter)
        var.ui.editDni.editingFinished.connect(clients.Clientes.validoDni)
        #var.ui.editDni.editingFinished.connect(lambda: clients.Clientes.validoDni)
        var.ui.btnCalendar.clicked.connect(clients.Clientes.abrirCalendar)
        var.ui.btnAltaCli.clicked.connect(clients.Clientes.altaCliente)
        var.ui.btnLimpiarCli.clicked.connect(clients.Clientes.limpiarCli)
        var.ui.btnBajaCli.clicked.connect(events.Eventos.mostrarAviso)
        var.ui.btnModifCli.clicked.connect(clients.Clientes.modifCliente)
        var.ui.btnReloadCli.clicked.connect(clients.Clientes.reloadCli)
        var.ui.btnBuscarCli.clicked.connect(clients.Clientes.buscarCli)
        clients.Clientes.valoresSpin()

        for i in var.rbtsex:
            i.toggled.connect(clients.Clientes.selSexo)
        for i in var.chkpago:
            i.stateChanged.connect(clients.Clientes.selPago)

        var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)
        var.ui.tableCli.clicked.connect(clients.Clientes.cargarCli)
        var.ui.tableCli.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        events.Eventos.cargarProv(self)
        var.ui.statusbar.addPermanentWidget(var.ui.lblstatus, 1)
        var.ui.statusbar.addPermanentWidget(var.ui.lblstatusdate, 2)
        var.ui.lblstatus.setStyleSheet('QLabel {color: red; font: bold;}')
        var.ui.lblstatus.setText('Bienvenido a 2º DAM')
        fecha = date.today()
        var.ui.lblstatusdate.setStyleSheet('QLabel {color: black; font: bold;}')
        var.ui.lblstatusdate.setText(fecha.strftime('%A %d de %B del %Y'))

        '''
        módulos de impresión
        '''
        var.ui.menubarReportCli.triggered.connect(printer.Printer.reportCli)
        '''
        módulos conexion base datos
        '''

        conexion.Conexion.db_connect(var.filebd)
        # conexion.Conexion()
        conexion.Conexion.mostrarClientes(self)

    def closeEvent(self, event):
        if event:
            events.Eventos.Salir(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())
