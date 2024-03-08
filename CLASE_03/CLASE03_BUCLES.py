"""
BUCLES .-PROCESOS REPETITIVOS ITERAR UNA ACCION DETERMINADAS VECES

PARA .- for
 -Cuando se conoce las veces que el bucle iterar
MIENTRAS .- while
 -Va a finalizar el bucle mediante una condicion logica


for vuelta in range(1, 11, 2):
    print(f" {vuelta} Hola desde python")  # iterar = loop

con = 0
while con <= 10:
    #Hasta que sea True
    print(con)
    con += 1
"""
"""
Hacer un programa que me permita llenar "n" calificaciones
a una lista de datos el programa debe terminar cuando 
se escriba 0
"""
calificaciones = list()
while True:
    califacion = float(input("Ingrese la calificacion:"))
    if califacion == 0:
        break  # Interrumpir el loop
    calificaciones.append(califacion)
print(calificaciones)
