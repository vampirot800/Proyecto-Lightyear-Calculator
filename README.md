# Lightyear-Calculator
#### Descripcion

El proyecto **Lightyear Calculator**

El programa funciona como una calculadora con interfaz de menu
en la cual se le proporciona al usuario con diversas opciones 
acerca de los planetas del sistema solar (periodos orbitales,
gravedad, etc..)
El programa tomara la opcion que el usuario seleccione y los 
planetas ingresados por el usuario y devolvera la informacion
solicitada.

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
