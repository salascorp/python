def run():
    squares = []

    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    #i elevado al cuadrado para todas las i en el rango de 1 a 101 solo si modulo 3 es distinto de 0
    #elemento para cada elemnto en el iterable solo si la condición
    # [element for element in iterable if condition] Element reprsenta a cada uno de los elementos a poner en la nueva lista - ciclo a partor del cual se extraeran elemtnos de otra lista o cualquier iterable condicion para filtrar los elemtnos del ciclo
    # para cada elemtno en el iterable yo voy a guardar ese elemento solo si cumple la condición

    squares = [i**2 for i in range(1,101) if i % 3 !=0]
    #para cada in en el rango de 1 a 101 voy a gurdar esa i elevada al cuadrado solo si no es divisible por 3
    print(squares)


if __name__=='__main__':
    run()