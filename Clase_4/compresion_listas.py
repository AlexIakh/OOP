# compresion listas

cuadrados = []

for i in range(10):
    cuadrados.append(i**2)
    
cuadrados_2 = [i**2 for i in range(10)]

print(cuadrados)
print(cuadrados_2)

# lista = [expresion for elemento in iterable]

aux = [0 for i in range(2)]
print(aux)

def cuadrado(i):
    return i**2

cuadrados = [cuadrado(i) for i in range(10)]
print(cuadrados)

texto = "Holla mundo"
letras_0 = [i for i in texto if i == 'o']
print(letras_0)

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]

my_dict = {i:j for i, j in zip(l1, l2)}
print(my_dict)

# lambda
def suma(x, y):
    return x+y

x = lambda a,b: a+b
print(x(5,4))

print((lambda a,b: a+b) (2, 5))
print((lambda a,b,c=10: a+b+c) (2, 5))

# programacion funcional
# map

aux = [i for i in range(20)]
print(aux)

def cuadrado(i):
    return i**2

# l_aux = []
# for l in aux:
#     l_aux.append(cuadrado(l))
# 
# print(l_aux)

l_aux = list(map(cuadrado, aux))
print(l_aux)

# filter
# l1 = filter(lambda x: x%2==0, aux)
# print(l1)

# reduce
from functools import reduce

suma = reduce(lambda a, b: a+b, l_aux)
print(suma)