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

def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

print(mensaje('cesar'))
