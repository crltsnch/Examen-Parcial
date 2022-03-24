# Examen-Parcial
El enlace a mi repositorio es: https://github.com/crltsnch/Examen-Parcial.git

Ejercicio 1:
````
class libro():
    def __init__(self, autor, titulo, genero):
        self.autor = autor
        self.titulo = titulo
        self.genero = genero

    def libro1(self):
        titulo = input("Escriba el titulo de un libro: ")
        autor = input("Escriba su autor: ")
        genero = input("Escriba su genero: ")


print(libro.libro1("titulo, autor, genero"))
```

Ejercicio 2:
```
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

```
Ejercicio 4:
```
class CuentaBancaria():
    def __init__ (self, ID, titular, fecha, ndecuenta, saldo):
        self.ID = ID
        self.titular = titular
        self.fecha = fecha
        self.ndecuenta = ndecuenta
        self.saldo = saldo

    #ingresar, retirar, transferir
    def RetirarDinero(self, reintegro):
        reintegro = int(input("¿Qué cantidad de dinero desea retirar? "))
        if self.saldo > reintegro:
            self.saldo = self.saldo - (reintegro + reintegro*0,05)
            print("Su nuevo saldo es " + self.saldo)
        else:
            print("No hay saldo suficiente")

    def IngresarDinero(self, ingreso):
        ingreso = int(input("¿Qué cantidad de dinero desea ingresar? "))
        self.saldo = self.saldo + ingreso
        print("Su nuevo saldo es " + self.saldo)

    def TransferirDinero(self, transferido):
        transferido = int(input("¿Qué cantidad de dinero desea transferir?"))
        if self.saldo > transferido:
            self.saldo = self.saldo - (transferido + transferido*0,05)
            print("Su nuevo saldo es " + self.saldo)
        else:
            print("No hay saldo suficiente")
    ```
