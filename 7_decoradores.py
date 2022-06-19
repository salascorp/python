#closure: es una función que contiene una función anidada que llama un valor de alcance superior y retorna la función anidada
#Decorador: Función que recibe como parámetro otra función, le añade cosas, y retorna una función diferente.


# def decorador(func):
#     def envoltura():
#         print('Esto se añade a mi función original')
#         func()
#     return envoltura

# def saludo():
#     print('¡Hola!')
# saludo=decorador(saludo)

# saludo()

# def decorador(func):
#     def envoltura():
#         print('Esto se añade a mi función original')
#         func()
#     return envoltura

# @decorador
# def saludo():
#     print('¡Hola!')

# saludo()

# def mayusculas(func):
#     def envoltura(texto):
#         return func(texto).upper()
#     return envoltura

# @mayusculas
# def mensaje(nombre):
#     return f'{nombre}, recibiste un mensaje'

# print(mensaje('cesar'))

from datetime import datetime
import pyrsistent
from pyrsistent import b

def execution_time(func):
    def wrapper(*args,**kwargs):
        initial_time=datetime.now()
        func(*args,**kwargs)
        final_time=datetime.now()
        time_elapsed=final_time-initial_time
        print("pasaron "+ str(time_elapsed.total_seconds()) +" segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1,1000000000):
        pass

#random_func()

@execution_time
def suma(a: int, b:int) -> int:
    return a+b

suma(5,5)