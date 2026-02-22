import re
from typing import Generator, Callable


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генерує всі дійсні числа з тексту як float.
    Числа повинні бути відокремлені пробілами або межами слова.

    :param text: Вхідний рядок з числами
    :return: Генератор чисел float
    """
    # Регулярний вираз для цілих та дійсних чисел
    # (?:...) — некаптурюча група, щоб re.findall повертав весь збіг
    pattern = r'\b\d+(?:\.\d+)?\b'

    # Знаходимо всі збіги та повертаємо по одному через yield
    for match in re.findall(pattern, text):
        yield float(match)


def sum_profit(
    text: str, func: Callable[[str], Generator[float, None, None]]
) -> float:
    """
    Обчислює суму всіх чисел, що повертає генератор.

    :param text: Вхідний рядок з числами
    :param func: Функція-генератор, яка повертає числа
    :return: Сума чисел як float
    """
    total = 0.0
    for number in func(text):
        total += number
    return total


# ==========================
# Приклад використання
# ==========================
if __name__ == "__main__":
    text_example = "Прибуток за місяць: 100 200.5 50"

    # Використовуємо генератор для виводу чисел по одному
    print("Знайдені числа:")
    for num in generator_numbers(text_example):
        print(num)

    # Підсумовуємо числа
    total_profit = sum_profit(text_example, generator_numbers)
    print(f"Загальний прибуток: {total_profit}")