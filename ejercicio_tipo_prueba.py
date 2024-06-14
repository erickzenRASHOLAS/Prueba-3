import os,time
from funciones import *



while True:
    os.system('cls')
    print("MENU TRABAJODERS")
    print("1. REGISTRAR TRABAJADOR")
    print("2. LISTAR TODOS LOS TRABAJADORES")
    print("3. IMPRIMIR PLANILLA DE SUELDOS")
    print("4.SALIR")
    opc=int(input("POR FAVOR ELIJA UNA OPCION: "))
    os.system('cls')

    if opc==1:
        resgitrar_trabajador()


    elif opc==2:
        listar_trabajadores()
    elif opc==3:
        exportar_archivo_txt()
    else:
        salir ()
    time.sleep(3)
