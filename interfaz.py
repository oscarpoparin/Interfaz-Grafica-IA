from PyQt5 import QtCore, QtGui, QtWidgets

def open_w_apps():
    print("Agregar app")

def open_w_pages():
    print("agregar paginas")

def open_w_contacts():
    print("agregar contactos")

def talk_pages():
    print("paginas agregadas")

def talk_apps():
    print("app agregadas")

def talk_files():
    print("archivos agregados")

def talk_contact():
    print("contactos agregados")

def read_and_talk():
    print("funcion hablar")

def run_oparin():
    print("funcion principal")

def open_w_files():
    print("Agregart archivos")

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.setEnabled(True)
        Main.resize(900, 576)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        Main.setMaximumSize(QtCore.QSize(900, 576))
        Main.setStyleSheet("*{\n"
            "font-family:Consolas;\n"
            "}\n"
            "\n"
            "QFrame{\n"
            "background:#4d4d4d;\n"
            "}\n"
            "\n"
            "QLabel#title{\n"
            "font-size:40px;\n"
            "color:#fff;\n"
            "}\n"
            "\n"
            "QLineEdit{\n"
            "border-radius:15px;\n"
            "}\n"
            "\n"
            "QPushButton#escuchar{\n"
            "font-size:30px;\n"
            "background:rgb(20, 41, 163);\n"
            "color:#fff;\n"
            "border-radius:none;\n"
            "border:none;\n"
            "padding:15px;\n"
            "}\n"
            "\n"
            "QPushButton#escuchar:hover{\n"
            "color:rgba(20, 41, 163, 0.733);\n"
            "border-radius:15px;\n"
            "color:#fff;\n"
            "}\n"
            "\n"
            "QPushButton{\n"
            "border-radius:none;\n"
            "border:2px solid #000;\n"
            "font-size:18px;\n"
            "color:#fff;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background:rgb(15, 173, 212);\n"
            "border-radius:15px;\n"
            "color:#fff;\n"
            "border:none;\n"
            "}\n"
            "\n"
            "QPlainTextEdit{\n"
            "border:2px solid #000;\n"
            "border-radius:15px;\n"
            "color:#fff;\n"
            "font-size:20px;\n"
            "}")
        self.centralwidget = QtWidgets.QWidget(Main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(900, 576))
        self.centralwidget.setMaximumSize(QtCore.QSize(900, 576))
        self.centralwidget.setSizeIncrement(QtCore.QSize(700, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 900, 576))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(900, 576))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setGeometry(QtCore.QRect(10, -1, 891, 81))
        self.title.setStyleSheet("")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.escuchar = QtWidgets.QPushButton(self.frame)
        self.escuchar.setGeometry(QtCore.QRect(350, 490, 210, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.escuchar.sizePolicy().hasHeightForWidth())
        self.escuchar.setSizePolicy(sizePolicy)
        self.escuchar.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/escucha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.escuchar.setIcon(icon)
        self.escuchar.setIconSize(QtCore.QSize(32, 32))
        #Eventos botones
        self.escuchar.setChecked(True)
        self.escuchar.clicked.connect(run_oparin)
        self.escuchar.setAutoDefault(False)
        self.escuchar.setDefault(False)
        self.escuchar.setObjectName("escuchar")
        self.escuchar_2 = QtWidgets.QPushButton(self.frame)
        self.escuchar_2.setGeometry(QtCore.QRect(650, 80, 231, 41))
        self.escuchar_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.escuchar_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.escuchar_2.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/barras-de-sonido.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.escuchar_2.setIcon(icon1)
        self.escuchar_2.setIconSize(QtCore.QSize(30, 30))
        #Eventos botones
        self.escuchar_2.setChecked(True)
        self.escuchar_2.clicked.connect(read_and_talk)
        self.escuchar_2.setShortcut("")
        self.escuchar_2.setCheckable(False)
        self.escuchar_2.setChecked(False)
        self.escuchar_2.setAutoRepeat(False)
        self.escuchar_2.setAutoExclusive(False)
        self.escuchar_2.setAutoRepeatInterval(100)
        self.escuchar_2.setAutoDefault(False)
        self.escuchar_2.setDefault(True)
        self.escuchar_2.setFlat(True)
        self.escuchar_2.setObjectName("escuchar_2")
        self.escuchar_3 = QtWidgets.QPushButton(self.frame)
        self.escuchar_3.setGeometry(QtCore.QRect(650, 130, 231, 41))
        self.escuchar_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/agregar-archivo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.escuchar_3.setIcon(icon2)
        self.escuchar_3.setIconSize(QtCore.QSize(30, 30))
        #Eventos botones
        self.escuchar_3.setChecked(True)
        self.escuchar_3.clicked.connect(open_w_files)
        self.escuchar_3.setDefault(True)
        self.escuchar_3.setFlat(True)
        self.escuchar_3.setObjectName("escuchar_3")
        self.escuchar_4 = QtWidgets.QPushButton(self.frame)
        self.escuchar_4.setGeometry(QtCore.QRect(650, 180, 231, 41))
        self.escuchar_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.escuchar_4.setIcon(icon2)
        self.escuchar_4.setIconSize(QtCore.QSize(30, 30))
        #Eventos botones
        self.escuchar_4.setChecked(True)
        self.escuchar_4.clicked.connect(open_w_apps)
        self.escuchar_4.setDefault(True)
        self.escuchar_4.setFlat(True)
        self.escuchar_4.setObjectName("escuchar_4")
        self.escuchar_5 = QtWidgets.QPushButton(self.frame)
        self.escuchar_5.setGeometry(QtCore.QRect(650, 230, 231, 41))
        self.escuchar_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.escuchar_5.setIcon(icon2)
        self.escuchar_5.setIconSize(QtCore.QSize(30, 30))
        #Eventos botones
        self.escuchar_5.setChecked(True)
        self.escuchar_5.clicked.connect(open_w_pages)
        self.escuchar_5.setDefault(True)
        self.escuchar_5.setFlat(True)
        self.escuchar_5.setObjectName("escuchar_5")
        self.escuchar_6 = QtWidgets.QPushButton(self.frame)
        self.escuchar_6.setGeometry(QtCore.QRect(650, 280, 231, 41))
        self.escuchar_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/img/agregar-usuario.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.escuchar_6.setIcon(icon3)
        self.escuchar_6.setIconSize(QtCore.QSize(30, 30))
        #Eventos botones
        self.escuchar_6.setChecked(True)
        self.escuchar_6.clicked.connect(open_w_contacts)
        self.escuchar_6.setDefault(True)
        self.escuchar_6.setFlat(True)
        self.escuchar_6.setObjectName("escuchar_6")
        self.escuchar_7 = QtWidgets.QPushButton(self.frame)
        self.escuchar_7.setGeometry(QtCore.QRect(650, 330, 231, 41))
        self.escuchar_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/img/clip-de-papel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.escuchar_7.setIcon(icon4)
        self.escuchar_7.setIconSize(QtCore.QSize(30, 30))
        #Eventos botones
        self.escuchar_7.setChecked(True)
        self.escuchar_7.clicked.connect(talk_pages)
        self.escuchar_7.setDefault(True)
        self.escuchar_7.setFlat(True)
        self.escuchar_7.setObjectName("escuchar_7")
        self.escuchar_8 = QtWidgets.QPushButton(self.frame)
        self.escuchar_8.setGeometry(QtCore.QRect(650, 380, 231, 41))
        self.escuchar_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.escuchar_8.setIcon(icon4)
        self.escuchar_8.setIconSize(QtCore.QSize(30, 30))
        #Eventos botones
        self.escuchar_8.setChecked(True)
        self.escuchar_8.clicked.connect(talk_apps)
        self.escuchar_8.setAutoDefault(False)
        self.escuchar_8.setDefault(True)
        self.escuchar_8.setFlat(True)
        self.escuchar_8.setObjectName("escuchar_8")
        self.escuchar_9 = QtWidgets.QPushButton(self.frame)
        self.escuchar_9.setGeometry(QtCore.QRect(650, 430, 231, 41))
        self.escuchar_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.escuchar_9.setIcon(icon4)
        self.escuchar_9.setIconSize(QtCore.QSize(30, 30))
        #Eventos botones
        self.escuchar_9.setChecked(True)
        self.escuchar_9.clicked.connect(talk_files)
        self.escuchar_9.setDefault(True)
        self.escuchar_9.setFlat(True)
        self.escuchar_9.setObjectName("escuchar_9")
        self.escuchar_10 = QtWidgets.QPushButton(self.frame)
        self.escuchar_10.setGeometry(QtCore.QRect(650, 480, 231, 41))
        self.escuchar_10.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.escuchar_10.setIcon(icon4)
        self.escuchar_10.setIconSize(QtCore.QSize(30, 30))
        #Eventos botones
        self.escuchar_10.setChecked(True)
        self.escuchar_10.clicked.connect(talk_contact)
        self.escuchar_10.setDefault(True)
        self.escuchar_10.setFlat(True)
        self.escuchar_10.setObjectName("escuchar_10")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 90, 241, 401))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(320, 110, 281, 341))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/img/machine-learning.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Main"))
        self.title.setText(_translate("Main", "Inteligencia Artificial"))
        self.escuchar.setText(_translate("Main", "Escuchar"))
        self.escuchar_2.setText(_translate("Main", "Hablar"))
        self.escuchar_3.setText(_translate("Main", "Agregar Archivos"))
        self.escuchar_4.setText(_translate("Main", "Agregar Apps"))
        self.escuchar_5.setText(_translate("Main", "Agregar Paginas"))
        self.escuchar_6.setText(_translate("Main", "Agregar Contacto"))
        self.escuchar_7.setText(_translate("Main", "Paginas Agregadas"))
        self.escuchar_8.setText(_translate("Main", "Apps Agregadas"))
        self.escuchar_9.setText(_translate("Main", "Archivos Agregados"))
        self.escuchar_10.setText(_translate("Main", "Contactos Agregados"))

import source 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
