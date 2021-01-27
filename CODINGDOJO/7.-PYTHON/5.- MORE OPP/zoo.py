class Animal:

    def __init__(self,nombre,edad,salud,felicidad):
        
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.felicidad = felicidad

    def display_info(self):
        print('Nombre: %s\tSalud: %s\tFelicidad: %s'%
        (self.nombre, self.salud, self.felicidad))

    def alimentar(self):
        self.salud +=10
        self.felicidad +=10


class Condor(Animal):

    def __init__(self,nombre,edad,salud=20,felicidad=40,altitud=4000):
        
        super().__init__(nombre,edad,salud,felicidad)
        self.altitud = altitud

    def alimentar(self):
        self.salud += 15
        felicidad += 5


class Rinoceronte(Animal):

    def __init__(self,nombre,edad,salud=40,felicidad=10):
        
        super().__init__(nombre,edad,salud,felicidad)
        

    def alimentar(self):
        self.salud += 10
        felicidad += 20

class Jirafa(Animal):

    def __init__(self,nombre,edad,salud=40,felicidad=10,estatura=10):
        
        super().__init__(nombre,edad,salud,felicidad)
        self.estatura = estatura

    def alimentar(self):
        self.salud += 10
        felicidad += 10


class Zoo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []

    def add_condor(self,nombre,edad):
        condor = Condor (nombre,edad)
        self.animales.append(condor)

    def add_jirafa(self,nombre,edad):
        jirafa = Jirafa (nombre,edad)
        self.animales.append(jirafa)


    def print_all_info(self):
        for animal in animales:
            animales.display_info()

