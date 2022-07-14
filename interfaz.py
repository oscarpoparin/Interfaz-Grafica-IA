from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
import subprocess as sub
import pyttsx3
import pywhatkit
from sqlalchemy import false
import wikipedia
import datetime
import keyboard
import os
import threading as tr
import whatsapp as whapp
import browser
import database
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer
from chatterbot import preprocessors
import source 


#Inicio codigo 

name = "oparin"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')  # coloca una voz
engine.setProperty('voices', voices[0].id) # colocar voz que este en esa posicion
engine.setProperty('rate', 145) # velocidad de la voz

#Funcion que cargara datos almacenados dentro de mis diccionarios

def charge_data(name_dict, name_file):
    try:
        with open(name_file) as f:
            for line in f:
                (key, val) = line.split(",")
                val = val.rstrip("\n")
                name_dict[key] = val
    except FileNotFoundError as e:
        pass

#Directorios

sites = dict()
charge_data(sites, "pages.txt")

files = dict()
charge_data(files, "archivos.txt")

programs = dict()
charge_data(programs, "apps.txt")

agenda = dict()
charge_data(agenda, "contactos.txt")

#Funcion para convertir audio a texto

def talk(text):
    engine.say(text)  # convierte el texto en voz
    engine.runAndWait()

#Funcion para escribir lo encontrado en internet en textarea

def read_and_talk():
    print("funcion leer y hablar")

#Funcion para escribir lo encontrado en internet en textarea

def write_text(text_wiki):
    text_info.insert(INSERT, text_wiki)

#funcion para voz de IA

def listen(phrase=None):
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        talk(phrase)
        pc = listener.listen(source)
        try:
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
        except sr.UnknownValueError:
            print("No te entendí, intenta d nuevo")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognitin service; {0}".format(e))
        return rec

#funciones que hay en los diccionarios como palabras claves

def reproduce(rec):
    music = rec.replace('reproduce', '')
    print("Reproduciendo " + music)
    talk("Reproduciendo " + music)
    pywhatkit.playonyt(music)

def busca(rec):
    search = rec.replace('busca', '')
    wikipedia.set_lang('es')
    wiki = wikipedia.summary(search, 1)
    talk(wiki)
    write_text(search + ": " + wiki)

def alarma(rec):
    num = rec.replace('alarma', '')
    num = num.strip()
    talk("Alarma activada a las " + num + " horas")
    if num[0] != '0' and len(num) < 5:
        num = '0' + num
        print(num)
    while True:
        if datetime.datetime.now().strftime('%H:%M') == num:
            print("DESPIERTA!!!")
            mixer.init()
            mixer.music.load("auronplay-alarma.mp3")
            mixer.music.play()
            if keyboard.read_key() == 's':
                mixer.music.stop()
            break

def abre(rec):
    task = rec.replace('abre','').strip()
            
    if task in sites:
        for task in sites:
            if task in rec:
                sub.call(f'start chrome.exe {sites[task]}', shell=True)
                talk(f'Abriendo {task}')
    elif task in programs:
        for task in programs:
            if task in rec:
                talk(f'Abriendo {task}')
                os.startfile(programs[task])
    else:
        talk("No se ha encontrado la app o pagina web, \
            usa los botones de agregar...")

def archivo(rec):
    file = rec.replace('archivo','').strip()
    if file in files:
        for file in files:
            if file in rec:
                sub.Popen([files[file]], shell=True)
                talk(f'Abriendo {file}')
            else:
                talk("No se ha encontrado el archivo, \
                    usa los botones de agregar...")

def escribir(rec):
    try:
        with open("notas.txt", 'a') as f:
            write(f)

    except FileNotFoundError as e:
        file = open("notas.txt", 'w')
        write(file)

