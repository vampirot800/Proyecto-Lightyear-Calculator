import math
math.pow
math.sqrt

k = int(1)
r = 0
p = input("Escriba el planeta del sistema solar de su preferencia:")

def calc_periodo(k,r):
    res=math.sqrt((k)*(pow(r,3)))
    return res

if p == "mercurio":
    r = 0.39
if p == "venus":
    r = 0.72
if p == "tierra":
    r = 1.00
if p == "marte":
    r = 1.52
if p == "jupiter":
    r = 5.20
if p == "saturno":
    r = 9.54
if p == "urano":
    r = 19.19
if p == "neptuno":
    r = 30.06

print ("El periodo orbital de",p, "en dar la vuelta al sol es de:",calc_periodo(k,r),"años")