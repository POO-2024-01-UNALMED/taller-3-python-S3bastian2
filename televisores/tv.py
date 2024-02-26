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