from PyQt5.QtWidgets import QMainWindow, QApplication
import sys 
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QSpinBox, QLineEdit, QHBoxLayout, QComboBox

#VENTANA CON QT

class MainWindow(QMainWindow): 
    def __init__(self): 
        super(MainWindow, self).__init__() 

        widget = QWidget() #Este será el widget principal
        self.setCentralWidget(widget) #Lo ponemos como el principal
        diseño = QHBoxLayout() #Con esto nos sale la operacion en vertical
        widget.setLayout(diseño)

        #Con esto hacemos las casillas de las operaciones
        self.operando1 = QSpinBox () 
        self.operando2 = QSpinBox () 
        self.operacion = QComboBox ()
        [self.operacion.addItem(op) for op in ["+", "-", "*", "/"]] 
        self.resultado = QLineEdit() 
        widgets = [self.operando1, self.operacion, self.operando2, QLabel("="), self.resultado] 
        [diseño.addWidget(widget) for widget in widgets] 

        #Estas dos lineas son para que se envíe la señal de que se han cambiado los numeros de la operacion
        self.operando1.valueChanged.connect(self.calcular) 
        self.operando2.valueChanged.connect(self.calcular)
        self.operacion.currentIndexChanged.connect(self.calcular) #Con currentIndexChanged, cambiamos el resultado cuando se cambian los operandos

        self.calcular() #Lo ponemos aquí para que el valor se vaya actualizando siempre que se cambie un operando en la ventana (funcion calcular más adelante)

    def calcular(self): 
        a = self.operando1.value()
        b = self.operando2.value() 
 
        #Ponemos todas las opciones de operación y devolvemos el resultado correspondiente
        if (self.operacion.currentText() == "+"): 
            resultado = str(a + b) 
        elif (self.operacion.currentText() == "-"): 
            resultado = str(a - b) 
        elif (self.operacion.currentText() == "*"): 
            resultado = str(a * b) 
        elif (self.operacion.currentText() == "/"): 
            # Cogemos la excepción para que no pete con la división entre 0
            try: 
                resultado = str(a / b) 
            except ZeroDivisionError as e: 
                resultado = "División por cero" 
        # Cambiamos el campo texto con el resultado de la operación. 
        self.resultado.setText(resultado) 

app = QApplication(sys.argv) 
window = MainWindow() 
window.show()
sys.exit(app.exec_()) 
