"""
Vectores/Listas

Como vimos en la parte teórica, los vectores son una estructura de dato organizada que nos permite 
almacenar información. Una de las implementaciones más utilizadas es Python son las listas (List). 

Nota: En Python hay algunas diferencias menores entre un arreglo (array) y una lista, 
pero por ahora vamos a asumir que son lo mismo.

Vamos a ver una definición de esta estructura en Python. Para crear una lista, utilizamos los corchetes 
y separamos los valores de nuestra estructura con una coma. 

Por ejemplo, en la siguiente instrucción estamos creando una lista llamada a con los valores 1, 3, 2, 5, 2.
"""

def ejemplo1():
    a = [1, 3, 2, 5, 2]
    print(a)

ejemplo1()

#Las listas no necesariamente tienen que ser de números, también pueden ser de texto:
def ejemplo2():
    nombres = ["María", "Juan","Andrés"]
    print(nombres)

#ejemplo2()

#Aquí van algunas funciones útiles cuando trabajamos con listas.
#    append(x) - inserta un nuevo valor x al final de la lista
#    remove(x) - remueve el primer valor X de la lista
#    pop([i]) - remueve el valor en la posición i. pop() remueve el último valor de la lista
#    len(x) - permite calcular el tamaño de una lista
#
# Ahora, veamoslas en acción
def ejemplo3():
    nombres = ["María", "Juan","Andrés"]
    nombres.append("Jorge")
    print(nombres)
    print(len(nombres))

    nombres.remove("Juan")
    print(nombres)
    print(len(nombres))

    nombres.pop(2)
    print(nombres)
    print(len(nombres))
#ejemplo3()

#Actividad 1

# Usando el conocimiento de ciclos, crea una funcion numeros que tenga una lista con los numeros pares del 1 al 10 
# y usa un ciclo para que los imprima

#actividad1()

listaNumeros = []

def llenarLista():
    for i in range(1,11):
        if i %2 == 0:
            listaNumeros.append(i)
    print(listaNumeros)
    for i in listaNumeros:
        print(i)

llenarLista()
    
    

#Actividad 2
#
#Escribamos un programa que nos permita crear una lista de 6 números aleatorios entre 1 y 20 en Python, y 
#creemos dos funciones que reciban la lista como parámetro de la siguiente forma:
#
#    mayor(x) - Una función que imprima el número mayor valor de una lista x
#    primos(x) - Una función que imprima los números de la lista que son números primos

#actividad2()

#lista 6 num entre 1 y 20
#2 def(lista) 
# def 1 imprime num mayor
# def 2 imprime todos los primos

import random

numberList = []

for i in range(0,6):
    numberList.append(random.randint(1,20))

print(f"Lista números: {numberList}")

def largestNumber(numberList):
    auxVar = 0
    for i in numberList:
        if i > auxVar:
            auxVar = i
    print(f"Número más grande: {auxVar}")

def oddNumber(numberList):
    auxList = []
    for i in numberList:
        if i % 2 != 0:
            auxList.append(i)
    print(f"Lista impares: {auxList}")
    for i in auxList:
        print(f"Lista impares uno por uno: {i}")


oddNumber(numberList)
largestNumber(numberList)