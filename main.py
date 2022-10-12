# ----------------------------------clase SO-------------------------------------------------------
import re


class SO():
    def __init__(self):
        self.memoria = [None] * 100
        self.acumulador = "acumulador"
        self.memoria[0] = self.acumulador
        self.kernel = ["kernel"] * 59
        self.iniciarKernel(self.kernel)
        self.variables = []
        self.etiquetas = []
        self.contMemori = 0
        self.errores = []
        self.variablesDonde = []
        self.variablesNames = []
        self.espacioProgramas = []

    def reiniciarSo(self):
        self.memoria = [None] * 100
        self.acumulador = "acumulador"
        self.memoria[0] = self.acumulador
        self.kernel = ["kernel"] * 59
        self.iniciarKernel(self.kernel)
        self.variables = []
        self.etiquetas = []
        self.contMemori = 0
        self.errores = []
        self.variablesDonde = []
        self.variablesNames = []
        self.espacioProgramas = []

    # cambia el numero del kernel y lo actualiza en la memoria principal
    def cambiarKernel(self, num):
        self.kernel = ["kernel"] * num
        self.iniciarKernel(self.kernel)
        return True

    def iniciarKernel(self, kernel):
        kernelActivador = 1
        self.resetMemory(len(self.memoria))
        while kernelActivador <= len(kernel):
            self.memoria[kernelActivador] = kernel[kernelActivador - 1]
            kernelActivador += 1
        return True

    def resetMemory(self, num):
        self.memoria = [None] * num
        self.memoria[0] = self.acumulador

    def cambiarMemoria(self, num):
        if num > 5100:
            return False
        elif num <= len(self.kernel):
            return False
        else:
            self.memoria = [None] * num
            self.memoria[0] = self.acumulador
            self.iniciarKernel(self.kernel)
            return True

    def getMemoria(self):
        return self.memoria

    def getEtiquetas(self):
        return self.etiquetas

    def getVariables(self):
        return self.variables

    def validarSyntax(self, programa, numeroPrograma):
        variables = []
        etiquetas = []

        nueva = 'nueva \w+ (C [\w+]?|I [\d+]?|R [\d+[.]\d+]?|L [0-1]?)'
        salto = '^\n'
        cargue = 'cargue \w+'
        almacene = 'almacene \w+'
        lea = 'lea \w+ \w+'
        sume = 'sume \w+'
        reste = 'reste \w+'
        multiplique = 'multiplique \w+'
        divida = 'divida \w+'
        potencia = 'potencia [-]?\d+'
        modulo = 'modulo \w+'
        concatene = 'concatene \w+'
        elimine = 'elimine \w+'
        extraiga = 'extraiga \d+'
        Y = 'Y \w+ \w+ \w+'
        O = 'O \w+ \w+ \w+'
        NO = 'NO \w+ \w+'
        muestre = 'muestre \w+'
        imprima = 'imprima \w+'
        retorne = 'retorne [\d+]?'
        vaya = 'vaya \w+'
        vayasi = 'vayasi \w+ \w+'
        etiqueta = 'etiqueta \w+ \d+'
        comentario = '//[\w+ \w+]+'

        contValid = 0
        espacioRetorne = 0
        ubicacionRetorne = 0
        listaErrores = []
        contInvalid = 0
        contItera = 0

        for e in programa:
            if re.search(comentario, e):
                contValid += 1
                contItera += 1
            elif re.search(cargue, e):
                contValid += 1
                contItera += 1
            elif re.search(nueva, e):
                a = e.split(" ")
                nombre = str(numeroPrograma) + a[1]
                aux = {"nombre": nombre, "valor": a[3], "tipo": "variable", "numeroPrograma": numeroPrograma}
                variables.append(aux)
                contValid += 1
                contItera += 1
            elif re.search(salto, e):
                contValid += 1
                contItera += 1
            elif re.search(almacene, e):
                contValid += 1
                contItera += 1
            elif re.search(lea, e):
                contValid += 1
                contItera += 1
            elif re.search(sume, e):
                contValid += 1
                contItera += 1
            elif re.search(reste, e):
                contValid += 1
                contItera += 1
            elif re.search(multiplique, e):
                contValid += 1
                contItera += 1
            elif re.search(divida, e):
                contValid += 1
                contItera += 1
            elif re.search(potencia, e):
                contValid += 1
                contItera += 1
            elif re.search(modulo, e):
                contValid += 1
                contItera += 1
            elif re.search(concatene, e):
                contValid += 1
                contItera += 1
            elif re.search(elimine, e):
                contValid += 1
                contItera += 1
            elif re.search(extraiga, e):
                contValid += 1
                contItera += 1
            elif re.search(Y, e):
                contValid += 1
                contItera += 1
            elif re.search(O, e):
                contValid += 1
                contItera += 1
            elif re.search(NO, e):
                contValid += 1
                contItera += 1
            elif re.search(muestre, e):
                contValid += 1
                contItera += 1
            elif re.search(imprima, e):
                contValid += 1
                contItera += 1
            elif re.search(retorne, e):
                contValid += 1
                contItera += 1
                ubicacionRetorne = contValid
            elif re.search(vaya, e):
                contValid += 1
                contItera += 1
            elif re.search(vayasi, e):
                contValid += 1
                contItera += 1
            elif re.search(etiqueta, e):
                a = e.split(" ")
                nombre = str(numeroPrograma) + a[1]
                aux = {"nombre": nombre, "lugar": a[2], "tipo": "etiqueta", "numeroPrograma": numeroPrograma}
                etiquetas.append(aux)
                contValid += 1
                contItera += 1
            else:
                contItera += 1
                contInvalid += 1
                listaErrores.append(f"Error linea {contItera}")

        if contValid == len(programa):
            if ubicacionRetorne == len(programa) - 1:
                return True, variables, etiquetas
            elif programa[ubicacionRetorne + 1] == "\n":
                return True, variables, etiquetas
            else:
                return True, variables, etiquetas
        elif contInvalid > 0:
            return False, listaErrores

    def llenarMemory(self, programa, variables, etiquetas):
        self.actualizar()
        tamaño = len(programa) + len(variables)
        final = len(self.memoria) - tamaño
        inicio = 0
        fin = 0
        numProg = ""
        if final >= 0:
            inicio = self.contMemori
            for i in programa:
                self.memoria[self.contMemori] = i
                self.contMemori += 1
            for i in variables:
                self.memoria[self.contMemori] = i
                self.variables.append(i)
                variable = {"nombre": i["nombre"], "numeroPrograma": i["numeroPrograma"], "posicion": self.contMemori}
                self.variablesDonde.append(variable)
                self.contMemori += 1
                numProg = i["numeroPrograma"]
            fin = self.contMemori
            for i in etiquetas:
                self.etiquetas.append(i)
            varia = {"inicio": inicio, "fin": fin, "numProg": numProg}
            self.espacioProgramas.append(varia)
            return True
        else:
            return False

    def actualizar(self):
        cont = 0
        for i in self.memoria:
            if i == None:
                self.contMemori = cont
                break
            cont += 1

    def cargue(self, variable, numeroPrograma):
        dato = 0
        variable = str(numeroPrograma) + variable
        for i in self.variables:
            if i["nombre"] == variable:
                dato = i["valor"]
                i["valor"] = int(i["valor"])
        self.memoria[0] = int(dato)

    def almacene(self, variable, numeroPrograma):
        dato = self.memoria[0]
        variable = str(numeroPrograma) + variable
        for i in self.variables:
            if i["nombre"] == variable:
                i["valor"] = int(dato)
        for i in self.variablesDonde:
            if i["nombre"] == variable:
                self.memoria[int(i["posicion"])]["valor"] = self.memoria[0]

    def lea(self, variable, valor):
        dato = valor
        for i in self.variables:
            if i["nombre"] == variable:
                i["valor"] = dato
        for i in self.variablesDonde:
            if i["nombre"] == variable:
                self.memoria[int(i["posicion"])]["valor"] = dato

    def sume(self, variable, numeroPrograma):
        variable = str(numeroPrograma) + variable
        for i in self.variables:
            if i["nombre"] == variable:
                self.memoria[0] = int(self.memoria[0]) + int(i["valor"])

    def reste(self, variable, numeroPrograma):
        variable = str(numeroPrograma) + variable
        for i in self.variables:
            if i["nombre"] == variable:
                self.memoria[0] = int(self.memoria[0]) - int(i["valor"])

    def multiplique(self, variable, numeroPrograma):
        variable = str(numeroPrograma) + variable
        for i in self.variables:
            if i["nombre"] == variable:
                self.memoria[0] = int(self.memoria[0]) * int(i["valor"])

    def divida(self, variable, numeroPrograma):
        variable = str(numeroPrograma) + variable
        for i in self.variables:
            if i["nombre"] == variable:
                if i["valor"] == 0:
                    return False
                self.memoria[0] /= int(i["valor"])

    def potencia(self, variable, numeroPrograma):
        variable = str(numeroPrograma) + variable
        for i in self.variables:
            if i["nombre"] == variable:
                self.memoria[0] = self.memoria ** int(i["valor"])

    def modulo(self, variable, numeroPrograma):
        variable = str(numeroPrograma) + variable
        for i in self.variables:
            if i["nombre"] == variable:
                self.memoria[0] = self.memoria[0] % int(i["valor"])

    def concatene(self, cadena):
        self.memoria[0] = str(self.memoria[0]) + cadena

    def elimine(self, string):
        cadena = self.memoria[0]
        characters = string
        for x in range(len(characters)):
            cadena = cadena.replace(characters[x], "")
        self.memoria[0] = cadena

    def extraiga(self, numero):
        cadena = self.memoria[0]
        cadena = cadena[numero - 1:]
        self.memoria[0] = cadena

    def Y(self, primer, segundo, tercer, numeroPrograma):
        tercer = str(numeroPrograma) + tercer
        for i in self.variables:
            if i["nombre"] == tercer:
                if primer & segundo:
                    tercer = True
                    return tercer
                else:
                    tercer = False
                    return tercer

    def O(self, primer, segundo, tercer, numeroPrograma):
        tercer = str(numeroPrograma) + tercer
        for i in self.variables:
            if i["nombre"] == tercer:
                if primer | segundo:
                    tercer = True
                    return tercer
                else:
                    tercer = False
                    return tercer

    def NO(self, primer, segundo,numeroPrograma):
        segundo = str(numeroPrograma) + segundo
        for i in self.variables:
            if i["nombre"] == segundo:
                return not primer

    def muestre(self, variable, numeroPrograma):
        if variable == "acumulador":
            return self.memoria[0]
        else:
            variable = str(numeroPrograma) + variable
            for i in self.variables:
                if i["nombre"] == variable:
                    return i["valor"]

    def imprima(self, variable, numeroPrograma):
        if variable == "acumulador":
            return self.memoria[0]
        else:
            variable = str(numeroPrograma) + variable
            for i in self.variables:
                if i["nombre"] == variable:
                    return i["valor"]

    def vaya(self, etiqueta, numeroPrograma):
        etiqueta = str(numeroPrograma) + etiqueta
        for i in self.etiquetas:
            if i["nombre"] == etiqueta:
                return i["lugar"]

    def vayasi(self, primero, segundo):
        if int(self.memoria[0]) > 0:
            return primero
        elif int(self.memoria[0]) < 0:
            return segundo
        elif int(self.memoria[0]) == 0:
            return False


