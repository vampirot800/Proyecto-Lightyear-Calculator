

"""
Proyecto Lightyear-Calculator Python.

El programa funciona como una calculadora con interfaz de menu
en la cual se le proporciona al usuario con diversas opciones 
acerca de los planetas del sistema solar (periodos orbitales,
gravedad, etc..)
El programa tomara la opcion que el usuario seleccione y los 
planetas ingresados por el usuario y devolvera la informacion
solicitada.

"""

#Biblioteca y funciones math
import math
math.pow
math.sqrt


print("\n \n Bienvenido a LightYear Calculator.py! \n \n")


""" 
========================= Variables ==============================
"""
#Variables constates:

#Constante gravitacional Gauss
GAUSS = int(1)
#Constante gravitacional universal
GRAV = float(6.67430*(pow(10,-11)))

radio_prop = 0
radio_exacto = 0
lunas = 0
masas = 0

interfaz_menu = (
"""

===================== Menu Principal:=========================

¿Que desea Calcular?

1: Periodo orbital 
2: Posicion 
3: Gravedad 
4: Lunas 
5: Comparar planetas

i: Presione '6' para ver informacion general del planeta 

0: Salir

==============================================================
*Escriba el numero de la opcion que desee:
"""
)

opciones_periodo = (
"""
Como desea obtener el resultado?:

1: Años 
2: Meses 
3: Dias 

==============================================================
*Escriba el numero de la opcion que desee:""")

""" 
========================= Listas ==============================
"""

#Listas de planetas, radios y lunas
list_planetas = ["mercurio","venus","tierra","marte","jupiter",
"saturno","urano","neptuno"]

#Esta lista es usada para el calculo de periodos
#(radios en proporcion a la tierra)
list_radios_prop = [0.39,0.72,1.00,1.52,5.20,9.54,19.19,30.06] 

#Esta lista es usada para el calculo de fuerzas de gravedades 
#(radios exactos)
list_radios_ex = [2440,6052,6371,3390,69911,58232,25362,24622] 

list_lunas = [0,0,1,2,79,82,27,14]

list_masas = [3.302*(pow(10,23)),4.869*(pow(10,24))
,5.9710*(pow(10,24)),6.4169*(pow(10,23)),1.899*(pow(10,27))
,5.688*(pow(10,26)),8.686*(pow(10,25)),1.024*(pow(10,26))]

#Lista anidada
matriz = [list_planetas,list_radios_ex,list_masas]



""" 
========================= Funciones ==============================
"""


#Funciones: Calculo del periodo en años/meses/dias 
#,Calculo de gravedades, Impresiones de textos finales, 
#Asignacion de posicion de planetas, Comparacion de planetas

def calc_periodo(GAUSS,radio_prop):
    res = math.sqrt((GAUSS)*(pow(radio_prop,3)))
    return res

def calcp_meses(GAUSS,radio_prop):
    a = calc_periodo(GAUSS,radio_prop)
    meses = (a)*(12)
    return meses

def calcp_dias(GAUSS,radio_prop):
    b = calcp_meses(GAUSS,radio_prop)
    dias = (b)*(30.44)
    return dias

def calc_gravedad(GRAV,m,radio_exacto):
    g = GRAV*(m/pow(radio_exacto*(pow(10,6)),2))
    return g 
    

def imprime_fin1(p):
    print( "El periodo orbital de",p,
    "aproximado en dar la vuelta al sol es de:")

def imprime_fin4(lunas):
    print("El planeta",p,"cuenta con un numero de:"
    ,lunas,"lunas confirmadas")


def posicion(list_planetas):
    return list_planetas.index(p)+1

def informacion(matriz):
    for i in matriz:
        for j in matriz[i]:
            if p in matriz[0]:
                return matriz[i[j]]


""" 
=============== Parte Principal del programa =====================
"""


#Variable Menu
MenuPrincipal = int(input(interfaz_menu))


while MenuPrincipal !=0:

#Input variable str(p) = planeta
    p = str(input("Escriba el planeta del sistema solar de su preferencia: "))


#Asignacion de variables dependiendo del planeta         
    for i in range(len(list_planetas)):
        if p == list_planetas[i]:
            radio_prop = list_radios_prop[i]
            radio_exacto = list_radios_ex[i]
            lunas = list_lunas[i]
            masas = list_masas[i]

#Condiciones de Menu
    if MenuPrincipal == 1: 
        format = int(input(opciones_periodo))
        if format == 1:
            print("\n--------")
            imprime_fin1(p)
            print(calc_periodo(GAUSS,radio_prop),"años de la Tierra")
            print("--------")
        elif format == 2:
            print("--------")
            imprime_fin1(p)
            print(calcp_meses(GAUSS,radio_prop),"meses de la Tierra")
            print("--------")
        elif format == 3:
            print("--------")
            imprime_fin1(p)
            print(calcp_dias(GAUSS,radio_prop),"dias de la Tierra")
            print("--------")


    elif MenuPrincipal == 2:
         if p in list_planetas:
            print("--------")
            print("\n El planeta",p, "esta en la posicion"
            , posicion(list_planetas),"del sistema solar")
            print("--------")

    elif MenuPrincipal == 3:
        print("--------")
        print ("\nLa gravedad de la superficie del planeta",p,"es igual a:", 
        "\n",calc_gravedad(GRAV,m,radio_exacto))
        print("--------")

    elif MenuPrincipal == 4:
        print("--------")
        (imprime_fin4(lunas))
        print("--------")

    elif MenuPrincipal == 6:
        for i in range(len(list_planetas)):
            if p == list_planetas[i]:
                radio_exacto = list_radios_ex[i]
                m = list_masas[i]
                print ("\n\n--> Planeta:",list_planetas[i])
                print("--------")
                print ("--> Radio:",list_radios_ex[i])
                print("--------")
                print ("--> Masa:",list_masas[i],"\n\n")



    else: print("\nPor favor ingrese una opcion valida")

#La Opcion (5) aun no esta habilitada :(

#Repeticion de ciclo
    MenuPrincipal = int(input(interfaz_menu))