import numpy as np
import os
if os.name == "nt": os.system("cls")

def menu():
    print("\n")
    print("1)  Ver disponibilidad de lotes")
    print("2)  Seleccionar un lote")
    print("3)  Ver detalles del lote seleccionado")
    print("4)  Ver clientes")
    print("5)  Salir")

def crear_matrices():
    global lotes
    global clientes
    global detalles_lotes
    lotes = [[" "] * 5 for i in range(4)]
    clientes = []
    detalles_lotes = [["Numero: 6352 Tamaño: 7369m² Precio: $60.312.248","Numero: 2749 Tamaño: 8581m² Precio: $59.076.189","Numero: 1508 Tamaño: 7909m² Precio: $45.049.412","Numero: 3865 Tamaño: 6971m² Precio: $46.277.485","Numero: 3287 Tamaño: 5630m² Precio: $58.312.619"],
                ["Numero: 8975 Tamaño: 8834m² Precio: $48.420.607","Numero: 8517 Tamaño: 7479m² Precio: $51.057.755","Numero: 6706 Tamaño: 5569m² Precio: $64.386.470","Numero: 4197 Tamaño: 8906m² Precio: $51.277.564","Numero: 7843 Tamaño: 8050m² Precio: $57.981.223"],
                ["Numero: 9719 Tamaño: 8206m² Precio: $54.378.188","Numero: 9035 Tamaño: 6892m² Precio: $61.947.024","Numero: 6368 Tamaño: 8422m² Precio: $61.456.181","Numero: 5893 Tamaño: 5407m² Precio: $63.222.889","Numero: 6342 Tamaño: 5082m² Precio: $51.510.035"],
                ["Numero: 4253 Tamaño: 7397m² Precio: $53.307.284","Numero: 3401 Tamaño: 7730m² Precio: $61.934.909","Numero: 3424 Tamaño: 8838m² Precio: $63.995.743","Numero: 1532 Tamaño: 5467m² Precio: $62.405.284","Numero: 2915 Tamaño: 5753m² Precio: $47.117.399"]]

def mostrar_lotes():
    lotes_disponibles = np.array(lotes)
    return print("---------Lotes---------"), print(lotes_disponibles), input("")

def comprar_lote():
    ingresar_lote = True
    global fila,columna
    while ingresar_lote == True:
        try:
            fila = int(input("Ingrese la fila del lote que desea:  "))
            columna = int(input("Ingrese la columna del lote que desea:  "))
            if fila >= 0 and fila <= 3 and columna >= 0 and columna <= 4:
                if lotes[fila][columna] == " ":
                    lotes[fila][columna] = "X"
                    guardar_cliente()
                    ingresar_lote = False
                else:
                    print("Lote no disponible, porfavor elija otro.\n")
            else:
                print("Numeros ingresados fuera de rango, porfavor vuelva a ingresarlos.\n")
        except:
            print("Error, Vuelva a ingresar los numeros.\n")

def guardar_cliente():
    datos = []
    guardardatos = True
    while guardardatos == True:
        try:
            rut_cliente = int(input("Ingrese su RUT (Sin puntos ni guion):  "))
            nom_cliente = input("Ingrese su nombre completo:  ")
            tel_cliente = int(input("Ingrese su telefono:  "))
            email_cliente = input("Ingrese su email:  ")
            guardardatos = False
        except:
            print("Error, vuelva a ingresar los datos.\n")
    datos = [[rut_cliente,nom_cliente,tel_cliente,email_cliente]]
    clientes.extend(datos)

def mostrar_detalle_lote():
    try:
        print("--------Detalles del lote--------")
        print(detalles_lotes[fila][columna])
        input("")
    except NameError:
        print("No se ha seleccionado ningun lote")
        input("")

def mostrar_clientes():
    numcliente = 1
    print("--------Clientes--------")
    if clientes == []:
        print("No hay clientes")
    else:
        for f in range(len(clientes)):
            print(f"   Cliente nro {numcliente}")
            for c in range(len(clientes[f])):
                print(clientes[f][c])
            numcliente += 1
            print("\n")
    input("")

def finalizar_programa():
    global menus
    print("Usted a salido de la aplicacion, Adios.")
    menus = False


crear_matrices()
menus = True
while menus == True:

    menu()
    try:
        op = int(input("Ingrese una opcion:  "))
        print("\n")
    except:
        print("\nError, vuelva a ingresar una opcion.")
        continue

    if op == 1:
        mostrar_lotes()
    
    elif op == 2:
        comprar_lote()
    
    elif op == 3:
        mostrar_detalle_lote()
    
    elif op == 4:
        mostrar_clientes()

    elif op == 5:
        finalizar_programa()

    else:
        print("Opcion ingresada incorrecta")