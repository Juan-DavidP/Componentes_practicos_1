"""
Mientras Que

Como vimos anteriormente, en Python, el ciclo Mientras Que se maneja con "while". 

Por ejemplo:
"""


# i = 1
# while i < 6:
#     print(i)
#     i += 1



# print("actividad1")
# Continuemos integrando los conceptos que hemos visto hasta el momento. 
# Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número. 

# Comentar las instrucciones anteriores para ejecutar las siguientes
# i = 2
# numUsuario = int(input("Ingrese un número mayor a dos hasta donde desea que se impriman los números en pantalla:"))

# while i < numUsuario:
#     i += 2
#     if i > numUsuario:
#         print("El número calculado es mayor al ingresado")
#     else:
#         print(i)        



# print("actividad2")
#Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario.

# Comentar las instrucciones anteriores para ejecutar las siguientes

# numeroIngresado = input("Ingrese el número al cual desea contar sus dígitos: ")
# contador = 0

# while contador < len(numeroIngresado):
#     contador +=1

# print(f"El número de dígitos ingresados es {contador}")


print("actividad3")
#Escribe el código que solicite números al usuario hasta que éste ingrese -1.
#Cuando se ingrese -1, el programa debe imprimir el promedio de todos los números ingresados hasta ese momento (sin contar con el -1).

# Comentar las instrucciones anteriores para ejecutar las siguientes

sumatoria = 0
contadorNumerosIngresados = 0
numeroIngresado = int(input("Ingrese un número: "))

while numeroIngresado != -1:
    sumatoria += numeroIngresado
    contadorNumerosIngresados += 1
    numeroIngresado = int(input("Ingrese un número: "))
    

print("El promedio de los números ingresados por el usuario es: " + f"{sumatoria/contadorNumerosIngresados}")
