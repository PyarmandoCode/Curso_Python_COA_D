"""
Escribe un programa que imprima los números del 1 al 100. Pero para múltiplos de 3,
imprime "Fizz" en lugar del número, y para múltiplos de 5, imprime "Buzz".
Para números que son múltiplos de ambos, imprime "FizzBuzz".
"""

for item in range(1, 101):
    if item % 3 == 0 and item % 5 == 0:
        print("FizzBuzz")
    elif item % 3 == 0:
        print("Fizz")
    elif item % 5 == 0:
        print("Buzz")
    else:
        print(item)
"""
El objetivo es filtrar elementos de una lista original y crear dos nuevas listas, 
 una con los elementos pares y otra con los elementos impares. 
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares=list()
impares=list()

for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f"La lista de pares {pares}")
print(f"La lista de impares {impares}")



