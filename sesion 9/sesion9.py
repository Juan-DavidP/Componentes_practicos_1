"""
Funciones

La verdad es que hemos venido trabajando con funciones desde que empezamos con archivos .py 
En Python, definimos una función con la siguiente estructura

def funcion(parametros)

Recuerda que los parametros son opcionales!
"""

# def suma(a,b):
    
#     print(a+b)

# suma(3,4)


#Actividad 1
#Usted es cajero en un supermercado de su ciudad. Su trabajo es imprimir cada uno de los productos de su cliente, su precio y calcular el total a pagar.
#
#Diseña un programa con las siguiente características:
#
#    1. Que tenga una función caja que solicite al usuario nombre y precio de cada producto.
#    2. Una variable total que vaya sumando el precio de los artículos
#    3. Una función adicional llamada imprimaProducto(nombre, precio) que reciba el nombre y
#        el precio de cada producto y los imprima.
#    4. Que después de llamar a imprimaProducto le pregunte al usuario si tiene o no más artículos a ingresar. Si no tiene, el programa debe detenerse.
#    5. Si no hay más artículos, que imprima el total de la compra

#    Al final de tus funciones, puedes simplement llamar a la función caja para probar

# def imprimirProducto(nombreProducto, precioProducto):
#         print(f"nombre: {nombreProducto}, precio: {precioProducto}")

# def caja():
#     print("Bienvenido a su caja para nosotros es un placer atenderlo ^_^")
#     total = 0
#     pregunta = False
#     while pregunta == False:
#         nombreProducto = input("Ingrese el nombre del producto: ")
#         precioProducto = int(input("Ingrese el precio del producto: "))
#         imprimirProducto(nombreProducto, precioProducto)
#         pregunta = input("Desea agregar un nuevo producto S para sí o N para no: ")
#         if pregunta == "NO" or "No" or "no" or "N" or "n":
#              pregunta = True
#         else:
#              pregunta = False
#         total += precioProducto
#     print(f"El valor total de su compra es: {total}")
    

# caja()

#Actividad 2
#
#Escribamos una función numAleatorio() que retorne un número aleatorio entre 100 y 130, 
#excepto los números 110, 115 y 120 .
#
#Adicionalmente, una función numeros que imprima diez números aleatorios 
#(retornados por la función numAleatorio()) alternando par, impar, comenzando por par.

import random

def numAleatorio():
    listaNumeros = []
    for i in range(100,131):
        listaNumeros.append(i)
    numero = random.choice(listaNumeros)
    if numero == 110 or numero == 115 or numero == 120:
        numero = random.choice(listaNumeros)
        return numero
    else:
        # print(numero)
        return numero

# numAleatorio()

def numeros():
    contador = 0
    while contador < 10:
        numeroAleatorio = numAleatorio()
        if contador % 2 == 0 and numeroAleatorio % 2 == 0:  # Par
            print(numeroAleatorio)
            contador += 1
        elif contador % 2 != 0 and numeroAleatorio % 2 != 0:  # Impar
            print(numeroAleatorio)
            contador += 1
        
numeros()

# def numeros():
#     listaNumeros = []
#     for i in range(10):
#         while True:
#             numero = numAleatorio()
#             if len(listaNumeros) % 2 == 0 and numero % 2 == 0:  # Par
#                 listaNumeros.append(numero)
#                 break
#             elif len(listaNumeros) % 2 != 0 and numero % 2 != 0:  # Impar
#                 listaNumeros.append(numero)
#                 break
#     print(listaNumeros)

# numeros()