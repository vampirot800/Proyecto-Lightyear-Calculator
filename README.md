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
funcion def calc_periodo(k,r)
(Calculo para obtener periodo): res=math.sqrt((k)*(pow(r,3)))
  return res
  
 Si planeta = mercurio:
   convertir radio (r) = 0.39
 Si planeta = venus:
   convertir radio (r) = 0.72
 Si planeta = tierra:
   convertir radio (r) = 1.00
 Si planeta = marte:
   convertir radio (r) = 1.52
 Si planeta = jupiter:
   convertir radio (r) = 5.20
 Si planeta = saturno:
   convertir radio (r) = 9.54
 Si planeta = urano:
   convertir radio (r) = 19.19
 Si planeta = neptuno:
   convertir radio (r) = 30.06
   
   imprimir resultado de periodo
  
Fin
