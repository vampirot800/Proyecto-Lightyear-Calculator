# Lightyear-Calculator
#### Descripcion

El proyecto **Lightyear Calculator** es un programa que tendra como funcion calcular el tiempo que un planeta tarda en dar una vuelta al sol.

Este programa dara resultados de los periodos entre la variedad de cuerpos celestes de nuestro sistema solar a el sol.
Lightyear Calculator sera actualizado de forma recurrente para en un futuro calcular distancias de lunas, estrellas, cometas y hasta otros sistemas solares o galaxias, dando resultados en km o años luz dependiendo de la distancia.
En la primera version de este programa, El usuario ingresara un cuerpo celeste del sistema solar su preferencia y el programa le calculara  el periodo que existe entre el cuerpo solicitado y el sol en años o en meses, dependiendo si de el resultado es mayor o menor a 1 año. (muy util si llevas fisica de primer semestre ;))

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
