import re
from typing import Callable
from decimal import Decimal

def generator_numbers(text: str):
    pattern = r'\b\d+(\.\d+)?\b'  # Регулярний вираз для пошуку дійсних чисел
    for match in re.finditer(pattern, text):
        yield Decimal(match.group())  # Повертаємо кожне знайдене число як десяткове

def sum_profit(text: str, func: Callable):
    total = sum(func(text), Decimal('0'))  # Використовуємо генератор для отримання всіх чисел та підсумовуємо їх
    return total

# Приклад використання
text = "Встановити зарплатню Тарасенко Ганні у розмірі 2000 євро як основний дохід, доповнений премією у 500.05 євро помісячно і 5325.1 євро на гарну відпустку."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")