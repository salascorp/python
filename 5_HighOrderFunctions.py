#Una función de order superior es una función que recibe como parametro otra función

# def saludo(fun):
#     fun()

# def hola():
#     print('hola funcion')

# saludo(hola)

#Usando la función filter

my_list=[1,2,3,4,5,6,7,8,9,10]

odd=list(filter(lambda x: x%2 !=0,my_list))

print (odd)

my_list=[1,2,3,4,5,6,7,8,9,10]

odd1=list(filter(lambda x: x**2,my_list))

print (odd1)

from functools import reduce

my_list2=[2,2,2,2,2]

all_multiplied=reduce(lambda a,b: a*b,my_list2)

print(all_multiplied)