# -------------------------------- importar librerias y recursos ------------------------------------------
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QFileDialog, QWidget, QSlider

# ----------------------------------iniciar interfaz-------------------------------------------------
app = QtWidgets.QApplication([])
widget = QWidget()

# ----------------------------------cargar interfaces ui--------------------------------------------
interface = uic.loadUi("interface.ui")

# ----------------------------------variables-------------------------------------------------------
chmaquina = SO()
names = []
proces = []
finalProces = []
memoNum = 0
kerNum = 0
contEjecutar = 0


# ----------------------------------funciones-------------------------------------------------------

# agregamos a procesos pendientes por cargar a la verificacion
def addfile():
    fileName = QFileDialog.getOpenFileNames(widget, "open file", "C://Users/Desktop", "*.ch")
    names.append(fileName[0])


# realizamos la adicion de los procesos a ser verificados y proximos a ejecutados
def loadfile():
    proces.clear()
    for i in names:
        for e in i:
            proces.append(e)
    print(names)
    print(proces)


# restaura el sistema a condiciones iniciales
def resetall():
    names.clear()
    proces.clear()
    interface.screen.clear()
    interface.impres.clear()
    chmaquina.reiniciarSo()
    finalProces.clear()
    actMemoryInterface()
    clearVariables()
    actEtiquetas()
    actProcesos()
    global contEjecutar
    contEjecutar = 0
    interface.correctLed.setStyleSheet("background:green;border-radius:10px;")
    interface.correctLabel.setStyleSheet("color:black")
    interface.failLed.setStyleSheet("background:red;border-radius:10px;")
    interface.failLabel.setStyleSheet("color:black")


