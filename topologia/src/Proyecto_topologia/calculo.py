from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QListWidget, QFileDialog
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QIcon, QFont, QPixmap
from dibujo import Dialogo
import os


class CalApp(QWidget):
	def __init__(self, campos=None):
		super().__init__()

		self.campos = campos
		self.setFixedSize(950,700)	#El tamaño por defecto de la pantalla sin permitir ajustes
		self.setWindowTitle("Cálculo")	#Establece el título de la ventana
		self.setStyleSheet("background-color: rgb(85, 255, 127)")
		self.setWindowIcon(QIcon("iconos/main_window.png"))
		self.altura_vuelo = int(self.campos[4]) #Accedemos al valor de la altura de vuelo de la lista campos y la volvemos un entero
		self.altura_sobre_mar = int(self.campos[-2]) #hacemos lo mismo con la altura del terreno sobre el mar
		'''
		Creamos una lista de los labels de la anterior pantalla para mostrarlos en el QListWidget
		'''
		self.etiquetas = ['Entidad', 'Número de Vuelo', 'Faja del vuelo', 'Escala de la fotografía 1',
						  'Altura del vuelo (metros)', 'Distancia focal', 'Altura sobre el nivel del mar',
						  'Fecha en que se tomó la fotografía']

		'''
		Configuración del título
		'''
		
		self.label_t = QLabel("Cálculos", self) #instanciamos un label
		self.label_t.setGeometry(0, 20, 800, 40)  #definimos las propiedades geométricas del label
		self.label_t.setAlignment(Qt.AlignHCenter)	#Aliniamos el label en el centro de la pantalla
		self.label_t.setFont(QFont('Times', 24))	#Definimos la fuente del label

		#label en donde se pide la fotografía
		self.label_f = QLabel("Abrir fotografía:", self)
		self.label_f.setGeometry(50, 70, 800, 30)
		self.label_f.setAlignment(Qt.AlignLeft)
		self.label_f.setFont(QFont('Times', 15))

		
		#boton para abrir imagen
		self.btn_abrir = QPushButton("...", self)	#instanciamos un boton
		self.btn_abrir.setGeometry(0, 0, 70, 20)
		self.btn_abrir.move(250, 70)
		self.btn_abrir.setStyleSheet("background-color: rgb(166, 152, 149)")
		self.btn_abrir.clicked.connect(self.abrir)
		
		#Ahora creamos un QListWidget para mostrar la información de la fotografía

		#En label de la información de la fotografía
		self.label_info = QLabel("Información de la fotografía", self)
		self.label_info.setGeometry(600, 200, 800, 40)
		self.label_info.setFont(QFont('Times', 14))


		'''
		Creamos un QListWidget y utilizamos un ciclo for para llenarlo con los datos de la anterior
		pantalla
		'''
		self.list_info = QListWidget(self)
		for i in range (len(self.campos)):
			self.list_info.insertItem(i, f'{self.etiquetas[i]}: {self.campos[i]}')

		self.list_info.move(600, 250)
		self.list_info.setStyleSheet("background-color: rgb(255, 255, 255)")

		#calculo de la altura del terreno
		self.label_a_t = QLabel(f"La áltura del terreno es de: {self.calAlturaTerreno()} metros", self)
		self.label_a_t.setGeometry(550, 500, 800, 30)
		self.label_a_t.setFont(QFont('Times', 14))

		self.label_img = QLabel("Cargar imágen", self)
		self.label_img.setGeometry(20, 125, 500, 400)
		self.label_img.setStyleSheet("background-color: rgb(255, 255, 255)")

		self.label_v_p = QLabel("Vista previa", self)
		self.label_v_p.setGeometry(240, 550, 800, 30)
		self.label_v_p.setFont(QFont('Times', 14))


		self.btn_dibujar = QPushButton("Dibujar",self)	#instanciamos un boton
		self.btn_dibujar.setGeometry(240, 600, 100, 50)
		self.btn_dibujar.setStyleSheet("background-color: rgb(255, 255, 0)")
		self.btn_dibujar.clicked.connect(self.dibujar)


		self.label_er = QLabel("", self)
		self.label_er.setGeometry(240, 650, 800, 30)
		self.label_er.setFont(QFont('Times', 14))
		self.label_er.setStyleSheet("color: red")
	

	def abrir(self):
		'''
		Esta funcón nos permite acceder al directorio para abrir una imágen
		'''
		self.file_imagen_name = QFileDialog.getOpenFileName(self, 'Abrir imagen', os.getcwd())
		'''
		ya que self.file_imagen_name es una tupla que contiene la ruta de la imagen y su tipo de dato
		lo que se debe hacer es solo acceder al item de la ruta y por eso accedemos al item
		en la posición 0
		'''
		self.image_name = self.file_imagen_name[0] 
		self.pixi = QPixmap(self.image_name).scaled(500, 400)
		self.label_img.setText("")
		self.label_img.setPixmap(self.pixi)
	

	
	def calAlturaTerreno(self):
		self.altura_terreno = (self.altura_sobre_mar - self.altura_vuelo)
		return self.altura_terreno
	
	def dibujar(self):
		if self.label_img.text():
			'''
			Si no hay ninguna imágen cargada no permite ir a la siguiente pantalla
			'''
			self.label_er.setText("no hay ninguna imágen cargada, intentalo nuevamente")
		else:
			'''
			Una vez cargada la imágen, abrimos una pantalla que recibe como parámetro 
			la imágen y su ruta para ser utilizadas en la siguiente pantalla
			'''
			self.label_er.setText("")
			self.w_d = Dialogo(self.pixi, self.image_name)
			self.w_d.show()
