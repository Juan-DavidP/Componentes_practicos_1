# """

# Para

# El ciclo Para o For en Python nos ayuda a ejecutar dentro dentro de un rango determinado de iteraciones. 


# En la semana uno exploramos el tipo de dato string (una cadena de caracteres). 
# Los caracteres dentro de este tipo de dato en Python puede ser recorridos con la posicion en la que se encuentran dentro de la cadena. Veamos un ejemplo:
# """


# palabra = "Prueba"
# longitud = len(palabra)

# print("Primer ciclo")
# for i in range(longitud):
#     print(palabra[i])

# print("Segundo ciclo")
# for x in "Prueba":
#     print(x)


# Actividad 1
# print("Actividad 1")
# Vamos a realizar un algoritmo que nos calcule la serie de Fibonacci.
# La serie o secuencia de Fibonacci comienza con los números 0 y 1 y 1, y a partir de allí es posible calcular el siguiente valor como la suma de los dos valores anteriores. 
# Por ejemplo, 1+1=2, 1+2=3, 2+3=5, etc. Así, los primeros números de la secuencia son: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Creemos un programa que a partir de un número N ingresado, imprima los primeros N números de la serie de Fibonacci.

# numeroIngresado = int(input("Ingrese el número hasta el que desea generar la serie de Fibonacci: "))
# num_uno = 0
# num_dos = 1
# sumatoria = 0

# for i in range(numeroIngresado):
#     print(sumatoria)
#     sumatoria = num_uno + num_dos
#     num_uno = num_dos
#     num_dos = sumatoria

# Actividad 2
# print("actividad2")
#Escribe el código usando break que reciba una palabra e imprima el número de letras que tiene y las letras hasta que, o bien termine la palabra o encuentre la letra a. .

# Para ejecutar esta actividad, poner en comentario el resto del codigo fuente.

# palabra = input("Ingrese la palabra a la cual desea contar sus letras: ")
# # tamañoPalabra = len(palabra)
# # print(tamañoPalabra)
# print((f"El tamaño de la palabra es de {len(palabra)} letras"))
# for i in palabra:
#     if i == "a":
#         break
#     print(i)



# Actividad 3
# print("Actividad 3")  
#Escribe un algoritmo que lea 10 números e imprima cuantos son positivos, cuantos negativos y cuantos neutros(0).

# Para ejecutar esta actividad, poner en comentario el resto del codigo fuente.

# contadorPositivos = 0
# contadorNegativos = 0
# contadorNeutros = 0
# for i in range(10):
#     numeroIngresado = int(input("Ingrese el número que desea determinar si es positivo, negativo o neutro : "))
#     if numeroIngresado > 0:
#         contadorPositivos += 1
#     elif numeroIngresado == 0:
#         contadorNeutros +=1
#     else:
#         contadorNegativos += 1
# print(f"La cantidad de números positivos son: {contadorPositivos}, La cantidad números negativos son: {contadorNegativos} y la cantidad de números neutros son: {contadorNeutros}")


# Actividad 4
# print("actividad4")
#Usando tanto while como for, escribe el codigo que pida números al usuario hasta que este ingrese -1 y que retorne el factorial de cada número ingresado usando un ciclo Para (For).

# Para ejecutar esta actividad, poner en comentario el resto del codigo fuente.

factorial = 1
contador = 0
numeroIngresado = int(input("Ingrese un número para calcular su factorial: "))
while numeroIngresado != -1:
    for i in range(1, numeroIngresado + 1):
        factorial = i * factorial
    print(factorial)
    print("Para salir escriba -1")
    factorial = 1
    numeroIngresado = int(input("Ingrese un número para calcular su factorial: "))