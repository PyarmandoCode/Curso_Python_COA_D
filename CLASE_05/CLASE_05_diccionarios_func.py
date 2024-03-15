"""
Hacer un programa que me permita ingresar "N" empleados a una lista con las sgtes caracteristicas:
1-El programa debe terminar cuando se ingrese "n"
2.Se debera calcular el pago a recibir por empleado
3.Se debera hallar el promedio de pago 
4.Se debera hallar el empleado con mayor salario
5.Se debera hallar el empleado con menor salario
"""
empleados =[
    {"codigo":"EMP-01","ht":16},
    {"codigo":"EMP-02","ht":18},
    {"codigo":"EMP-03","ht":20}
]

nuevos_empleados_list=list()
def hacer_totales():
    for empleado in empleados:
        pago=empleado["ht"]*39
        nuevos_empleados = {
             "codigo":empleado["codigo"],
             "ht":empleado["ht"],
             "pago":pago
        }
        nuevos_empleados_list.append(nuevos_empleados)
        suma_pagos =+ pago
    cantidad_empleados=len(nuevos_empleados_list)
    promedio_pagos=suma_pagos/cantidad_empleados #Numerica
    return nuevos_empleados_list,promedio_pagos
    
def listar_empleados():
    nuevos_empleados_list,promedio=hacer_totales()
    for index,empleado in enumerate(nuevos_empleados_list):
        print(f"{index} {empleado}")
    print(f"El Promedio de Pagos es {round(promedio,2)}")    

while True:
    cod_val=input("Ingrese el codigo del empleado:")
    ht_val=int(input("Ingrese las horas trabajadas:"))
    nuevo_empleado = {
        "codigo":cod_val,
        "ht":ht_val,
    }
    empleados.append(nuevo_empleado)
    rpta=input("Desea Ingresar otro empleado:")
    if rpta=="n":
        break
listar_empleados()    

    
     