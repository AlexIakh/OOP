from wallet import Wallet, InsuficienteSaldo
import pytest

def test_cantidad_inicial():
    mi_wall = Wallet()
    assert mi_wall.saldo == 0
    
def test_cantidad_inicial_2():
    mi_wall = Wallet()
    assert mi_wall.saldo == 10
    
def test_gastar():
    mi_wall = Wallet(100)
    mi_wall.gastardinero(50)
    assert mi_wall.saldo == 50   
    
def test_anadir():
    mi_wall = Wallet(100)
    mi_wall.anadir_saldo(50)
    assert mi_wall.saldo == 150    
    
def test_excepcion():
    mi_wall = Wallet(100) 
    with pytest.raises(InsuficienteSaldo):
        mi_wall.gastardinero(150)