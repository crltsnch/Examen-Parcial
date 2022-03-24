#Considere los objetos siguientes: Animal, Mamífero, Ovíparo, Pollo, Gato, Ornitorrinco
#Describa las relaciones entre los diferentes objetos. El diagrama asociado se llama diagrama de clases.
#Dar un ejemplo de descripción algorítmica de las clases asociadas (únicamente la declaración de clase XXX).
#¿Es posible implementar estos objetos en Python? Sí, es posible.

class Animal():
    def __init__(self, nombre, especie, nacimiento) :
        self.nombre = nombre
        self.especie = especie
        self.nacimiento = nacimiento

    def getNombre(self):
        return self.nombre
    def getEspecie(self):
        return self.especie
    def getNacimiento(self):
        return self.nacimiento
    
    def Animal1(self):
        print("Nombre: " + self.getNombre())
        print("Eespecie: " + self.getEspecie())
        print("Nacimiento: " + self.getNacimiento())

nombre = input("Dime el tipo de animal: ")
especie = input("Dime el tipo de especie: ")
nacimiento = input("Tipo de animal según su nacimiento: ")
a = Animal(nombre, especie, nacimiento)

a.Animal1()
