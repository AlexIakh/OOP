# -------- try, except, finally ---------

#try:
#    '3'+2
#except ZeroDivisionError:
#    print("Error1")
#except NameError:
#    print("Error2")
#except Exception as e:
#    print("Error3", e)
#else:
#    print("Se ejecuta siempre que no se ejecute el except")
#finally:
#    print("Se ejecuta siempre")
#  


  
# ---------   raise ---------
# Nos permite lanzar las exepciones

#a= 2
#b=0
#if b==0:
#    raise ZeroDivisionError("No se puede dividir entre 0")
#else:
#    a/b
    
    
# ---------   assert ---------
# nos permite ralizar compobaciones
# compueba una condicion e si es falsa laanza una excepcion

#assert False, "Mensaje personalizadoo de Assert"

# assert en testing
def calcular(a, b):
    return a+b

assert(calcular(2, 2) == 4)

def suma_enteros(a, b):
    assert(type(a)==int)
    assert(type(b)==int)
    return a+b

print(suma_enteros(4, 5))

def sumar_enteros(a: int, b:int):
    return a+b

print(sumar_enteros(4.5, 5))

class miExcepcion(Exception):
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        
try:
    raise miExcepcion("Valor param1", "Valor param2")
except Exception as e:
    p1, p2 = e.args
    print(p1, p2)


class miOtraExcepcion(Exception):
    pass

try:
    raise miOtraExcepcion({"Mensaje": "mensaje de la excepcion", "info":"informacion"})
except Exception as e:
    parametros = e.args[0]
    print(parametros["Mensaje"], parametros["mensaje de la excepcion"])

