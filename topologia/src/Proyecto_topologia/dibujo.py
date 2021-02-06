from PyQt5.QtWidgets import (QGraphicsScene, QGraphicsView, QDialog, QGridLayout, QPushButton, 
QComboBox, QGraphicsRectItem, QGraphicsPixmapItem)
from PyQt5.QtCore import QPointF, QRectF, Qt
from PyQt5.QtGui import QPen, QBrush, QPolygonF, QPixmap
from PIL import Image

class Paint(QGraphicsView):
 '''
 La clase Paint recive dos parámetros en el constructor una imagen y el nombre de dicha imágen
 '''
 def __init__(self, img=None, img_name=None):
  '''
  Esta clase hereda atributos y métodos de la clase QgraphicsView
  La clase QgraphicsView permite añadir una escena y en dicha escena
  se pueden hacer los dibujos.
  '''
  QGraphicsView.__init__(self)  
  self.setSceneRect(QRectF(self.viewport().rect())) #El Tamaño de la escena va a tener el tamaño de la pantalla original que es Dialogo
  self.scene = QGraphicsScene() #Creamos un objeto tipo QgraphicsScene
  self.isObject = None          #Esta variable inicialmente nula, permite controlar las opciones de que dibujo queremos realizar
  self.startX = None            #Al momento de dibujar, esta variable guarda las cordenadas en x del primer clic
  self.startY = None            #Al momento de dibujar, esta variable guarda las cordenadas en y del primer clic
  self.pointPolygon = None      #Es una tubla de puntos del poligono en x e y
  self.arrayPolygon = []        #Es una lista con cada una de las tuplas de las coordenadas del poligono
  self.puntosX = []             #Es una lista que guarda solo los puntos de x
  self.puntosY = []             #Es una lista que guarda solo los puntos de y
  self.img_name = img_name      

  self.pixi = img.scaled(638, 478)  #Reescalamos la imágen al tamaño de nuestra pantalla
  self.scene.addPixmap(self.pixi)   #añadimos la imágen a la escena
  self.setScene(self.scene)         #enviamso la escena al GraphicsVie
 
 '''
 Esta función nos permite seleccionar que tipo de dibujo queremos hacer
 '''
 def paintObject(self, e):
  if self.isObject != None:
   object = self.isObject
   if object == 1: #Line
    pen = QPen(Qt.red)
    self.scene.addItem(self.scene.addLine(self.startX, self.startY, e.x(), e.y(), pen))
    self.setScene(self.scene)
   elif object == 2: #Rect
    '''
    Solo podemos dibujar un rectangulo para hacer un solo recorte, por eso cada vez que dibujemos
    uno preguntamos si ya hay algún rectangulo en la escena, si es así lo borramos
    '''
    for self.item in self.scene.items():

      x = isinstance(self.item, QGraphicsRectItem)
      if x:
        self.scene.removeItem(self.item)

    pen = QPen(Qt.red)
    brush = QBrush()
    self.scene.addItem(self.scene.addRect(self.startX, self.startY, e.x()-self.startX, e.y()-self.startY, pen, brush))
    self.region = (self.startX, self.startY, e.x(), e.y()) #éste es el rectangulo que obtendremos al recortar
    self.img = Image.open(self.img_name)  #Abrimos la misma imágen que ya teniamos
    self.img_resized = self.img.resize((638, 478))  #La redimensionamos, si no hacemos esto, al momento de recortar, no se obtendra la imagen requerida
    self.img_recortada = self.img_resized.crop(self.region) #Hacemos el recorte
    self.setScene(self.scene) #Enviamos el rectangulo a la escena
    

   elif object == 3: #Ellipse
    pen = QPen(Qt.red)
    brush = QBrush()
    self.scene.addItem(self.scene.addEllipse(self.startX, self.startY, e.x()-self.startX, e.y()-self.startY, pen, brush))
    self.setScene(self.scene)
    
 def paintPolygon(self, e):
  if self.isObject != None:
   object = self.isObject
   if object == 4: #Polygon
    self.pointPolygon = QPointF(e.x(), e.y())
    self.puntosX.append(e.x())
    self.puntosY.append(e.y())
    self.arrayPolygon.append(self.pointPolygon)
    pen = QPen(Qt.green)
    brush = QBrush(Qt.green, Qt.Dense4Pattern)
    self.scene.addItem(self.scene.addPolygon(QPolygonF(self.arrayPolygon), pen, brush))
    self.setScene(self.scene)
 '''
 Esta funcion captura el evento de clickear
 '''
 def mousePressEvent(self, event):
  e = QPointF(self.mapToScene(event.pos()))
  self.startX = e.x()
  self.startY = e.y()
 
 '''
 Esta función actualiza las coordenadas en x e y
 '''
 def mouseReleaseEvent(self, event):
  e = QPointF(self.mapToScene(event.pos()))
  self.paintObject(e)
  self.paintPolygon(e)
 
 '''
 Esta función captura el evento de movimiento del mouse
 '''
 def mouseMoveEvent(self, event):
  e = QPointF(self.mapToScene(event.pos()))

