import math
math.pow
math.sqrt
 
print("\n \n Bienvenido a LightYear Calculator.py! \n \n")

k = int(1)
r = 0
l = 0

def calc_periodo(k,r):
    res=math.sqrt((k)*(pow(r,3)))
    return res

def calcp_meses(k,r):
    meses = (calc_periodo(k,r))*(12)
    return meses

def imprime_fin1(p):
    print( "\n\n" "El periodo orbital de",p,"en completar una vuelta al sol es de:")

def imprime_fin4(l):
    print("\n",p,"cuenta con un numero de:",l,"lunas confirmadas")

MenuPrincipal = int(input("Menu Principal: \n \n ¿Que desea Calcular? \n \n 1: Periodo orbital \n 2: Periodo de rotacion \n 3: Gravedad \n 4: Lunas \n 0: Salir \n"))

while MenuPrincipal !=0:

    p = input("Escriba el planeta del sistema solar de su preferencia:")
    if p.lower() == "mercurio":
        r = 0.39
        l = 0
    if p.lower()== "venus":
        r = 0.72
        l = 0
    if p.lower() == "tierra":
        r = 1.00
        l = 1
    if p.lower() == "marte":
        r = 1.52
        l = 2
    if p.lower() == "jupiter":
        r = 5.20
        l = 79
    if p.lower() == "saturno":
        r = 9.54
        l = 82
    if p.lower() == "urano":
        r = 19.19
        l = 27
    if p.lower() == "neptuno":
        r = 30.06
        l = 14

    if MenuPrincipal == 1: 
        format = int(input("Como desea obtener el resultado?: \n 1: Años \n 2: Meses \n"))
        if format == 1:
            imprime_fin1(p)
            print()
            print(calc_periodo(k,r),"años")
            print()
        elif format == 2:
            (imprime_fin1(p)),print(calcp_meses(k,r),"meses")
            print()
            
    elif MenuPrincipal == 4:
        (imprime_fin4(l))

    else: print("Por favor ingrese una opcion valida")

    MenuPrincipal = int(input("\n Menu Principal: \n \n ¿Que desea Calcular? \n \n 1: Periodo orbital \n 2: Periodo de rotacion \n 3: Gravedad \n 4: Lunas \n 0: Salir \n"))
        


