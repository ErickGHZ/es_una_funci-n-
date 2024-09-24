def calcular_reciprocos():
    # Crear una lista para almacenar los números
    numeros = []

    # Solicitar 5 números reales al usuario
    for i in range(5):
        while True:
            try:
                numero = float(input(f"Ingrese el número real {i + 1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Por favor, ingrese un número real válido.")

    # Verificar si el conjunto contiene el 0
    if 0 in numeros:
        print("El conjunto de valores contiene el 0. No puede ser una función.")
        return None

    # Calcular los recíprocos
    reciprocos = [1 / numero for numero in numeros]
    
    return reciprocos

# Llamar a la función y mostrar los resultados
resultados = calcular_reciprocos()
if resultados is not None:
    print("Los recíprocos son:", resultados)
