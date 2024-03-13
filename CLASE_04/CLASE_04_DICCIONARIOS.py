"""
Diccionarios
-Almacenar y organizar informacion
-Los diccionarios utilizan claves(keys)para acceder a los valores asociados.
-Cada par clave-valor es un diccionario es unico
-Son muy utiles cuando necesitas almacenr informacion de manera estructurada
y acceder a ella de manera rapida por medio de un identificador
"""

"""
Crear un diccionario con informacion de una persona
"""
lista_empleados = [
    {'nombre': 'juan', 'edad': 25, 'ciudad': 'Lima', 'ocupacion': 'empleado'},
    {'nombre': 'armando', 'edad': 45, 'ciudad': 'Cuzco', 'ocupacion': 'empleado'},
]

# print(lista_empleados[0])

# for x, d in enumerate(lista_empleados):
#    #print(f"{x} {d}")
#    print(f"{x} {d["nombre"]} {d["ocupacion"]}")

persona = {'nombre': 'juan', 'edad': 25, 'ciudad': 'Lima', 'ocupacion': 'empleado'}

persona['idioma'] = 'Español'
persona['ciudad'] = 'Cuzco'
del persona['ciudad']

#print(persona)
# print(persona['nombre'])
# print(persona['ocupacion'])
# print(persona['edad'])

empresa = {
    'nombre': 'Techco',
    'ubicacion': 'Ciudad Tech',
    'empleados':
        {
            'jefe': 'Alice',
            'programadores': ['Bob', 'Charlie', 'David', 'Fanny'],
            'diseñadores': ['Eva', 'Frank']
        }
}

print(empresa['empleados']['programadores'][1])