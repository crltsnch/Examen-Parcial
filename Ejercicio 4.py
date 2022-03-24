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
            self.saldo = self.saldo - reintegro
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
            self.saldo = self.saldo - transferido
            print("Su nuevo saldo es " + self.saldo)
        else:
            print("No hay saldo suficiente")
    