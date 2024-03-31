"""
Cada ejemplo y actividad será definida como un bloque independiente.
Si-Sino-Finsi
Recuerda que los condicionales múltiples y anidados nos permiten evaluar múltiples casos. 
El condicional Si-Sino-Si-Finsi tiene la siguiente estructura:

    Si (condición) Entonces
        instrucción(es)
    Sino Si
        instrucción(es)
    Fin Si

En Python, esto se escribe un poco diferente y la estructura general depende de las tabulaciónes. 
Por ejemplo:
"""

# x = int(input("Por favor ingresa un número: "))
# if x < 0:
#     print('El número es Negativo')
# elif x > 0:
#     print('El número es positivo')
# elif x == 0:
#     print('El número es cero')


# Actividad 1
# Escribe el código que imprima un comando dada la luz del semáforo
    # print("Actividad 1")
    #Verde = Siga
    #Amarillo = Precaución
    #Rojo = Pare

# luz_semaforo = input("Ingrese el color de la luz que tiene el semaforo: ").title()

# if luz_semaforo == "Verde":
#     print("Siga")
# elif luz_semaforo == "Amarillo":
#     print("Precaución")
# elif luz_semaforo == "Rojo":
#     print("Pare")
# else:
#     print("El color ingresado no es valido.")


# Para ejecutar cada actividad, debes poner en comentarios todas las lineas de los bloques anteriores o si lo prefieres
# crear otro programa python


# Actividad 2
# Escribe el código que basado en la actividad 1 y una variable que nos indica si hay peaton o no (hayPeaton), imprima:
    # print("Actividad 2")
    #Verde -------- Si hay peaton - Pare, Sino - Siga
    #Amarillo ----------- Si hay peaton - Pare, Sino - Precaución
    #Rojo = Pare

# luz_semaforo = input("Ingrese el color de la luz que tiene el semaforo: ").title()
# peaton = input("Se encuentra un peaton en la via S para si y N para no: ").upper()

# if luz_semaforo == "Verde":
#     if peaton == "S":
#         print("Pare")
#     else:
#         print("Siga")
# elif luz_semaforo == "Amarillo":
#     if peaton == "S":
#         print("Pare")
#     else:
#         print("Precaución")
# elif luz_semaforo == "Rojo":
#     print("Pare")
# else:
#     print("El color ingresado no es valido.")

# Para ejecutar cada actividad, debes poner en comentarios todas las lineas de los bloques anteriores o si lo prefieres
# crear otro programa python




# Actividad 3
# Escribe el código para dos numeros a y b, el usuario va a seleccionar una opcion: 
    # print("Actividad 3")
    #1 para sumar, 2 para multiplicar, 3 para restar (a-b) y 4 para dividir (a/b) y 
    #retornar el resultado de la operación indicada.

num1 = int (input("Ingrese el primer número: "))
num2 = int (input("Ingrese el segundo número: "))
operacion = int(input("Ingrese el número de la operación que desea realizar: \n 1 para sumar \n 2 para multiplicar \n 3 para restar \n 4 para dividir \n"))

if operacion == 1:
    print("El resultado de la suma es: " + str(num1 + num2))
elif operacion == 2:
    print("El resultado de la multiplicación es: " + str(num1 * num2))
elif operacion == 3:
    print("El resultado de la resta es: " + str(num1 - num2))
elif operacion == 4:
    print("El resultado de la división es: " + str(num1 / num2))
else:
    print("Se ha ingresado una operación invalida.")

# Para ejecutar cada actividad, debes poner en comentarios todas las lineas de los bloques anteriores o si lo prefieres
# crear otro programa python