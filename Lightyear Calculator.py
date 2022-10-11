
#Biblioteca y funciones math
import math
math.pow
math.sqrt


print("\n \n Bienvenido a LightYear Calculator.py! \n \n")

#Variables (k = constante k, r = radios, l = lunas, m = masas, g = constante gravitacional)
k = int(1)
r = 0
r_2 = 0
l = 0
m = 0
gk = float(6.67430*(pow(10,-11)))


#Listas de planetas, radios y lunas
planetas = ["mercurio","venus","tierra","marte","jupiter","saturno","urano","neptuno"]
radios = [0.39,0.72,1.00,1.52,5.20,9.54,19.19,30.06] #Esta lista es usada para el calculo de periodos (radios en proporcion a la tierra)
radios_2 = [2440,6052,6371,3390,69911,58232,25362,24622] #Esta lista es usada para el calculo de fuerzas de gravedades (radios exactos)
lunas = [0,0,1,2,79,82,27,14]
masas = [3.302*(pow(10,23)),4.869*(pow(10,24)),5.9710*(pow(10,24)),6.4169*(pow(10,23))
,1.899*(pow(10,27)),5.688*(pow(10,26)),8.686*(pow(10,25)),1.024*(pow(10,26))]

#Lista anidada
matriz = [planetas,radios_2,masas]


#Funciones: Calculo del periodo, Calculo de el periodo en meses, Calculo del periodo en dias
#,Calculo de gravedades, Impresiones de textos finales, Asignacion de posicion de planetas, Comparacion de planetas

def calc_periodo(k,r):
    res = math.sqrt((k)*(pow(r,3)))
    return res

def calcp_meses(k,r):
    a = calc_periodo(k,r)
    meses = (a)*(12)
    return meses

def calcp_dias(k,r):
    b = calcp_meses(k,r)
    dias = (b)*(30.44)
    return dias

def calc_gravedad(gk,m,r_2):
    g = gk*(m/pow(r_2*(pow(10,6)),2))
    return g 
    

def imprime_fin1(p):
    print( "El periodo orbital de",p,"aproximado en dar la vuelta al sol es de:")

def imprime_fin4(l):
    print("\nEl planeta",p,"cuenta con un numero de:",l,"lunas confirmadas")


def posicion(planetas):
    return planetas.index(p)+1

def informacion(matriz):
    for i in matriz:
        for j in matriz[i]:
            if p in matriz[0]:
                return matriz[i[j]]


#Variable Menu
MenuPrincipal = int(input("Menu Principal: \n \n ¿Que desea Calcular? \n \n 1: Periodo orbital \n 2: Posicion \n 3: Gravedad \n 4: Lunas \n 5: Comparar planetas \n\n i: Presione '6' para ver informacion general del planeta \n\n 0: Salir \n\n*Escriba el numero de la opcion que desee:" ))


while MenuPrincipal !=0:

#Input variable str(p) = planeta
    p = str(input("Escriba el planeta del sistema solar de su preferencia: "))


#Asignacion de variables dependiendo del planeta            
    for i in range(len(planetas)):
        if p == planetas[i]:
            r = radios[i]
            r_2 = radios_2[i]
            l = lunas[i]
            m = masas[i]

#Condiciones de Menu
    if MenuPrincipal == 1: 
        format = int(input("\nComo desea obtener el resultado?: \n 1: Años \n 2: Meses \n 3: Dias \nEscriba el numero de la opcion que desee:"))
        if format == 1:
            print("\n--------")
            imprime_fin1(p)
            print(calc_periodo(k,r),"años de la Tierra")
            print("--------")
        elif format == 2:
            print("--------")
            imprime_fin1(p)
            print(calcp_meses(k,r),"meses de la Tierra")
            print("--------")
        elif format == 3:
            print("--------")
            imprime_fin1(p)
            print(calcp_dias(k,r),"dias de la Tierra")
            print("--------")


    elif MenuPrincipal == 2:
         if p in planetas:
            print("--------")
            print("\n El planeta",p, "esta en la posicion", posicion(planetas),"del sistema solar")
            print("--------")

    elif MenuPrincipal == 3:
        print("--------")
        print ("\nLa gravedad de la superficie del planeta",p,"es igual a:", "\n",calc_gravedad(gk,m,r_2))
        print("--------")

    elif MenuPrincipal == 4:
        print("--------")
        (imprime_fin4(l))
        print("--------")

    elif MenuPrincipal == 6:
        for i in range(len(planetas)):
            if p == planetas[i]:
                r_2 = radios_2[i]
                m = masas[i]
                print ("\n\n--> Planeta:",planetas[i])
                print("--------")
                print ("--> Radio:",radios_2[i])
                print("--------")
                print ("--> Masa:",masas[i],"\n\n")



    else: print("\nPor favor ingrese una opcion valida")

#La Opcion (5) aun no esta habilitada :(

#Repeticion de ciclo
    MenuPrincipal = int(input("\nMenu Principal: \n \n ¿Que desea Calcular? \n \n 1: Periodo orbital \n 2: Posicion \n 3: Gravedad \n 4: Lunas \n 5: Comparar planetas \n\n i: Presione '6' para ver informacion general del planeta \n\n 0: Salir \n\nEscriba el numero de la opcion que desee:"))
        
