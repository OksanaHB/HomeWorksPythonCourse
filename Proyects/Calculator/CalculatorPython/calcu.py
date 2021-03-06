import sys, math
from PyQt5 import QtCore, uic, QtWidgets


form_class = uic.loadUiType("calculator.ui")[0]

def calcular_fibonachi(n):
  if n<=1:
    return 0
  if n==2:
    return 1
  else:
    a, b = 0,1
    for i in range(n-2):
        a, b = b, a + b
    return b

def num(self,s):
    self.textB.insertPlainText(s)


def label_mostrar(self,part1,part2):
    self.MyLabel.clear()
    self.MyLabel.setText(str(part1)+" = " + str(part2))
def calcular_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_factorial(n-1)

def operador(self,op):
  div = self.textB.toPlainText()
  if(validarExpresion(div)):
    nuevo = div + op
    pantalla(self,nuevo)

def pantalla(self,a):
  self.textB.clear()
  self.textB.insertPlainText(a)

def validarExpresion(div):
  ultimo = div[len(div)-1]
  simbolos = "+-*/."
  encontro = True
  for i in range(len(simbolos)):
    if(simbolos[i] == ultimo):
      encontro = False
      break
  return encontro

def calcular_num (div):
  resultado = eval(str(div))
  return resultado
  

def calcular (self,div):
  if (len(div)>2):
    try:
     resultado = eval(str(div))
     label_mostrar(self,div,resultado)
     pantalla(self,str(resultado))

    except:
      error(self)
  else:
    pantalla(self,"Введіть вираз для обчислення: ")

def error(self):
  p=self.textB.toPlainText()
  self.textB.clear()
  self.textB.insertPlainText("Цей вираз містить помилки:"+p)

class MyWindowClass(QtWidgets.QMainWindow, form_class):
 def __init__(self, parent=None):
    QtWidgets.QMainWindow.__init__(self, parent)
    self.setupUi(self)
    self.bt1.clicked.connect(self.btuno)
    self.bt2.clicked.connect(self.btdos)
    self.bt3.clicked.connect(self.bttres)
    self.bt4.clicked.connect(self.btcuatro)
    self.bt5.clicked.connect(self.btcinco)
    self.bt6.clicked.connect(self.btseis)
    self.bt7.clicked.connect(self.btsiete)
    self.bt8.clicked.connect(self.btocho)
    self.bt9.clicked.connect(self.btnueve)
    self.bt0.clicked.connect(self.btcero)
    self.btmas.clicked.connect(self.btms)
    self.btmenos.clicked.connect(self.btmen)
    self.btpor.clicked.connect(self.btpo)
    self.btdiv.clicked.connect(self.btdi)
    self.btpunto.clicked.connect(self.btpu)
    self.btdes.clicked.connect(self.btd)
    self.btclear.clicked.connect(self.bc)
    self.btparI.clicked.connect(self.parI)
    self.btparD.clicked.connect(self.parD)
    self.btcal.clicked.connect(self.igu)
    self.btpot.clicked.connect(self.pot)
    self.btrad.clicked.connect(self.rad)
    self.btfactorial.clicked.connect(self.factorial)
    self.btfib.clicked.connect(self.fibonachi)


 
 def btuno(self):
    return num(self,"1")
 def btdos(self):
    return num(self,"2")
 def bttres(self):
    return num(self,"3")
 def btcuatro(self):
    return num(self,"4")
 def btcinco(self):
    return num(self,"5")
 def btseis(self):
    return num(self,"6")
 def btsiete(self):
    return num(self,"7")
 def btocho(self):
    return num(self,"8")
 def btnueve(self):
    return num(self,"9")
 def btcero(self):
    return num(self,"0")
 def parI(self):
    return num(self,"(")
 def parD(self):
    return num(self,")")
 
 def btms(self):
  return operador(self,'+')
 def btmen(self):
  return operador(self,'-')
 def btpo(self):
  return operador(self,'*')
 def btdi(self):
  return operador(self,'/')
 def btpu(self):
  return operador(self,'.')
 def btd(self):
  p = self.textB.toPlainText()
  pa = ""
  for i in range(len(p)):
    if (i == (len(p)-1)):
      pa += ""
    else:
         pa += p[i]
    pantalla(self,str(pa))
 def bc(self):
  self.MyLabel.clear()
  self.textB.clear()

 def igu(self):
  div = self.textB.toPlainText()
  calcular(self,div)

 def pot(self):
  p = self.textB.toPlainText()
  r = pow(float(p),2)
  label_mostrar(self,"("+str(p)+")²",str(r))
  pantalla(self,str(r))

 def rad(self):
  p = self.textB.toPlainText()
  r = math.sqrt(float(p))
  label_mostrar(self,"√("+str(p)+")",str(r))
  pantalla(self,str(r))

 def factorial(self):
   div = self.textB.toPlainText()
   p=calcular_num(div)
   r =calcular_factorial(int(p))
   label_mostrar(self,"("+str(int(p))+")!",str(r))
   pantalla(self,str(r))

 def fibonachi(self):
   div = self.textB.toPlainText()
   p=calcular_num(div)
   r =calcular_fibonachi(int(p))
   label_mostrar(self,"Fibonachi("+str(int(p))+")",str(r))
   pantalla(self,str(r))

app = QtWidgets.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()