def enviar_mensaje(rec):
    talk("¿A quien quieres enviar el mensaje?")
    contact = listen("Te escucho")
    contact = contact.strip()

    if contact in agenda:
        for con in agenda:
            if con == contact:
                contact = agenda[con]
                talk("¿Qué mensaje deseas enviar?")
                message = listen("Te escucho")
                talk("Enviando mensaje...")
                whapp.send_menssage(contact, message)
    else:
        talk("No existe un contacto con ese nombre")

def cierra(rec):
    for task in programs:
        kill_task = programs[task].split('\\')
        kill_task = kill_task[-1]
        if task in rec:
            sub.call(f'TASKKILL /IM {kill_task} /F', shell=True)
            talk(f'Cerrando {task}')
        if 'todo' in rec:
            sub.call(f'TASKKILL /IM {kill_task} /F', shell=True)
            talk(f'Cerrando {task}')
    if 'termina' in rec:
        talk(f'Adiós')
        sub.call(f'TASKKILL /IM python.exe /F', shell=True)

def buscame(rec):
    something = rec.replace('buscame', '').strip()
    talk("Buscando " + something)
    browser.search(something)

#Palabras clave
key_words = {
    'reproduce' : reproduce,
    'busca' : busca,
    'alarma' : alarma, #cambiar para que diga la hora
    'abre' : abre,
    'archivo' : archivo,
    'escribe' : escribir,
    'mensaje' : enviar_mensaje,
    'cierra' : cierra,
    'termina' : cierra,
    'buscame' : buscame,
}



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
        #Cuadro de texto
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

#funcion principal

def run_oparin():
    chat = ChatBot('oparin', database_uri=None)
    trainer = ListTrainer(chat)
    trainer.train(database.get_questions_answers()) 
    talk("Te escucho...")
    print("te escucho")
    while True:
        try:
            rec = listen("")
            #rec = listen("Te escucho")
        except UnboundLocalError:
            talk("No te entendí, intenta de nuevo")
            continue
        if 'busca' in rec:
            key_words['busca'](rec)
            break
        elif rec.split()[0] in key_words:
            #for word in key_words:
            #    if word in rec:
            key_words[rec.split()[0] ](rec)
        else:
            print("Tu: " , rec)
            answer = chat.get_response(rec)
            print("bot ",answer)
            if 'adios' in rec:
                break
    Ui_Main.update()

#funcion para escrirbir dentro de un documento

def write(f):
    talk("¿Qué quieres que escriba?")
    rec_write = listen("Te escucho")
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo, puedes revisarlo")
    sub.Popen("notas.txt", shell=True)

#creacion de ventana con modulo tkinter

windows = Tk()
# Hide it with .withdraw
windows.withdraw()
# To reveal it again:
windows.deiconify()

#Funciones para abrir, escribir y guardar datos

def open_w_files():
    global namefile_entry, pathf_entry
    windows_files = Toplevel() # segunda ventana
    windows_files.title("Agregar Archivos")
    windows_files.geometry("300x200")
    windows_files.resizable(0,0)
    windows_files.configure(bg='#434343')
    windows.eval(f'tk::PlaceWindow {str(windows_files)} center') # centrar segunda ventana

    title_label = Label(
                            windows_files,
                            text="Agregar Archivos",
                            fg="#fff",
                            bg="#434343",
                            font=('Arial', 10, 'bold')
                        )
    title_label.pack(pady=3)
    name_label = Label(
                            windows_files,
                            text="Nombre del Archivo",
                            fg="#fff",
                            bg="#434343",
                            font=('Arial', 10, 'bold')
                        )
    name_label.pack(pady=2)

    namefile_entry = Entry(windows_files)
    namefile_entry.pack(pady=1)

    path_label = Label(
                            windows_files,
                            text="Ruta del Archivo",
                            fg="#fff",
                            bg="#434343",
                            font=('Arial', 10, 'bold')
                        )
    path_label.pack(pady=2)

    pathf_entry = Entry(windows_files, width=35)
    pathf_entry.pack(pady=1)

    save_button = Button(
                            windows_files,
                            text="Guardar",
                            bg="#16222a",
                            fg="#fff",
                            width=8,
                            height=1,
                            command=add_files
                        )
    save_button.pack(pady=5)


