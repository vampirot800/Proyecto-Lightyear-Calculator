# Lightyear-Calculator
#### Descripcion

**!!!ESTE PROGRAMA REQUIERE DE LA DESCARGA DE LAs BIBLIOTECAs TERMCOLOR, PRETTYTABLE!!!**
Por lo que inclui dos archivos en el repositorio:

1: Lightyear Calculator.py <--- (archivo original sin requerimientos de descarga)
2: LightCalc(+bibliotecas).py <--- (archivo extra con bibliotecas termcolor, prettytable)

El proyecto **Lightyear Calculator**

El programa funciona como una calculadora con interfaz de menu
en la cual se le proporciona al usuario con diversas opciones 
acerca de los planetas del sistema solar (periodos orbitales,
gravedad, etc..)
El programa tomara la opcion que el usuario seleccione y los 
planetas ingresados por el usuario y devolvera la informacion
solicitada.

Este proyecto fue realizado con formulas de fisica que fueron investigadas cuidadosamente para obtener los resultados matematicos correctos 
, por lo que el usuario puede confirmar en internet o sitios como NASA cualquier informacion que el programa le brinde para comprobar que esta es veridica y fue programada y calculada de una manera efectiva.





#### Pseudocodigo inicial (Avance 1-2)
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
