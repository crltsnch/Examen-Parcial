#Escriba una clase que permita describir un libro y situar los valores asociados. Dar un ejemplo de uso en Python.

class libro():
    def __init__(self, autor, título, genero):
        self.autor = autor
        self.titulo = titulo
        self.genero = genero
