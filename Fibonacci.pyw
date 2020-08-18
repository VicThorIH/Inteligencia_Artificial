print("¿Que valor de Fibonacci quieres obtener?")

numero = int(input())
numero_Actual = 1
numero_Anterior = 0

# print("Posición - Numero")
# for i in range(1,numero + 1,1):
#     if i == 1 or i == 2:
#         print(i, "  -   ", numero_Actual)
#     else:
#         print(i, "  -  ", numero_Actual + numero_Anterior)
#         aux = numero_Actual
#         numero_Actual += numero_Anterior
#         numero_Anterior = aux



def fibonacci(n):
    
    if n == 1:
        
        return 0
    elif n == 2:
        
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print("Fibonacci #" + str(numero) + ": " + str(fibonacci(numero)))