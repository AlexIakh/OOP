#-------------------- PART- I ---------------------
#-------------------- UNITTEST --------------------

import unittest

def add(x,y):
    return x + y

def upper_text(word):
    return word.upper()

class MyTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add(3,4), 7)
        
    def test_2(self):
        self.assertEqual(add(3,4), 6)

    def test_3(self):
        self.assertTrue(upper_text("name") == "NAME")
        
    def test_4(self):
        self.assertTrue(upper_text("name") == 151)
    
    def test_5(self):
        self.assertIn('h', ['1', '2', '/', 'g', 'h'])
        
if __name__ == '__main__':
    unittest.main()
    
#-------------------- PART- II -------------------   
#-------------------- PYTEST ---------------------
import pytest

class BatteryProblem(Exception):
    pass

class Battery:
    def __init__(self, use=100):
        self.duracion = use
        
    def using_phone(self, use):
        if self.duracion < use:
            raise BatteryProblem("El telefono sera apagado!!!")
        else:
            self.duracion -= use
    
    def charge_battery(self, use):
        if (self.duracion + use) > 100:
            self.duracion = 100
        else:
            self.duracion += use
        

    
def test_capacity_initial():
    battery = Battery(100) 
    assert battery.duracion == 100
    
def test_capacity_inicial_2():
    battery = Battery(100) 
    assert battery.duracion == 0
    
def test_using_phone():
    battery = Battery(100) 
    with pytest.raises(BatteryProblem):
        battery.using_phone(101)
    
def test_using_phone_2():
    battery = Battery(100) 
    battery.using_phone(50)
    assert battery.duracion == 50
    
def test_charge_battery():
    battery = Battery(50) 
    battery.charge_battery(100)
    assert battery.duracion == 150
    
def test_charge_battery_2():
    battery = Battery(60) 
    battery.charge_battery(13)
    assert battery.duracion == 73