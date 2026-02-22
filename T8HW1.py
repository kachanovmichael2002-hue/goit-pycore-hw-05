from typing import Callable, Dict

def caching_fibonacci() -> Callable[[int], int]:
    """
    Повертає функцію fibonacci(n), яка обчислює n-е число Фібоначчі
    з використанням кешу для оптимізації рекурсивних викликів.
    """
    cache: Dict[int, int] = {}  # Словник для кешу {n: F(n)}

    def fibonacci(n: int) -> int:
        """Обчислює n-е число Фібоначчі рекурсивно з кешуванням."""
        # Базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1
        # Перевірка кешу
        if n in cache:
            return cache[n]
        # Рекурсивний виклик і збереження в кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci  # Повертаємо внутрішню функцію (замикання)

# ==========================
# Приклад використання
# ==========================
if __name__ == "__main__":
    # Створюємо функцію Фібоначчі з кешем
    fib = caching_fibonacci()

    # Використовуємо функцію
    print(fib(10))  # 55
    print(fib(15))  # 610
    print(fib(5))   # 5, швидко повертається з кешу
