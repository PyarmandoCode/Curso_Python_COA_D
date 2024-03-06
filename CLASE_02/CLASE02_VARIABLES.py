"""
Variables
Tipo de datos Primitivos
"""
nombre_persona="Armando" #str
apellido_persona='Ruiz' #str
edad_persona=49 #int
sueldo_persona=1900.20 #float
estado=True #bool

#print("Hola Mundo desde Python")
#print(nombre_persona+apellido_persona)
#print(nombre_persona,apellido_persona)
#print(f"Tu Nombre es:{nombre_persona} y tu apellido:{apellido_persona} y la edad es : {edad_persona}") #inyeccion

"""
Operadores Matematicos
+,-,*,
/,// = division decimales,division entera
** = Exponente
% = Residuo de la division

Operadores Logicos
>,<,>=,<=,==,!=
and,or,not
"""
#print(23 // 4) #division entera
#print(23 / 4) #division decimales
#print(23 % 4) #Sobra de la division

"""
Hacer un Programa que me permita calcular el promedio de un estudiante
teniendo sus tres calificaciones
"""
calificacion_1=float(input("Ingrese la calificacion #1:"))
calificacion_2=float(input("Ingrese la calificacion #2:"))
calificacion_3=float(input("Ingrese la calificacion #3:"))
promedio=(calificacion_1+calificacion_2+calificacion_3)/3
if promedio>=10.5:
    print(f"El Estudiante Aprobo con una calificacion de {round(promedio,1)} ")
else:
    nota_sustitutoria=float(input("Ingrese la Nota Sustitutoria:"))
    nuevo_promedio=(nota_sustitutoria+promedio)/2
    if nuevo_promedio>=10.5:
        print(f"El Estudiante Aprobo con una calificacion de {round(nuevo_promedio, 1)} ")
    else:
        print(f"El Estudiante Desaprobo con una calificacion de {round(nuevo_promedio, 1)} ")

"""
Condicionales
edad=12
if edad>=18:#identacion
    print("La persona es mayor edad")#verdad
else:
    print("La persona es menor de edad") #falso
"""
