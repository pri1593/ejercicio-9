# Ejercicio 9
historial5 = [8520, 9510, 7530, 3570, 1590]
def valorMaximo(valor):
    mayor = valor[0]
    for i in range(1, len(valor)):
        if valor[i] > mayor:
            mayor = valor[i]
    return mayor

print(valorMaximo(historial5))        
