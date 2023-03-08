from datetime import datetime
import time

def get_instantiation_time(self):
    return self.instantiation_time

class My_Meta(type):
    """
    The class will modify all subclasses.

    ...

    Attributes
    ----------
    obj : class
        subclass belongs to superclass
        
    classes: list
        append the list with all subclasses involved

    Methods
    -------
    __new__(additional=""):
        * equipping all newly instantiated classes with time stamps, persisted in a class attribute named instantiation_time;
    * equipping all newly instantiated classes with the get_instantiation_time() method.  
    """
    classes = []
    
    
    
    def __new__(mcs, name, bases, dictionary):
        """
        Enter to the subclass and create new method of time to see the execution time
        and creat

        Parameters
        ----------
            obj : class
                modified subclass
        
        Returns
        -------
        modified subclass
        """
        if 'get_instantiation_time' not in dictionary:
            dictionary['get_instantiation_time'] = get_instantiation_time
        
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.instantiation_time = datetime.now()
        My_Meta.classes.append(name)
        return obj
    
class Test(metaclass=My_Meta):
    pass
class Test2(metaclass=My_Meta):
    pass
class Test3(metaclass=My_Meta):
    pass

t1 = Test()
t2 = Test2()
t3 = Test3()

# print('The class Test was created at:', t1.get_instantiation_time())
# print('The class Test2 was created at:', t2.get_instantiation_time())
# print('The class Test3 was created at:', t3.get_instantiation_time())
# print('My_Meta class was used in following classes', My_Meta.classes)