def open_w_apps():
    global nameapps_entry, pathapps_entry
    windows_apps = Toplevel() # tercer ventana
    windows_apps.title("Agregar una app")
    windows_apps.geometry("300x200")
    windows_apps.resizable(0,0)
    windows_apps.configure(bg='#434343')
    #Ui_Main.eval(f'tk::PlaceWindow {str(windows_apps)} center') # centrar segunda ventana

    title_label = Label(
                            windows_apps,
                            text="Agregar una app",
                            fg="#fff",
                            bg="#434343",
                            font=('Arial', 10, 'bold')
                        )
    title_label.pack(pady=3)
    name_label = Label(
                            windows_apps,
                            text="Nombre de la app",
                            fg="#fff",
                            bg="#434343",
                            font=('Arial', 10, 'bold')
                        )
    name_label.pack(pady=2)

    nameapps_entry = Entry(windows_apps)
    nameapps_entry.pack(pady=1)

    path_label = Label(
                            windows_apps,
                            text="Ruta de la app",
                            fg="#fff",
                            bg="#434343",
                            font=('Arial', 10, 'bold')
                        )
    path_label.pack(pady=2)

    pathapps_entry = Entry(windows_apps, width=35)
    pathapps_entry.pack(pady=1)

    save_button = Button(
                            windows_apps,
                            text="Guardar",
                            bg="#16222a",
                            fg="#fff",
                            width=8,
                            height=1,
                            command=add_apps
                        )
    save_button.pack(pady=5)

def open_w_pages():
    global namep_entry, pathp_entry
    windows_pages = Toplevel() # cuarta ventana
    windows_pages.title("Agregar una pagina web")
    windows_pages.geometry("300x200")
    windows_pages.resizable(0,0)
    windows_pages.configure(bg='#434343')
    #Ui_Main.eval(f'tk::PlaceWindow {str(windows_pages)} center') # centrar segunda ventana

    title_label = Label(
                            windows_pages,
                            text="Agregar una pagina",
                            fg="#fff",
                            bg="#434343",
                            font=('Arial', 10, 'bold')
                        )
    title_label.pack(pady=3)
    name_label = Label(
                            windows_pages,
                            text="Nombre de la pagina",
                            fg="#fff",
                            bg="#434343",
                            font=('Arial', 10, 'bold')
                        )
    name_label.pack(pady=2)

    namep_entry = Entry(windows_pages)
    namep_entry.pack(pady=1)

    path_label = Label(
                            windows_pages,
                            text="URL de la pagina",
                            fg="#fff",
                            bg="#434343",
                            font=('Arial', 10, 'bold')
                        )
    path_label.pack(pady=2)

    pathp_entry = Entry(windows_pages, width=35)
    pathp_entry.pack(pady=1)

    save_button = Button(
                            windows_pages,
                            text="Guardar",
                            bg="#16222a",
                            fg="#fff",
                            width=8,
                            height=1,
                            command=add_pages
                        )
    save_button.pack(pady=5)

