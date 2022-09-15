import math
math.pow
math.sqrt

print("Bienvenido a LightYear Calculator.py!")

k = int(1)
r = 0

def calc_periodo(k,r):
    res=math.sqrt((k)*(pow(r,3)))
    return res

def calcp_meses(k,r):
    meses = (calc_periodo(k,r))*(12)
    return meses

def imprime_fin(p):
    print("El periodo orbital de",p,"en dar la vuelta al sol es de:")

MenuPrincipal = int(input("Menu Principal: \n ¿Que desea Calcular? \n 1: Periodo orbital \n 2: Periodo de rotacion \n 3: Gravedad \n 4: Lunas \n 0: Salir \n"))

while MenuPrincipal !=0:

    p = input("Escriba el planeta del sistema solar de su preferencia:")
    if p.lower() == "mercurio":
        r = 0.39
    if p.lower()== "venus":
        r = 0.72
    if p.lower() == "tierra":
        r = 1.00
    if p.lower() == "marte":
        r = 1.52
    if p.lower() == "jupiter":
        r = 5.20
    if p.lower() == "saturno":
        r = 9.54
    if p.lower() == "urano":
        r = 19.19
    if p.lower() == "neptuno":
        r = 30.06

    if MenuPrincipal == 1: 
        format = int(input("Como desea obtener el resultado?: \n 1: Años \n 2: Meses \n"))
        if format == 1:
            print(imprime_fin(p)),print(calc_periodo(k,r),"años")
        elif format == 2:
            print(imprime_fin(p)),print(calcp_meses(k,r),"meses")
        
        
    else: print("Por favor ingrese una opcion valida")

    MenuPrincipal = int(input("\n Menu Principal: \n ¿Que desea Calcular? \n 1: Periodo orbital \n 2: Periodo de rotacion \n 3: Gravedad \n 4: Lunas \n 0: Salir \n"))
        


