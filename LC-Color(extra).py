
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

""" 
========================= Bibliotecas ==============================
"""

#Biblioteca y funciones math
import math
math.pow
math.sqrt

#Nuevas funciones/bibliotecas

from termcolor import cprint 
"""
Esta biblioteca le proporciona con una variedad de colores para texto
en python, al igual que fonts que se implementan al codigo por medio
de cprint ("texto","red",attrs=[bold])
aprendido de https://pypi.org/project/termcolor/
"""

from prettytable import PrettyTable 
x = PrettyTable()
"""
Esta biblioteca le proporciona al usuario con una forma visualmente
placentera y ordenada de organizar informacion, por medio de tablas
con columnas y filas que se implementan al programa por medio de
x.add_column("Area", [, , , , ]), enc = ["Planeta", "Radio", "Masa"]
y x.clear()
aprendido de https://pypi.org/project/prettytable/
"""


cprint("\n \n Bienvenido a LightYear Calculator.py!","blue")


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
p_2 =()
interfaz_menu = (
"""


===================== Menu Principal:=========================

¿Que desea Calcular?

1: Periodo orbital 
2: Posicion 
3: Gravedad 
4: Lunas 

5: Grafica de info general 

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

opciones_comp = (
"""
Que desea comparar?:

1: Radio
2: Masa 

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

#lista de numero de lunas por planeta
list_lunas = [0,0,1,2,79,82,27,14]

#lista de masas usada para
# calcular la gravedad
list_masas = [3.302*(pow(10,23)),4.869*(pow(10,24))
,5.9710*(pow(10,24)),6.4169*(pow(10,23)),1.899*(pow(10,27))
,5.688*(pow(10,26)),8.686*(pow(10,25)),1.024*(pow(10,26))]

#Lista anidada usada para agrupar la informacion 
# de tres listas en una tabla
matriz = [list_planetas,list_radios_ex,list_masas]



""" 
========================= Funciones ==============================
"""


#Funciones: Calculo del periodo en años/meses/dias 
#,Calculo de gravedades, Impresiones de textos finales, 
#Asignacion de posicion de planetas, Comparacion de planetas

def calc_periodo(GAUSS,radio_prop):
    """
    recibe: GAUSS valor constante numerico, radio_prop valor numérico
    saca la raiz cuadrada de la multiplicacion de GAUSS por 
    radio_prop al cubo
    devuelve: resultado de operación numérico (periodo orbital)
    """
    res = math.sqrt((GAUSS)*(pow(radio_prop,3)))
    return res


def calcp_meses(GAUSS,radio_prop):
    """
    recibe: GAUSS valor constante numerico, radio_prop valor numérico
    multiplica el resultado de la funcion calc_periodo por 12
    devuelve: resultado de operación numérico en meses (periodo orbital)
    """
    a = calc_periodo(GAUSS,radio_prop)
    meses = (a)*(12)
    return meses

def calcp_dias(GAUSS,radio_prop):
    """
    recibe: GAUSS valor constante numerico, radio_prop valor numérico
    multiplica el resultado de la funcion calcp_meses por 30.44
    devuelve: resultado de operación numérico en dias (periodo orbital)
    """
    b = calcp_meses(GAUSS,radio_prop)
    dias = (b)*(30.44)
    return dias

def calc_gravedad(GRAV,masas,radio_exacto):
    """
    recibe: GRAV valor constante numerico, masa valor numerico, 
    radio_exacto valor numerico
    multiplica GRAV por la division de masas entre radio_exacto
    elevado al cuadrado por 10 elevado a la sexta potencia 
    devuelve: resultado de operación numérica (gravedad)
    """
    g = GRAV*(masas/pow(radio_exacto*(pow(10,6)),2))
    return g 
    

def imprime_fin1(p):
    """
    recibe: p variable string planeta
    devuelve: una impresion de texto final con la variable 
    """
    print( "El periodo orbital de",p,
    "aproximado en dar la vuelta al sol es de:")

def imprime_fin4(lunas):
    """
    recibe: lunas valor numerico
    devuelve: una impresion de texto final con la variable 
    """
    print("El planeta",p,"cuenta con un numero de:"
    ,lunas,"lunas confirmadas")


def posicion(list_planetas):
    """
    recibe: lista list_planetas
    hace uso de un indice para obtener la posicion del planeta en la lista
    del planeta ingresado por el usuario sumando 1 para encontrarla
    devuelve: una impresion de texto con la variable 
    """
    return list_planetas.index(p)+1


def informacion(matriz):
    """
    recibe: matriz/lista anidada
    hace uso de la biblioteca prettytable para generar una tabla
    con todos los datos de la matriz y separarla en columnas
    devuelve: la tabla de la matriz (x)
    """
    x.clear()
    enc = ["Planeta", "Radio", "Masa"]
    for i in range(len(matriz)):
        x.add_column(enc[i], matriz[i])
    print(x)


""" 
=============== Parte Principal del programa =====================
"""


#Variable Menu
Menu_principal = int(input(interfaz_menu))


while Menu_principal !=0:

#Input variable str(p) = planeta
    if Menu_principal != 5:
        p = str(input
("""Escriba el planeta del sistema solar de su preferencia: """))


#Asignacion de variables dependiendo del planeta         
        for i in range(len(list_planetas)):
            if p == list_planetas[i]:
                radio_prop = list_radios_prop[i]
                radio_exacto = list_radios_ex[i]
                lunas = list_lunas[i]
                masas = list_masas[i]


#Condiciones de Menu
    if Menu_principal == 1: 
        format = int(input(opciones_periodo))
        if format == 1:
            print("\n--------")
            imprime_fin1(p)
            a = (calc_periodo(GAUSS,radio_prop),"años terrestres")
            cprint(a, "blue", attrs=["bold"])
            print("--------")
        elif format == 2:
            print("\n--------")
            imprime_fin1(p)
            b = (calcp_meses(GAUSS,radio_prop),"meses terrestres")
            cprint(b,"green", attrs=["bold"])
            print("--------")
        elif format == 3:
            print("\n--------")
            imprime_fin1(p)
            c = (calcp_dias(GAUSS,radio_prop),"dias terrestres")
            cprint(c,"magenta", attrs=["bold"])
            print("--------")


    elif Menu_principal == 2:
         if p in list_planetas:
            cprint("\n---------------", "green")
            print(" El planeta",p, "esta en la posicion"
            ,posicion(list_planetas),"del sistema solar")
            cprint("---------------","green")

    elif Menu_principal == 3:
        cprint("\n---------------", "red")
        print ("La gravedad de la superficie del planeta",p,"es igual a:", 
        "\n",calc_gravedad(GRAV,masas,radio_exacto))
        cprint("---------------","red")

    elif Menu_principal == 4:
        cprint("\n---------------", "yellow")
        imprime_fin4(lunas)
        cprint("---------------","yellow")


    
    elif Menu_principal == 5:
        informacion(matriz)

#Repeticion de ciclo

    input("\npresione enter para regresar al menu")

    Menu_principal = int(input(interfaz_menu))

        
else: print("\nPor favor ingrese una opcion valida")
