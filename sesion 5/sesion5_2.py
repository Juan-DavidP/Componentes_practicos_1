# Diseñar 3 opciones:
#
#   1. Leer un número de 4 dígitos, mostrar el dígito mayor e 
#      informar si es par o impar.
#   2. Leer dos números de 3 dígitos cada uno, formar un tercer número 
#      con el mayor del primero y el menor del segundo.
#   3. Leer un número de 3 dígitos y formar el mayor número posible 
#      con sus cifras.

# 1.
# numeroIngresado =input("Ingrese un número de 4 dígitos: ")
# if len(numeroIngresado) == 4:
#     digitoMayor = 0
#     for i in numeroIngresado:
#         i = int(i)
#         if i > digitoMayor:
#           digitoMayor = i
#     if digitoMayor % 2 == 0:
#         print(f"El último dígito es el número {digitoMayor} y es par")
#     else:
#         print(f"El último dígito es el número {digitoMayor} y es impar")
# else:
#     print("El número ingresado no tiene 4 dígitos")

# 2.
# numero1 = input("Ingrese un número de 3 dígitos: ")
# numero2 = input("Ingrese nuevamente un número de 3 dígitos: ")

# if len(numero1) and len(numero2) == 3:
#     digitoMayor = 0
#     digitoMenor = 999
#     for i in numero1:
#         i = int(i)
#         if i > digitoMayor:
#             digitoMayor = i
#     for j in numero2:
#         j = int(j)            
#         if j < digitoMenor:
#             digitoMenor = j
#     print(str(i) + str(j))
# else:
#     print("Uno o ambos números no cumplen con el largo permitido de 3 dígitos")


#3.
# numeroIngresado = input("Ingrese por favor un número de 3 dígitos: ")
# if len(numeroIngresado) == 3:
#     numeroMayor = ""
#     for i in range(9, 0, -1):  # Comienza desde 9 (el dígito más grande posible) y disminuye hasta 0
#         for j in numeroIngresado:
#             if i == int(j):
#                 numeroMayor += j
#             if len(numeroMayor) == len(numeroIngresado):
#                 break
#     print("El número ordenado de mayor a menor es: ", numeroMayor)
# else:
#     print("El número ingresado no tiene 3 dígitos")


# numeroIngresado = input("Ingrese por favor un número de 3 dígitos: ")
# if len(numeroIngresado) == 3:
#     numeroMayor = "".join(sorted(numeroIngresado, reverse=True))
#     print("El número ordenado de mayor a menor es: ", numeroMayor)
# else:
#     print("El número ingresado no tiene 3 dígitos")

# Luego crea un menú con las tres opciones.

# Menu de opciones:
# print("1. Leer numero de 4 digitos y mostrar digito mayor")
# print("2. Leer numero de 3 digitos y combinar sus valores")
# print("3. Leer numero de 3 digitos y formar el numero mayor de sus valores")

# Lee la opcion deseada
  # Ejecuta el bloque de codigo de acuerdo a la opcion elegida

# Observe que el programa finaliza una vez se ejecute la opcion deseada
    
print("""¿Qué desea hacer?
      1. Leer un número de 4 dígitos, mostrar el dígito mayor e informar si es par o impar.
      2. Leer dos números de 3 dígitos cada uno, formar un tercer número con el mayor del primero y el menor del segundo
      3. Leer un número de 3 dígitos y formar el mayor número posible con sus cifras.""")

opcion = int(input("Ingrese la opcion deseada:"))

if opcion == 1:
    numeroIngresado =input("Ingrese un número de 4 dígitos: ")
    if len(numeroIngresado) == 4:
        digitoMayor = 0
        for i in numeroIngresado:
            i = int(i)
            if i > digitoMayor:
                digitoMayor = i
        if digitoMayor % 2 == 0:
            print(f"El último dígito es el número {digitoMayor} y es par")
        else:
            print(f"El último dígito es el número {digitoMayor} y es impar")
    else:
        print("El número ingresado no tiene 4 dígitos")

elif opcion == 2:
    numero1 = input("Ingrese un número de 3 dígitos: ")
    numero2 = input("Ingrese nuevamente un número de 3 dígitos: ")
    if len(numero1) and len(numero2) == 3:
        digitoMayor = 0
        digitoMenor = 999
        for i in numero1:
            i = int(i)
            if i > digitoMayor:
                digitoMayor = i
        for j in numero2:
            j = int(j)            
            if j < digitoMenor:
                digitoMenor = j
        print(str(i) + str(j))
    else:
        print("Uno o ambos números no cumplen con el largo permitido de 3 dígitos")
elif opcion == 3:
    numeroIngresado = input("Ingrese por favor un número de 3 dígitos: ")
    if len(numeroIngresado) == 3:
        numeroMayor = ""
        for i in range(9, 0, -1):  # Comienza desde 9 (el dígito más grande posible) y disminuye hasta 0
            for j in numeroIngresado:
             if i == int(j):
                numeroMayor += j
            if len(numeroMayor) == len(numeroIngresado):
                break
    print("El número ordenado de mayor a menor es: ", numeroMayor)
else:
    print("El número ingresado no tiene 3 dígitos")