class BaseComputer:
    def __init__(self, serial_number):
        self.serial_number = serial_number
        
class Personal_Computer(BaseComputer):
    def __init__(self, sn, connection):
        super().__init__(sn)
        self.connection = connection
        print("The computer costs 100$")
        
class Connection:
    def __init__(self, speed):
        self.speed = speed
        
    def download(self):
        print(f"Downloading at {self.speed}")

class DialUp(Connection):
    def __init__(self):
        super().__init__('9600bit/s') 
        
    def download(self):
        print('Dialling the access number ...'.ljust(40), end='')
        super().download()

class ADSL(Connection):
    def __init__(self):
        super().__init__('2Mbit/s') 
        
    def download(self):
        print('Dialling the access number ...'.ljust(40), end='')
        super().download()
        
class Ethernet(Connection):
    def __init__(self):
        super().__init__('10Mbit/s') 
        
    def download(self):
        print('Dialling the access number ...'.ljust(40), end='')
        super().download()
        
my_compyter = Personal_Computer('1995', DialUp())
my_compyter.connection.download()

my_compyter.connection = ADSL()
my_compyter.connection.download()

my_compyter.connection = Ethernet()
my_compyter.connection.download()
