from __future__ import absolute_import

class App:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def resta(a, b):
        return a - b

    @staticmethod
    def multiplicacion(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        if b == 0:
            raise ValueError("División por cero no permitida")
        return a / b

    # 1. Verifica si una lista contiene un número primo
    @staticmethod
    def contiene_numero_primo(lista):
        def es_primo(num):
            if num <= 1:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        for numero in lista:
            if es_primo(numero):
                return True
        return False

    # 2. Cuenta los números pares en un rango dado
    @staticmethod
    def contar_pares(inicio, fin):
        return sum(1 for i in range(inicio, fin + 1) if i % 2 == 0)

    # 3. Encuentra el número máximo en una lista que sea múltiplo de un valor dado
    @staticmethod
    def maximo_multiplo(lista, multiplo):
        multiplos = [num for num in lista if num % multiplo == 0]
        return max(multiplos) if multiplos else None

    # 4. Verifica si una palabra es palíndroma
    @staticmethod
    def es_palindromo(palabra):
        return palabra == palabra[::-1]

    # 5. Calcula la suma de los primeros n números impares
    @staticmethod
    def suma_primeros_impares(n):
        return sum(i for i in range(1, 2 * n, 2))

    # 6. Verifica si todos los elementos de una lista son únicos
    @staticmethod
    def elementos_unicos(lista):
        return len(lista) == len(set(lista))

    # 7. Calcula el factorial de un número sin usar recursión
    @staticmethod
    def calcular_factorial(numero):
        if numero < 0:
            raise ValueError("El factorial no está definido para números negativos")
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

    # 8. Cuenta la cantidad de vocales en una cadena
    @staticmethod
    def contar_vocales(cadena):
        return sum(1 for char in cadena.lower() if char in "aeiou")

    # 9. Encuentra el segundo número mayor en una lista
    @staticmethod
    def segundo_mayor(lista):
        unicos = list(set(lista))
        if len(unicos) < 2:
            return None
        unicos.sort(reverse=True)
        return unicos[1]

    # 10. Calcula la serie de Fibonacci hasta n términos
    @staticmethod
    def fibonacci(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        serie = [0, 1]
        for i in range(2, n):
            serie.append(serie[-1] + serie[-2])
        return serie
