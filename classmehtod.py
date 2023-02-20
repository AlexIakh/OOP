class Luxury_watch:
    
    __created = 0
    
    def __init__(self):
        Luxury_watch.__created += 1
    
    @classmethod
    def get_created(cls):
        return cls.__created
    
    @classmethod   
    def engraving(cls, text):
        if Luxury_watch.validate(text):
            _watch = cls()
            _watch.text = text
            return _watch
        else:
            print(text + " - The alphanumerical characters whould be without any space\n")
            
    @staticmethod
    def validate(text):
        if len(text) >= 40 or not text.isalnum():
            return False
        return True
        
        
print("Watches created: ", Luxury_watch.get_created())

w1 = Luxury_watch()
print("Watches created: ", Luxury_watch.get_created())
print(w1.engraving(""))

w2 = Luxury_watch.engraving("Hello2")
print("Watches created: ", Luxury_watch.get_created())

w3 = Luxury_watch.engraving("foo@foo.com")
print("Watches created: ", Luxury_watch.get_created())
