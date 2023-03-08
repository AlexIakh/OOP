class InsuficienteSaldo(Exception):
    pass

class Wallet:
    
    def __init__(self, cantidad=0):
        self.saldo = cantidad
        
    def gastardinero(self, cantidad):
        if self.saldo < cantidad:
            raise InsuficienteSaldo("No hay suficiente saldo en tuu cuenta")
        else:
            self.saldo -= cantidad
            
    def anadir_saldo(self, cantidad):
        self.saldo += cantidad