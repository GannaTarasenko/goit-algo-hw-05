def caching_fibonacci():
    cache = {}  # Створення кешу для зберігання результатів обчислень

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:  # Перевірка, чи результат вже збережено у кеші
            return cache[n]
        else:
            # Рекурсивне обчислення числа Фібоначчі та збереження результату у кеш
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci

# Приклад використання
fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
