"""
CONDICIONALES MULTIPLES

#precio = int(input("Ingrese el precio:"))
if precio == 200:
    print("El Precio es 200")
elif precio == 100:
    print("El Precio es 100")
elif precio == 50:
    print("El Precio es 50")
else:
    print("El Precio es errado")
"""
"""
Hacer un programa que calcule la bonificacion que recibira un empleado
de acuerdo al area en que labora y su tiempo de servicio
*************
AREA  TS    BON
***************
SIS   >3    2%
CON  >4    3%
MAR   >2    1.4%
****************
"""
sueldo = float(input("Ingrese el sueldo del empleado:"))
area = input("Ingrese el area en que labora:")
ts = int(input("Ingrese el tiempo de servicio:"))
if area == "SIS" and ts > 3:
    bon = 0.02
elif area == "CON" and ts > 4:
    bon = 0.03
elif area == "MAR" and ts > 2:
    bon = 0.014
else:
    bon = 0
bonificacion= sueldo * bon
nuevo_sueldo = sueldo + bonificacion
if bonificacion>0:
    print(f"El Nuevo Sueldo que le corresponde es {round(nuevo_sueldo,2)} con Bon {bonificacion}")
else:
    print(f"El Nuevo Sueldo que le corresponde es {round(nuevo_sueldo,2)}")