def open_w_contacts():
    global namec_entry, pathc_entry
    windows_contacts = Toplevel() # cuarta ventana
    windows_contacts.title("Agregar contacto")
    windows_contacts.geometry("300x200")
    windows_contacts.resizable(0,0)
    windows_contacts.configure(bg='#434343')
    #Ui_Main.eval(f'tk::PlaceWindow {str(windows_contacts)} center') # centrar segunda ventana

    title_label = Label(
                            windows_contacts,
                            text="Agregar contacto",
                            fg="#fff",
                            bg="#434343",
                            font=('Arial', 10, 'bold')
                        )
    title_label.pack(pady=3)
    name_label = Label(
                            windows_contacts,
                            text="Nombre del contacto",
                            fg="#fff",
                            bg="#434343",
                            font=('Arial', 10, 'bold')
                        )
    name_label.pack(pady=2)

    namec_entry = Entry(windows_contacts)
    namec_entry.pack(pady=1)

    path_label = Label(
                            windows_contacts,
                            text="Numero (codigo pais)",
                            fg="#fff",
                            bg="#434343",
                            font=('Arial', 10, 'bold')
                        )
    path_label.pack(pady=2)

    pathc_entry = Entry(windows_contacts, width=35)
    pathc_entry.pack(pady=1)

    save_button = Button(
                            windows_contacts,
                            text="Guardar",
                            bg="#16222a",
                            fg="#fff",
                            width=8,
                            height=1,
                            command=add_contact
                        )
    save_button.pack(pady=5)

#funcion para agregar archivos,paginas y apps

def add_files():
    name_file = namefile_entry.get().strip()
    path_file = pathf_entry.get().strip()
    files[name_file] = path_file
    save_data(name_file, path_file, "archivos.txt")
    namefile_entry.delete(0, "end")
    pathf_entry.delete(0,"end")


def add_apps():
    name_app = nameapps_entry.get().strip()
    path_app = pathapps_entry.get().strip()
    programs[name_app] = path_app
    save_data(name_app, path_app, "apps.txt")
    nameapps_entry.delete(0, "end")
    pathapps_entry.delete(0,"end")

def add_pages():
    name_pages = namep_entry.get().strip()
    url_pages = pathp_entry.get().strip()
    sites[name_pages] = url_pages
    save_data(name_pages, url_pages, "pages.txt")
    namep_entry.delete(0, "end")
    pathp_entry.delete(0,"end")

def add_contact():
    name_contacto = namec_entry.get().strip()
    path_contacto = pathc_entry.get().strip()
    agenda[name_contacto] = path_contacto
    save_data(name_contacto, path_contacto, "contactos.txt")
    namec_entry.delete(0, "end")
    pathc_entry.delete(0,"end")

#funcion para guardar datos

def save_data(key, value, file_name):
    try:
        with open(file_name, 'a') as f:
            f.write(key + "," + value + "\n")
    except FileNotFoundError:
        file = open(file_name, 'a')
        file.write(key + "," + value + "\n")

#funcion para mostrar los datos almacenados

def talk_pages():
    if bool(sites) == True:
        talk("Has agregado las siguientes paginas web")
        for site in sites:
            talk(site)
    else:
        talk("Aun no has agregado páginas web!")

def talk_apps():
    if bool(programs) == True:
        talk("Has agregado las siguientes apps")
        for app in programs:
            talk(app)
    else:
        talk("Aun no has agregado apps!")

def talk_files():
    if bool(files) == True:
        talk("Has agregado las siguientes archivos")
        for file in files:
            talk(file)
    else:
        talk("Aun no has agregado archivos!")

def talk_contact():
    if bool(agenda) == True:
        talk("Has agregado los siguientes contactos")
        for conta in agenda:
            talk(conta)
    else:
        talk("Aun no hay contactos registrados!")

#funcion para preguntar nombre
def give_me_name():
    talk("Hola, ¿Cómo te llamas?")
    name = listen("Te escucho...")
    name = name.strip()
    talk(f"Bienvenido {name}")
    try:
        with open("name.txt", 'w') as f:
            f.write(name)
    except FileNotFoundError:
        file = open("name.txt", 'w')
        file.write(name)

#funcion para decir nombre

def say_hello():
    if os.path.exists("name.txt"):
        with open("name.txt") as f:
            for name in f:
                talk(f"Hola, bienvenido {name}")
    else:
        give_me_name()


def thread_hello():
    t = tr.Thread(target=say_hello)
    t.start()

#thread_hello()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

thread_hello()
windows.mainloop()
