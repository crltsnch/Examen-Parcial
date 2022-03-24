#Escriba una clase que permita describir un libro y situar los valores asociados. Dar un ejemplo de uso en Python.

class libro():
    def __init__(self, autor, título, genero):
        self.autor = autor
        self.titulo = titulo
        self.genero = genero

    def libro1(self):
        titulo = input("Escriba el titulo de un libro: ")
        autor = input("Escriba su autor: ")
        genero = input("Escriba su genero: ")

print(libro.libro1(" ", " ", " "))