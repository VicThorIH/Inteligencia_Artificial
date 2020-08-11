print("¿Qué valor de Fibonacci quieres obtener?")

numero = int(input())
numero_Actual = 1
numero_Anterior = 1

print("Posición - Número")
for i in range(1,numero + 1,1):
    if i == 1 or i == 2:
        print(i, "  -   ", numero_Actual)
    else:
        print(i, "  -  ", numero_Actual + numero_Anterior)
        aux = numero_Actual
        numero_Actual += numero_Anterior
        numero_Anterior = aux

