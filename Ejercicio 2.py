"""

Crear 3 variables y asignarles 3 valores numericos entre los valores 1 
y 15, sin repetir y hacer la sigueinte cuenta:

A la primer variable le sumo 10 y lo multiplico por 5, a la segunda 
variable le resto 5 y le sumo el resultado de la primer variable y a 
la tercer variable le sumo el resultado de la segunda variable y la 
divido por 4, luego mostrar el resultado por pantalla. Solo puede haber 
3 variables no mas.

"""

valor1 = 5
valor2 = 9
valor3 = 15
valor1 = (valor1 + 10) * 5
valor2 = valor2 - 5 + valor1
valor3 = (valor3 + valor2) / 4
print('valor1 =', valor1)
print('valor2 =', valor2)
print('valor3 =', valor3)