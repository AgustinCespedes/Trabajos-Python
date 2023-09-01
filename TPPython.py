# TP generar un rango con una funcion.
range(1, 10, 2)

def rango(inicio, fin, intervalo):
    resultado = []
    while inicio < fin:
        resultado.append(inicio)
        inicio = inicio + intervalo
    return resultado

lista = rango(5, 16, 3)
print(lista)


=========================================================

# Lab. 2: Comprobar ingreso.
while edad.isdecimal() == False:
    print("Debe ingresar numeros")
    edad = input("Ingrese su edad")

edad = int(edad)

if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")



while True:
    edad = input("Ingrese su edad: ")

    if edad.isdecimal() == True:
        print("Ingreso correcto")
        edad = int(edad)
        if edad >= 18:
            print("es mayor")
            break
        else:
            print("es menor")
            break
    else:
        print("No es correcto")


=========================================================

# Estrellas
def mostrar_estrellas(cantidad):
    for i in range(1, numero_estrellas + 1):
        print("*" * i)

numero_estrellas = int(input("Coloque la cantidad de estrellas: "))

mostrar_estrellas(numero_estrellas)

# Clase numero 6

import time, random

print(time.asctime())
print("Esperando....")
time.sleep(5)
print("Clase numero 6")


print(random.randint(25, 50))


=========================================================

# Estrellas
def mostrar_estrellas(cantidad):
    for i in range(1, numero_estrellas + 1):
        print("*" * i)

numero_estrellas = int(input("Coloque la cantidad de estrellas: "))

mostrar_estrellas(numero_estrellas)

# Clase numero 6

import time, random

print(time.asctime())
print("Esperando....")
time.sleep(5)
print("Clase numero 6")


print(random.randint(25, 50))


=========================================================


# Ejercicio 1 contador.
import time

var = 1
while var <= 10:
    print(var)
    time.sleep(1)
    var = var + 1

# TP. 2 dado
import random

while True:
    print("1 -> Tirar dado")
    print("2 -> Salir")
    opc = input("Ingrese una opcion: ")
    if opc == "1":
        dado = random.randint(1, 6)
        print("El dado muestra el numero", dado)
    elif opc == "2":
        print("Fin del programa")
        break
    else:
        print("Opcion incorrecta")


=========================================================


# Ejercicio 1
matriz = [[3.3, 6.1, 4.0], 
          [4.9, 5.7, 6.4]]
    
fila = int(input("Ingrese el numero de Fila: "))
columna = int(input("Ingrese el numero de columna: "))
if (fila == 0 or fila == 1) and (columna >= 0 and columna <= 2):
    print(matriz[fila][columna])
else:
    print("Error en el ingreso de valores")


=========================================================


# TP Cuenta regresiva
import time
import sys

argumentos = sys.argv

ayuda = """
Ayuda
Esta es la ayuda de regresiva.py.
Este programa permite hacer una cuenta 
regresiva desde el numero que vos pases por
argumento hasta 0

Ejemplo

/regresiva.py 3
>>> 3
>>> 2
>>> 1
"""

try:
    tiempo = int(argumentos[1])
except IndexError:
    tiempo = 10
except ValueError:
    if argumentos[1].lower() == "-h" or argumentos[1].lower() == "-help":
        print(ayuda)
    else:
        print("Hay un error. Solo se permiten numeros")
    sys.exit()


for n in range(10,0,-1):
    print(n)
    time.sleep(1)


=========================================================


# Ejercicio 2:

import sqlite3
import os
from tabulate import tabulate
import requests

##############################


def input_numerico(frase):
    valor = input(frase)
    while True:
        try:
            valor = int(valor)
            break
        except ValueError:
            try:
                valor = float(valor)
                break
            except ValueError:
                print("Error. ¡El ingreso no es numerico!")
        valor = input("Nuevamente. " + frase)
    return valor


