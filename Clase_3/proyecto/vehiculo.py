class Vehiculo(object):
    '''
    The Vehicle object contains lots of vehicles
    :param arg: The arg is used for ...
    :type arf: str
    :param '*atgs': The variable arguments are used for ...
    :param `*kwards`: The keyword arguments are used for ...
    :ivar arf: This is where we store arg
    :vartype arg: str
    '''
    
    def __init__(self, arg, *args, **kwards):
        self.arg = arg
        
    def cars(self, distance, destination):
        '''
        We can`t travel a certain distance in vehicles without gas, so here´s the fuel
        
        :param distance: The amount of distance traveles
        :type amount: int
        :param bool destinationReached: Should the gas be refilled to cover required distance?
        :raises: class:`RuntimeError`: Out of gas
        
        :returns: A car milage
        :rtype: Cars
        '''
        
        pass