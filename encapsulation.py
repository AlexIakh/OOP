class BankError(Exception):
    pass

class BankAccount:
    def __init__(self, number):
        self.__balance = 0
        self.__number = number
        pass
        
    @property
    def balance(self):
        #return f'The Balance of the acount:\n\t {self.__number}\t{self.__balance}€'
        return self.__balance
        
    @balance.setter
    def balance(self, deposit):
        if deposit < 0:
            raise BankError("Exeption detected: Should not be negative!")
        if deposit > 100000:
            print('This operation will be audited')
        self.__balance = deposit # I could put += to invcrease the balance
            
    @balance.deleter
    def balance(self):
        if self.__balance > 0:
            raise BankError('Can not delete account as long it is not empty')
        self.__balance = None
        
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, value):
        print("Exeption detected: Invalid operation!")
    
    @number.deleter
    def number(self):
        raise BankError("Exeption detected: Invalid operation!")

    def __str__(self) -> str:
        return f'The Balance of the acount:\n\t {self.__number}\t{self.__balance}€\n'
    

ac = BankAccount("ES40 1234 5678 9012 3456")
ac.balance += 500
print(ac)

try:
    ac.balance = -200
except BankError:
    print("Should not be negative!")
  
ac.number ="fasjdlfa"
ac.balance = 1000000


try:
    del ac.balance
except BankError as be:
    print('Exception detected:', be)