def guardar(i, n, p):
    try:
        conn = sqlite3.connect("productos.sqlite")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE productos (id INT, nombre TEXT, precio INT)")
        cursor.execute("INSERT INTO productos VALUES(?,?,?)", (i, n, p))
        conn.commit()
        conn.close()
    except sqlite3.OperationalError:
        conn = sqlite3.connect("productos.sqlite")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos VALUES(?,?,?)", (i, n, p))
        conn.commit()
        conn.close()
    print("¡Producto agregado!")


def ver():
    r = requests.get(
        "https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    data = r.json()
    dolar = float(data[0]["casa"]["venta"].replace(",", "."))
    try:
        conn = sqlite3.connect("productos.sqlite")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        datos = cursor.fetchall()
        # datos=[(1,"pc",500),(2,"tv",100)]
        aux = []
        for n in datos:
            actual = list(n)
            actual[2] = actual[2] * dolar
            aux.append(actual)
        return aux
    except sqlite3.OperationalError:
        pass


##############################

if os.name == "nt":
    borrar = "cls"
else:
    borrar = "clear"


os.system(borrar)


while True:
    print("Menú")
    print("""
        1 - Agregar productos
        2 - Ver productos
        3 - Salir
          """)
    opcion = input(">>> ")
    if opcion == "1":
        nombre = input("Ingrese nombre del producto: ")
        identificador = input_numerico("Id del producto: ")
        precio = input_numerico("Ingrese precio del producto: ")
        guardar(identificador, nombre, precio)
    elif opcion == "2":
        r = ver()
        if r:
            print(tabulate(r, ["ID", "NOMBRE", "PRECIO"], tablefmt="pretty"))
        else:
            print("¡Tabla vacia!")
    elif opcion == "3":
        print("¡Gracias por usar nuestro programa!")
        break
    else:
        print("¡Error de opción!")
    input("Toque ENTER para continuar...")
    os.system(borrar)



import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="",
    db="alumnos"
)

cursor = conn.cursor()

cursor.execute("INSERT INTO personas VALUES (%s,%s)", ("Juan", 32))

cursor.execute("SELECT * FROM personas")
data = cursor.fetchall()

conn.commint()
conn.close()


=========================================================


import time

#######################################

def verificar(texto):
    while texto == "":
        print("Error")
        texto = input("Ingrese nuevamente: ")
    return texto


def guardar(nombre, evento):
    fecha = time.asctime()
    f = open("registro.txt", "a")
    f.write(f"{nombre} - {fecha} - {evento} \n")
    f.close()
    print("¡Registro salvado!")


def ultimos():
    f = open("registro.txt", "r")
    lista = f.readlines()
    f.close()
    if len(lista) >= 5:
        for n in lista[-5:]:
            print(n.strip())
    else:
        for n in lista:
            print(n.strip())

#######################


while True:
    print("Menú:")
    print(#""""""
          1 - Ingreso al edificio
          2 - Egreso del edificio
          3 - Ver los últimos registros 
          4 - Salir del programa
          )
    opcion = input(">>> ")
    if opcion == "1":
        nombre = input("Ingrese nombre de la persona: ")
        nombre = verificar(nombre)
        guardar(nombre, "Ingreso")
    elif opcion == "2":
        nombre = input("Ingrese nombre de la persona: ")
        nombre = verificar(nombre)
        guardar(nombre, "Egreso")
    elif opcion == "3":
        print("Los ultimos registros son: ")
        ultimos()
    elif opcion == "4":
        print("Gracias por usar nuestro programa")
        break
    else:
        print("Error de opción")



=========================================================


# Ejercicios = Paises

paises = {
    "ar": "Argentina",
    "es": "España",
    "us": "Estados Unidos",
    "fr": "Francia"
}

while True:
    cod = input("Ingrese cod pais: ")
    try:
        print("El cod ingresado corresponde a:", paises[cod])
    except KeyError:
        if cod == "salir":
            print("Programa terminado")
            break
        else:
            print("Error de codigo")
