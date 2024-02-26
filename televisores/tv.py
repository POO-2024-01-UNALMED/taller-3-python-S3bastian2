class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self.__marca = marca
        self.__canal = 1
        self.__precio = 500
        self.__estado = estado
        self.__volumen = 1
        self.control = None
        tv.numTV += 1
    
    def setMarca(self, marca):
        self.__marca = marca

    def getMarca(self):
        return self.__marca
    
    def setCanal(self, canal):
        self.__canal = canal

    def getCanal(self):
        return self.__canal
    
    def setPrecio(self, precio):
        self.__precio = precio
    
    def getPrecio(self):
        return self.__precio
    
    def setVolumen(self, volumen):
        self.__volumen = volumen

    def getVolumen(self):
        return self.__volumen
    
    def setControl(self, control):
        self.__control = control

    def getControl(self):
        return self.control 
    
    def turnOn(self):
        self.__estado = True
    
    def turnOff(self):
        self.__estado = False
    
    def getEstado(self):
        return self.__estado
    
    def getNumTV(cls):
        return cls.numTV
    
    def setNumTV(cls, num):
        cls.numTV = num