# actualiza la memoria segun el numero del slider
def actMemory(dato):
    global memoNum
    memoNum = dato
    interface.numMemory.setNum(memoNum)


# actualiza el kernel segun el numero del slider
def actKernel(dato):
    global kerNum
    kerNum = dato
    interface.numKernel.setNum(kerNum)


# resetea la memoria y actualiza el kernel y el almacenamiento
def setMemoria():
    resetall()
    chmaquina.cambiarMemoria(memoNum)
    chmaquina.cambiarKernel(kerNum)
    print(chmaquina.getMemoria())
    actMemoryInterface()


# ejecutar los programas que tenga cargado en la memoria
def ejecut():
    global contEjecutar
    numeroPrograma = []
    inicio = 0
    fin = 0
    cont = 0
    for i in finalProces:
        numeroPrograma.append(i.split("  ")[0])
    memo = chmaquina.getMemoria()
    for i in chmaquina.espacioProgramas:
        if i["numProg"] == int(numeroPrograma[contEjecutar]):
            inicio = i["inicio"]
            fin = int(i["fin"])
    cont = int(inicio)
    print("sisas")
    while cont <= fin:
        valor = memo[cont].split(" ")
        # interface.ejecutor.setText(memo[cont])
        if valor[0] == "nueva":
            print("sisas pa")
        elif valor[0] == "cargue":
            chmaquina.cargue(valor[1].split("\n")[0], numeroPrograma[contEjecutar])
        elif valor[0] == "almacene":
            chmaquina.almacene(valor[1].split("\n")[0], numeroPrograma[contEjecutar])
        elif valor[0] == "lea":
            interface.botEntrada.setStyleSheet("border:black;color:black;background:grey;")
            interface.entrada.setStyleSheet("border:black")

            def leaInterno():
                dato = interface.entrada.text()
                chmaquina.lea(valor[1], int(dato))

            interface.botEntrada.clicked(leaInterno)
            interface.botEntrada.setStyleSheet("border:white;color:white;background:white;")
            interface.entrada.setStyleSheet("border:white")
        elif valor[0] == "sume":
            chmaquina.sume(valor[1].split("\n")[0], numeroPrograma[contEjecutar])
        elif valor[0] == "reste":
            chmaquina.reste(valor[1].split("\n")[0], numeroPrograma[contEjecutar])
        elif valor[0] == "multiplique":
            chmaquina.multiplique(valor[1].split("\n")[0], numeroPrograma[contEjecutar])
        elif valor[0] == "divida":
            chmaquina.divida(valor[1].split("\n")[0], numeroPrograma[contEjecutar])
        elif valor[0] == "potencia":
            chmaquina.potencia(valor[1].split("\n")[0], numeroPrograma[contEjecutar])
        elif valor[0] == "modulo":
            chmaquina.modulo(valor[1].split("\n")[0], numeroPrograma[contEjecutar])
        elif valor[0] == "concatene":
            chmaquina.concatene(valor[1].split("\n")[0])
        elif valor[0] == "elimine":
            chmaquina.elimine(valor[1].split("\n")[0])
        elif valor[0] == "extraiga":
            chmaquina.extraiga(valor[1].split("\n")[0])
        elif valor[0] == "Y":
            chmaquina.Y(valor[1], valor[2], valor[3].split("\n")[0], numeroPrograma[contEjecutar])
        elif valor[0] == "0":
            chmaquina.O(valor[1], valor[2], valor[3].split("\n")[0], numeroPrograma[contEjecutar])
        elif valor[0] == "NO":
            chmaquina.NO(valor[1], valor[2].split("\n")[0],numeroPrograma[contEjecutar])
        elif valor[0] == "muestre":
            pantalla = chmaquina.muestre(valor[1].split("\n")[0], numeroPrograma[contEjecutar])
            interface.screen.addItem(str(pantalla))
        elif valor[0] == "imprima":
            impresora = chmaquina.imprima(valor[1].split("\n")[0], numeroPrograma[contEjecutar])
            interface.impres.addItem(str(impresora))
        elif valor[0] == "vaya":
            vaya = chmaquina.vaya(valor[1].split("\n")[0], numeroPrograma[contEjecutar])
            cont = inicio + int(vaya)
            continue
        elif valor[0] == "vayasi":
            vaya = chmaquina.vayasi(valor[1], valor[2].split("\n")[0])
            if vaya is False:
                cont += 1
                continue
            else:
                cont = inicio - 1 + int(chmaquina.vaya(vaya, numeroPrograma[contEjecutar]))
                continue
        elif valor[0] == "retorne":
            cont = fin
            contEjecutar += 1
            break
        cont += 1
    actMemoryInterface()
    actVaribles()
    actEtiquetas()


