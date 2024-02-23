def get_digit(num, position):
    """
    Función para obtener el dígito en una posición específica de un número.
    """
    return (num // (10 ** position)) % 10

def radix_sort(arr):
    """
    Función que implementa el algoritmo Radix Sort para ordenar una lista de números.
    """
    max_num = max(arr)  # Encontrar el número máximo en la lista
    max_digits = len(str(max_num))  # Calcular la cantidad máxima de dígitos en los números

    # Imprimir el arreglo desordenado
    print("Arreglo desordenado:", arr)

    # Iterar a través de las posiciones de los dígitos
    for position in range(max_digits):
        # Crear una lista temporal para almacenar los números en cada posición
        temporal = [[] for _ in range(10)]

        # Distribuir los números en la lista temporal según el dígito en la posición actual
        for num in arr:
            digit = get_digit(num, position)
            temporal[digit].append(num)

        # Reconstruir el arreglo original con los números ordenados en la lista temporal
        arr = []
        for bucket in temporal:
            arr.extend(bucket)

        # Imprimir el arreglo parcialmente ordenado en esta posición
        print(f"Arreglo parcialmente ordenado en la posición {position + 1}:", arr)

        # Imprimir el arreglo antes de la próxima iteración
        if position < max_digits - 1:
            print(f"Actualización del arreglo para la posición {position + 1}:", arr)

    return arr

# Arreglo original
Arreglo = [22, 178, 249, 6, 18, 314]

# Ordenar el arreglo usando Radix Sort
Arreglo_ordenado = radix_sort(Arreglo)

# Imprimir el arreglo ordenado
print("Arreglo ordenado:", Arreglo_ordenado)
