class CuentaBancaria():
    def __init__ (self, ID, titular, fecha, ndecuenta, saldo):
        self.ID = ID
        self.titular = titular
        self.fecha = fecha
        self.ndecuenta = ndecuenta
        self.saldo = saldo

#ingresar, retirar, transferir
def RetirarDinero(self, reintegro):
    if self.saldo > reintegro:
        self.saldo = self.saldo - reintegro

    else:
        print("No hay saldo suficiente")

def IngresarDinero(self, ingreso):
    self.saldo = self.saldo + ingreso

