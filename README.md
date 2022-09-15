# Lightyear-Calculator
#### Descripcion

El proyecto **Lightyear Calculator** es un programa que tendra como funcion calcular una variedad de datos acerca de los planetas del sistema solar, por ahora  periodos orbitales, pero en el siguiente avance periodos de rotacion, gravedad, lunas, etc.

Este programa dara resultados de los periodos entre la variedad de cuerpos celestes de nuestro sistema solar a el sol.
En la version actual de este programa, se le presenta un menu al usuario, con el cual ingresara la opcion que quiera calcular incluyendo especificaciones como obtener el resultado en años o en meses y el usuario ingresara un cuerpo celeste del sistema solar su preferencia.

#### Pseudocodigo
Inicio
import math
math.pow, math.sqrt

Variables:
constante k = 1, r, p

funciones:
(Calculo para obtener periodo):
def calc_periodo(k,r)
 res=math.sqrt((k)*(pow(r,3)))
  return res

(Calculo para convertir periodo a meses):
calc_periodo*(12)

(mensaje de resultado):
imprimir ("El periodo orbital de",p,"en dar la vuelta al sol es de:")

(tomar en cuenta p en mayusculas y minusculas)

Dependiendo del planeta ingresado convertir "r" al radio correspondiente
(mercurio,venus,tierra,marte,jupiter,saturno,urano,neptuno)

opcion = calc_periodo
si opcion > 1 = imprimir mensaje de resultado y calculo del periodo en años
si opcion < 1 = imprimir mensaje de resultado y calculo de periodo en meses
  
Fin
