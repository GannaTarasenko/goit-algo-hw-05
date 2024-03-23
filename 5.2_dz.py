import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\b\d+(\.\d+)?\b'  # Регулярний вираз для пошуку дійсних чисел
    for match in re.finditer(pattern, text):
        yield float(match.group())  # Повертаємо кожне знайдене число як дійсне

def sum_profit(text: str, func: Callable):
    total = sum(func(text))  # Використовуємо генератор для отримання всіх чисел та підсумовуємо їх
    return total

# Приклад використання
text = "Встановити зарплатню Тарасенко Ганні у розмірі 2000 євро як основний дохід, доповнений премією у 500.05 євро помісячно і 325.1 євро на гарну відпустку."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")