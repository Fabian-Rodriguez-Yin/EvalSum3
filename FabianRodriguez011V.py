from csv import *
from random import *
from os import *

saco1 = 0
saco2 = 0
saco3 = 0

sectores = ["san bernardo", "calera de tango", "buin"]
pedidos = [ ]

nroped = randint(1,1000)

def menu():
    print("Bienvenido a Catpremiun, el mejor lugar para comprar comida para tu bebé")
    print("Elige una opción para saber en que podemos ayudarte!")
    print("1- Registrar pedido")
    print("2- Listar todos los pedidos")
    print("3- Imprimir hoja de ruta")
    print("4- Salir del programa")

def guardar_pedidos_csv(pedidos):
    archivo_csv = "pedidos.csv"
    with open(archivo_csv,"w")as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nroped, nombre, direccion, comuna, saco1, saco2, saco3])
        escritor.writerows(pedidos)

while True:
    menu()
    try:
        opcion = int(input("Ingrese la opción que desea usar: "))
    except ValueError:
        print("Ingrese un número")
        continue
    if opcion == 1:
        nombre = input("Ingrese su nombre y apellido: ")
        direccion = input("Ingrese su dirección: ")
        while True:
            comuna = input("Ingrese su comuna entre: San Bernardo, Calera de Tango o Buin: ").lower()
            if comuna in sectores:
                print("Se ha seleccionado su comuna.")
                break
            else:
                print("Por favor seleccione una de las comunas mencionadas.")
        while True:
            print("Elija el tipo de saco de quiere comprar.")
            print("1- 5kg.")
            print("2- 10kg.")
            print("3- 20kg.")
            print("4- Salir.")
            numpedido = int(input("Ingrese el tipo de saco: "))
            if numpedido == 1:
                cant1 = int(input("Ingrese la cantidad de sacos de 5kg: "))
                saco1 = saco1 + cant1
            elif numpedido == 2:
                cant2 = int(input("Ingrese la cantidad de sacos de 10kg: "))
                saco2 = saco2 + cant2
            elif numpedido == 3:
                cant3 = int(input("Ingrese la cantidad de sacos de 20kg: "))
                saco3 = saco3 + cant3
            elif numpedido == 4:
                pedidos.append ({ "Nro.Ped: " : nroped, "Nombre" : nombre, "Dirección" : direccion, "Sector" : comuna, "Saco 5kg" : saco1, "Saco 10kg" : saco2, "Saco 20kg" : saco3})
                print("")
                cant1 = 0
                cant2 = 0
                cant3 = 0
                nroped = nroped + 1
                break
            else:
                print("Ingrese un número entre 1 y 4.")
                continue
    elif opcion == 2:
                print(pedidos)
    elif opcion == 3:
        print("imprimir_pedidos_csv") #No logré hacer que el write o el open funcionancen...
    elif opcion == 4:
        guardar_pedidos_csv
        break
    else:
        print("Opcion incorrecta, elija un numero del 1 al 4.")   
        