# verifica las sintaxs de los programas cargados si es correcto se carga en memoria
def verSyntax():
    tomemory = []
    tomemoryVariables = []
    tomemoryEtiquetas = []
    tobash = []

    for i in range(len(proces)):
        with open(proces[i], "r") as prog:
            proga = prog.readlines()
            check = chmaquina.validarSyntax(proga, i)
            if check[0] is True:
                interface.correctLed.setStyleSheet("background:green;border-radius:10px;")
                interface.correctLabel.setStyleSheet("color:black")
                interface.failLed.setStyleSheet("background:none;border-radius:10px;")
                interface.failLabel.setStyleSheet("color:white")
                tomemory.append(proga)
                tomemoryVariables.append(check[1])
                tomemoryEtiquetas.append(check[2])
                finalProces.append(f"{i}  {proces[i]}")
                print(f"proces {proces[i]} was {check[0]}")
            else:
                interface.correctLed.setStyleSheet("background:none;border-radius:10px;")
                interface.correctLabel.setStyleSheet("color:white")
                interface.failLed.setStyleSheet("background:red;border-radius:10px;")
                interface.failLabel.setStyleSheet("color:black")
                tobash.append(proga)
                print(f"proces {proces[i]} was {check[0]}")

    for i in range(len(tomemory)):
        chmaquina.llenarMemory(tomemory[i], tomemoryVariables[i], tomemoryEtiquetas[i])

    actMemoryInterface()
    actVaribles()
    actEtiquetas()
    actProcesos()


