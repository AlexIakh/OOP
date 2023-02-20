import abc

class Scanner(abc.ABC):
    def scan_document(self):
        return 'Document was scanned'

    @abc.abstractmethod
    def get_scanner_status(self):
        pass

class Printer(abc.ABC):
    def print_document(self):
        return 'Document was printed'

    @abc.abstractmethod
    def get_printer_status(self):
        pass

class MFD1(Scanner, Printer):
    def get_scanner_status(self):
        return 'Max scan resolution is low, S/N: S001'

    def get_printer_status(self):
        return 'Max print resolution is low, S/N: P001'

class MFD2(Scanner, Printer):
    def get_scanner_status(self):
        return 'Max scan resolution is fine, S/N: S002'

    def get_printer_status(self):
        return 'Max print resolution is fine, S/N: P002'

    def get_history(self):
        return 'The history is...'

class MFD3(Scanner, Printer):
    def get_scanner_status(self):
        return 'Max scan resolution is high, S/N: S003'

    def get_printer_status(self):
        return 'Max print resolution is high, S/N: P003'

    def get_history(self):
        return 'The history is...'

    def send_fax(self):
        print('sending fax')

    def receive_fax(self):
        print('receiving fax')
mfd1 = MFD1()
print(mfd1.print_document())
print(mfd1.get_printer_status())

mfd2 = MFD2()
print(mfd2.print_document())
print(mfd2.get_printer_status())

mfd3 = MFD3()
print(mfd3.print_document())
print(mfd3.get_printer_status())
