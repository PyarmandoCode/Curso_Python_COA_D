"""
-Es un bloque de codigo reutilizable que realiza una tarea especifica
-Puedes definir una funcion y luego llamarla en cuanquier parte del codigo
-Las funciones pueden tomar tomar argumentos(Parametros) y devolver un resultado opcional
"""

def saludar(nombre):
    mensaje=f"hola {nombre}!"
    return mensaje

#print(saludar("Armando"))

#Funciones con multiples parametros
def calcular_rectangulo(base,altura):
    """Esta funcion calcular el area y el perimetro de un rectangulo"""
    area=base*altura
    perimetro=2*(base + altura)
    return area,perimetro

a,p=calcular_rectangulo(4,5)
#print(f"El Area es {a} y el Perimetro es {p}")

#Funciones con argumentos predeterminados
def mensaje_bienvenida(curso="Python"):
    print(f"Curso de {curso}" )

#mensaje_bienvenida("JAVA")    




