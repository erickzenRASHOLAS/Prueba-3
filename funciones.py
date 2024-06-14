trabajadores=[]
cargos=("CEO", "DESARROLADOR", "ANALISTA")#0:ceo 1:desarrollador 2:analista
def resgitrar_trabajador():
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

def listar_trabajadores():
    if len(trabajadores)==0:
        print("error!!!lista vacia, registre un trabajador en la opción 1 !!!")
    else:
        print("\tLISTA DE TRABAJADORES")
        for t in trabajadores:
            print (f"NOMBRE: {t[0]}\n CARGO: {t[1]}\n BRUTO: {t[2]}\n SALUD: {t[3]}\n AFP: {t[4]}\n LIQUIDO {t[5]}\n" )
            
def exportar_archivo_txt():
    pass
def salir():
    print ("GRACIAS HASTA LUEGO!!!")
    exit()

#puedes agregar mas funciones, que les ayuden