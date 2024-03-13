"""
ESTRUCTURA DE DATOS  - COLLECIONES

LISTAS []
DICCIONARIOS {}
TUPLAS ()
CONJUNTOS(SETS) {}

- Almacenar mas de un dato a la vez
- Diferentes tipos
- Metodos y Funciones Manipular los datos
- Generalmente comienza con el indice0
"""
frutas = []
frutas = list()
frutas = ["Manzanas", "Platanos", "Peras", 'Naranjas']
# print(frutas[2])
# print(frutas)
# print(type(frutas))
frutas.append("Fresas")  # todo Añade un elemento al final de la lista
frutas.insert(2, "Sandia")  # todo inserta un valor de la lista en la posicion indicada
frutas.pop(0)  # todo elimina un elemento de la lista por su index
frutas.remove("Naranjas")  # todo eliminar un elemento de la lista por su valor
frutas[2] = "Manzanas"

# for i,f in enumerate(frutas):
#    print(f"{i} {f}")

"""
Realizar un programa que me permita llenar en una lista
sueldos de empleados , el programa debe terminar cuando ingrese 0
luego calcular el total de sueldo,el promedio de sueldo, el mayor sueldo y el menor
"""

sueldo_empleados = list()
cont = 1
sum = 0
while True:
    sueldo = float(input(f"Ingrese el sueldo del empleado{cont}  [cero] Para Terminar:"))
    if sueldo != 0 :
        sueldo_empleados.append(sueldo)
    cont += 1  # todo Contando lo valores de la lista
    sum += sueldo  # todo acumulando el sueldo
    if sueldo == 0:
        break
if len(sueldo_empleados) > 0:
    promedio = sum / len(sueldo_empleados)
    max_sueldo = max(sueldo_empleados)
    min_sueldo = min(sueldo_empleados)
    for i, s in enumerate(sueldo_empleados):
        print(f"{i} {s}")
    print(
        f"El Sueldo total es {sum} \nY el Promedio es {round(promedio, 2)}\nEl Sueldo Maximo es {max_sueldo}\nEl Minimo es {min_sueldo}")
else:
    print("No Hay Valores que mostrar")