# actualiza la memoria de la interface
def actMemoryInterface():
    interface.listMemoria.clear()
    memoAux = chmaquina.getMemoria()
    print(memoAux)
    indice = 0
    print(len(memoAux))
    for i in memoAux:
        stri = str(indice) + "    " + str(i)
        interface.listMemoria.addItem(stri)
        indice += 1


# actualiza las etiquetas de la interface
def actEtiquetas():
    interface.listEtiquetas.clear()
    memoAux = chmaquina.getEtiquetas()
    for i in memoAux:
        stri = str(i["numeroPrograma"]) + "  " + str(i["nombre"]) + " " + str(i["lugar"])
        interface.listEtiquetas.addItem(stri)


# actualiza las variables de la interface
def actVaribles():
    interface.listEtiquetas.clear()
    memoAux = chmaquina.getVariables()
    for i in memoAux:
        stri = str(i["numeroPrograma"]) + "  " + str(i["nombre"]) + " " + str(i["valor"])
        interface.listVariables.addItem(stri)


# actualizar procesos de la interface
def actProcesos():
    interface.listProcesos.clear()
    for i in finalProces:
        interface.listProcesos.addItem(i)


def clearVariables():
    interface.listVariables.clear()


# ----------------------------------botones---------------------------------------------------------
interface.abrir.clicked.connect(addfile)
interface.cargar.clicked.connect(loadfile)
interface.reiniciar.clicked.connect(resetall)
interface.ejecutar.clicked.connect(ejecut)
interface.sliderMemory.sliderMoved.connect(actMemory)
interface.sliderKernel.sliderMoved.connect(actKernel)
interface.setMemory.clicked.connect(setMemoria)
interface.sintax.clicked.connect(verSyntax)

# ----------------------------------ejecutar--------------------------------------------------------
interface.show()
app.exec()

# -----------------------------------comentarios para hilos ideas---------------------------------------
"""
fase 2 chmaquina
las lineas de ejecucion van a determinar la prioridad de ejecucion, no se cuentan 
las lineas declarativas (nueva,etiqueta,retorne,comentarios)
    del total de lineas restar los contadores de estas declarativas
tiene que existir un timer con resto al tiempo de ejecucion de los procesos o hilos    


notas de clase 
multiples flujos de informacion pero cada proceso se puede tener 
con multiples procesos de ejecucion, 

multihilado va existir un retraso a la hora de ejecucion, 
por lo que tienen que usar variables de control,
mientras unos hilos estan bloqueados los otro puede que no,
todos compraten recursos,y usted se encarga de mantener 

pensar si crear una clase proceso o tener las propiedades temporales
"""
