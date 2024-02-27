class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.volumen = 1
        self.precio = 500

        TV.numTV += 1

    @staticmethod
    def getNumTV():
        return TV.numTV

    @staticmethod
    def setNumTV(numTV):
        TV.numTV = numTV

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def canalUp(self):
        if self.estado:
            self.setCanal(self.canal + 1)

    def canalDown(self):
        if self.estado:
            self.setCanal(self.canal - 1)

    def volumenUp(self):
        if self.estado:
            self.setVolumen(self.volumen + 1)

    def volumenDown(self):
        if self.estado:
            self.setVolumen(self.volumen - 1)

    def getMarca(self):
        return self.marca

    def getCanal(self):
        return self.canal

    def getPrecio(self):
        return self.precio

    def getVolumen(self):
        return self.volumen

    def getControl(self):
        return self.control

    def getEstado(self):
        return self.estado

    def setMarca(self, marca):
        self.marca = marca

    def setCanal(self, canal):
        if self.estado and 1 <= canal <= 120:
            self.canal = canal

    def setPrecio(self, precio):
        self.precio = precio

    def setVolumen(self, volumen):
        if self.estado and 0 <= volumen <= 7:
            self.volumen = volumen

    def setControl(self, control):
        self.control = control
