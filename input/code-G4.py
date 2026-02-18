# # Obtener n números primos

# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Función para obtener una lista de números primos hasta n
def obtener_primos(n):
    primos = []
    for numero in range(2, n + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

# Ejemplo de uso
if __name__ == "__main__":
    n = 50
    numeros_primos = obtener_primos(n)
    print(f"Números primos hasta {n}: {numeros_primos}")