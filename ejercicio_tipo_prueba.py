import os,time

trabajadores=[]
cargos=("CEO", "DESARROLADOR", "ANALISTA")#0:ceo 1:desarrollador 2:analista

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
        print("Registro trabajadores")
        nombre_apellido=input("ingrese nombre y apellido") 
        cargo=int(input("Ingrese cargo (1.CEO 2.DESARROLLADOR 3. ANALISTA): "))
        sueldo_bruto=int(input("INGRESE SUELDO BRUTO: ")) 
        dcto_salud=int(sueldo_bruto-(sueldo_bruto*0.93) )
        dcto_AFP=int(sueldo_bruto-(sueldo_bruto*0.93) )
        sueldo_liquido=sueldo_bruto*0.81 
        traba=[nombre_apellido,cargos[cargo-1],sueldo_bruto,dcto_salud,dcto_AFP,sueldo_liquido]
        trabajadores.append(traba)
        print("TRABAJADOR REGISTRADO CON ÉXITO") 


    elif opc==2:
        pass
    elif opc==3:
        pass
    else:
        print ("GRACIAS HASTA LUEGO!!!")
        break
    time.sleep(3)