class Dialogo(QDialog):
 def __init__(self, img=None, img_name=None):
  '''
  Esta pantalla hereda de QDialog y es la pantalla en donde se encontrarán los botones de dibujo
  además de recortar y limpiar
  '''
  QDialog.__init__(self)
  self.setFixedSize(638, 600)
  self.layout = QGridLayout()
  self.setLayout(self.layout)
  self.img_name = img_name
  self.img = img
  self.paint = Paint(self.img, self.img_name)
  self.btn_recortar = QPushButton("Recortar")
  self.btn_limpiar = QPushButton("Limpiar")
  self.combo_object = QComboBox() #El QComboBox es donde se encontraran las opciones de dibujo
  '''
  Añadimos elementos al comboBox
  '''
  self.combo_object.addItem("Seleccionar")  
  self.combo_object.addItem("Linea")
  self.combo_object.addItem("recortar")
  self.combo_object.addItem("Elípse")
  self.combo_object.addItem("Polígono")
  '''
  Agregamos todos los Widgets a el gridlayout para que puedan ser visibles
  '''
  self.layout.addWidget(self.combo_object)
  self.layout.addWidget(self.btn_limpiar)
  self.layout.addWidget(self.paint)
  self.layout.addWidget(self.btn_recortar)
  self.btnDefault = "background-color: grey; border: 0; padding: 10px"
  self.btnActive = "background-color: orange; border: 0; padding: 10px"
  
  self.combo_object.setStyleSheet(self.btnDefault)
  
  self.btn_recortar.clicked.connect(self.isRecortar)
  self.combo_object.currentIndexChanged.connect(self.isObject)
  self.combo_object.activated.connect(self.isObject)
  self.btn_limpiar.clicked.connect(self.isLimpiar)
  
  
 def resizeEvent(self, event):
  self.paint.setSceneRect(QRectF(self.paint.viewport().rect()))
   
  
 def isObject(self):
  '''
  Esta función nos permite saber que opción de dibujo fue seleccionada
  '''
  object = self.combo_object.currentIndex()
  self.paint.isObject = object

  '''
  Cada vez que seleccionemos una opción de dibujo debemos borrar los puntos del poligono
  esto debe hacerse para que cuando la opción del poligono se seleccione de nuevo, se cree
  un nuevo poligono y no siga agregando puntos al ya dibujado
  '''
  del self.paint.arrayPolygon[:] 
  del self.paint.puntosX[:]
  del self.paint.puntosY[:]
 

 def isRecortar(self):
  '''
  Esta función nos permite recortar el area del rectangulo dibujado cuando se de clic en el boton
  de recortar, sin embargo es necesario preguntar si en todo el QGraphicsView hay algun item Rectangulo
  en caso de que lo haya recortará dicha área, sino no hace nada  
  '''
  for self.paint.item in self.paint.scene.items():
    x = isinstance(self.paint.item, QGraphicsRectItem)
    if x:
      self.paint.img_recortada.save("imgs/imagen_recortada.png") #Guardamos la imágen recortada
      '''
      Creamos un objeto QPixmap que abra la imagen recortada, y a su vez la añadimos a la escena
      así mismo borramos los puntos del poligono para que cuando se dibuje uno, sea nuevo
      '''
      self.paint.imagen_recortada = QPixmap("imgs/imagen_recortada.png").scaled(638, 478)
      self.paint.scene.addPixmap(self.paint.imagen_recortada)
      self.paint.setScene(self.paint.scene)
      del self.paint.arrayPolygon[:]
      del self.paint.puntosX[:]
      del self.paint.puntosY[:]
      break
    else:
      continue 
  

 def isLimpiar(self):
  '''
  Ya que la imagen es una escena, si pedimos limpiar toda la escena nos va a borrar la imagen también
  por lo que es necesario recorrer la lista de escenas y pedirle que no haga nada cuando la
  escena es la imagen, de esta forma limpiara todo escepto la imágen
  '''
  for self.paint.item in self.paint.scene.items():
    x = isinstance(self.paint.item, QGraphicsPixmapItem)
    if x:
      continue
    else:
      self.paint.scene.removeItem(self.paint.item)
      del self.paint.arrayPolygon[:]
      del self.paint.puntosX[:]
      del self.paint.puntosY[:]  