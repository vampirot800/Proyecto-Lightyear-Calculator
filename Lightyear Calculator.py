import math
math.pow
math.sqrt

k = int(1)
r = 0
p = input("Escriba el planeta del sistema solar de su preferencia:")

def calc_periodo(k,r):
    res=math.sqrt((k)*(pow(r,3)))
    return res

def calc_meses(k,r):
    meses = (calc_periodo(k,r))*(12)
    return meses

def imprime_fin(p):
    print("El periodo orbital de",p,"en dar la vuelta al sol es de:")


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

opcion = calc_periodo(k,r)

if opcion < 1 :
    (imprime_fin(p)),print(calc_meses(k,r),"meses")
elif opcion > 1:
    (imprime_fin(p)),print(calc_periodo(k,r),"años")
elif opcion == 1:
    (imprime_fin(p)),print(calc_periodo(k,r),"año")
