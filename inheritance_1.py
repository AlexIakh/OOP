class Tires:
    
    def __init__(self, size):
        self.size = size
        self.pressure = 0
        
    def get_pressure(self):
        print(f'The pressure in the tire is: {self.pressure} psi')
        return self.pressure
    
    def pump(self, psi):
        self.pressure = psi
        print(f'The pressure in the tire is: {self.pressure} psi')
        
    def __str__(self) -> str:
        return f'The tire size is {self.size}'
    
class Engine:
    
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = 'OFF'
        
    def start(self):
        self.state = 'ON'
        return 'The engine is ON!'
        
    def stop(self):
        self.state = 'OFF'
        return 'The engine is OFF!'
        
    def get_state(self):
        print(f'The engine is: {self.state}')
        return self.state

class Vehicle():
    def __init__(self, VIN,engine, tires):
        self.vin = VIN
        self.engine = engine
        self.tires = tires
        
    def __str__(self) -> str:
        return f'The Vehicle with serial number "{self.vin}" was created\n\tThe engine {self.engine} \n\t{self.tires}'

city_tires = Tires(15)
city_tires.get_pressure()
city_tires.pump(5)

print("")
off_road_tires = Tires(18)
off_road_tires.get_pressure()
off_road_tires.pump(10)

print("")
engine_patrol = Engine('Gas')
engine_patrol.get_state()

print("")
engine_electric = Engine('Electric')
engine_electric.get_state()

print("")
city_car = Vehicle('ES123456', engine_electric, city_tires)
all_terr_car = Vehicle('ES000000', engine_patrol, off_road_tires)

print(f"\tState:\nCity car: ".ljust(20), city_car.engine.start(), end='\n\n')
print(f"\tState:\nAll terrain car: ".ljust(20), all_terr_car.engine.stop(), end='\n\n')

city_car.engine.get_state()
all_terr_car.engine.get_state()
