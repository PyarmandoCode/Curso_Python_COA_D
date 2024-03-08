trabajadores = [
    {"codigo": 1010, "ht": 20},  # 0
    {"codigo": 1011, "ht": 21},  # 1
    {"codigo": 1012, "ht": 21},  # 2
]
while True:
    codigo = input("Ingrese el codigo del trabajador:")
    ht = int(input("Ingrese las Horas Trabajadas:"))
    dato_nuevo = {
        "codigo": codigo,
        "ht": ht
    }
    trabajadores.append(
        dato_nuevo
    )
    rpta = input("Desea Continuar [S/N]:")
    if rpta == "N":
        break
total_gen=0
for indice, trabajador in enumerate(trabajadores):
    total_gen = total_gen + trabajadores[indice]["ht"] * 28
print(f" El Total de la planilla de este mes es: {total_gen/len(trabajadores)}")
