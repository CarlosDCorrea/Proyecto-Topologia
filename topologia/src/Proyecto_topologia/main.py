from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QDateEdit, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont, QIntValidator, QDoubleValidator
from calculo import CalApp


class MainApp(QMainWindow):
	"""Esta será la aplicación principal"""
	def __init__(self, parent=None, *args):
		super(MainApp, self).__init__(parent=parent)
		
		'''
		configuración de la pantalla
		'''
		self.setFixedSize(850,600)	#El tamaño por defecto de la pantalla sin permitir ajustes
		self.setWindowTitle("Parámetros de la fotografía aérea")	#Establece el título de la ventana
		self.setStyleSheet("background-color: rgb(85, 255, 127)")  #Establece el color de fondo 
		self.setWindowIcon(QIcon("iconos/main_window.png")) #se establece un ícono para la pantalla
		'''
		Configuración del título
		'''
		self.label_t = QLabel("Definir los parámetros de la fotografía aérea", self) #instanciamos un label
		self.label_t.setGeometry(0, 20, 800, 40)  #definimos las propiedades geométricas del label
		self.label_t.setAlignment(Qt.AlignHCenter)	#Aliniamos el label en el centro de la pantalla
		self.label_t.setFont(QFont('Times', 24))	#Definimos la fuente del texto del label
		'''
		Configuración de los labels e inputs
		'''

		#label 1 entidad
		self.label_e = QLabel("Entidad de donde proviene la fotografía:", self)
		self.label_e.setGeometry(50, 100, 800, 30)
		self.label_e.setAlignment(Qt.AlignLeft)
		self.label_e.setFont(QFont('Times', 12))
		#input 1 entidad
		self.input_e = QLineEdit(self)	#instanciamos un objeto para realizar una entrada
		self.input_e.move(600, 100)		#movemos el input a estas coordenadas
		self.input_e.resize(200, 25)	#Definimos el tamaño de el campo de texto
		self.input_e.setStyleSheet("background-color: #fff")	#el color del campo de texto será blanco
		self.input_e.setMaxLength(50) 	#definimos la cantidad maxima de carácteres a recibir


		#label 2 número de vuelo
		self.label_n_v = QLabel("Número de vuelo:", self)
		self.label_n_v.setGeometry(50, 150, 800, 30)
		self.label_n_v.setAlignment(Qt.AlignLeft)
		self.label_n_v.setFont(QFont('Times', 12))
		#input 2 número de vuelo
		self.input_n_v = QLineEdit(self)
		self.input_n_v.move(600, 150)
		self.input_n_v.resize(200, 25)
		self.input_n_v.setStyleSheet("background-color: #fff")
		self.input_n_v.setValidator(QIntValidator(0, 30000, self))	#Validamos que solo se acepten valores numéricos con un rango de 0 a 30000

		#label 3 faja de vuelo
		self.label_f_v = QLabel("Faja de vuelo:", self)
		self.label_f_v.setGeometry(50, 200, 800, 30)
		self.label_f_v.setAlignment(Qt.AlignLeft)
		self.label_f_v.setFont(QFont('Times', 12))
		#input 3 faja de vuelo
		self.input_f_v = QLineEdit(self)
		self.input_f_v.move(600, 200)
		self.input_f_v.resize(200, 25)
		self.input_f_v.setStyleSheet("background-color: #fff")
		self.input_f_v.setMaxLength(50)

		#label 4 escala de la fotografía
		self.label_e_f = QLabel("Escala de la fotografía 1:", self)
		self.label_e_f.setGeometry(50, 250, 800, 30)
		self.label_e_f.setAlignment(Qt.AlignLeft)
		self.label_e_f.setFont(QFont('Times', 12))
		#input 4 escala de la fotografía
		self.input_e_f = QLineEdit(self)
		self.input_e_f.move(600, 250)
		self.input_e_f.resize(200, 25)
		self.input_e_f.setStyleSheet("background-color: #fff")
		self.input_e_f.setValidator(QIntValidator(0, 300000, self))

		#label 5 altura del vuelo
		self.label_a_v = QLabel("Altura del vuelo (en metros):", self)
		self.label_a_v.setGeometry(50, 300, 800, 30)
		self.label_a_v.setAlignment(Qt.AlignLeft)
		self.label_a_v.setFont(QFont('Times', 12))
		#input 5 altura del vuelo
		self.input_a_v = QLineEdit(self)
		self.input_a_v.move(600, 300)
		self.input_a_v.resize(200, 25)
		self.input_a_v.setStyleSheet("background-color: #fff")
		self.input_a_v.setValidator(QIntValidator(0, 300000, self))

		#label 6 distancia focal
		self.label_d_f = QLabel("Distancia focal:", self)
		self.label_d_f.setGeometry(50, 350, 800, 30)
		self.label_d_f.setAlignment(Qt.AlignLeft)
		self.label_d_f.setFont(QFont('Times', 12))
		#input 6 distancia focal
		self.input_d_f = QLineEdit(self)
		self.input_d_f.move(600, 350)
		self.input_d_f.resize(200, 25)
		self.input_d_f.setStyleSheet("background-color: #fff")
		self.input_d_f.setValidator(QDoubleValidator(0.0, 1000000.0, 4, self))

		#label 7 altura del terreno sobre el nivel del mar
		self.label_a_t_m = QLabel("Altura del terreno/nivel del mar:", self)
		self.label_a_t_m.setGeometry(50, 400, 800, 30)
		self.label_a_t_m.setAlignment(Qt.AlignLeft)
		self.label_a_t_m.setFont(QFont('Times', 12))
		#input 7 altura del terreno sobre el nivel del mar
		self.input_a_t_m = QLineEdit(self)
		self.input_a_t_m.move(600, 400)
		self.input_a_t_m.resize(200, 25)
		self.input_a_t_m.setStyleSheet("background-color: #fff")
		self.input_a_t_m.setValidator(QIntValidator(0, 300000, self))

		#label 8 fecha en que se tomn_v la fotografía
		self.label_f_f = QLabel("Fecha en que se tomó la fotografía:", self)
		self.label_f_f.setGeometry(50, 450, 800, 30)
		self.label_f_f.setAlignment(Qt.AlignLeft)
		self.label_f_f.setFont(QFont('Times', 12))
		#input 8 fecha en que se tomó la fotografía
		self.input_f_f = QDateEdit(self)
		self.input_f_f.move(600, 450)
		self.input_f_f.resize(200, 25)
		self.input_f_f.setStyleSheet("background-color: #fff")

		'''
		configuración del boton
		'''
		#boton de aceptar
		self.btn_acept = QPushButton("Aceptar", self)	#instanciamos un boton
		self.btn_acept.setGeometry(0, 0, 100, 50)
		self.btn_acept.move(375, 500)
		self.btn_acept.setStyleSheet("background-color: rgb(255, 255, 0)")
		self.btn_acept.clicked.connect(self.slot_aceptar)  #definimos que evento realizará al ser presionado

		self.label_er = QLabel("", self)	#definimos un label de error en caso de no todos los campos estén llenos
		self.label_er.setGeometry(20, 575, 800, 30)
		self.label_er.setAlignment(Qt.AlignHCenter)
		self.label_er.setFont(QFont('Times', 12))
		self.label_er.setStyleSheet("color: red")


		#Este es el evento que se va a ejecutar si se da en aceptar
	def slot_aceptar(self):
		#Creamos una lista con los textos de los campos para verificiar si están vacíos o no
		self.campos = []
		self.campos.extend([self.input_e.text(), self.input_n_v.text(), self.input_f_v.text(), 
							self.input_e_f.text(), self.input_a_v.text(), self.input_d_f.text(), 
							self.input_a_t_m.text(), self.input_f_f.text()]) 

		#Recorremos la lista anteriormente creada
		for i in self.campos:
			'''
			ya que cada valor de i es un texto podemos preguntar si ese texto esta vacío o no
			de tal forma que aquí preguntamos si el texto es falso, es decir no hay texto, entonces
			mande un mensaje de error
			'''
			if not i: 
				return self.label_er.setText("Uno o más campos están vacíos, Vuelve a intentarlo")
		else:
			'''
			Una vez verificado que los campos están llenos, validamos que el valor de la altura 
			del terreno sobre el mar es mayor a la altura de la fotografía, si esto no es así
			mandamos un mensaje de error pidiendo que se ingresen valores validos
			'''
			if int(self.campos[4]) >= int(self.campos[-2]):
				return self.label_er.setText("La altura del vuelo no puede ser mayor o igual a la altura del terreno sobre  el mar")
			else:
				#Creamos un objeto de tipo CalApp para posteriormente mostrarla
				self.w = CalApp(self.campos)	#Mandamos la lista de campos como parámetro
				self.w.show()	#mostramos la pantalla


if __name__ == '__main__':
	'''
	QAplication solo se debe llamar una vez por aplicación
	'''
	app = QApplication([]) 	#primero debe iniciarse la aplicación
	window = MainApp()	 	#Se establece una ventana principal
	window.show() 			#se muestra la ventana principal
	app.exec_()				#ejecutamos la aplicación

