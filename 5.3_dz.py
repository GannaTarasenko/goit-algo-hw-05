import sys

# Функція для розбору рядка логу і створення словника з компонентами
def parse_log_line(line: str) -> dict:
    parts = line.split(' ', maxsplit=3)  # Розділяємо рядок на частини, обмежуючи максимальне розділення до 3
    return {'date': parts[0], 'time': parts[1], 'level': parts[2], 'message': parts[3].strip()}  # Повертаємо словник з компонентами логу

# Функція для завантаження логів з файлу
def load_logs(file_path: str) -> list:
    logs = []  # Створюємо порожній список для збереження логів
    try:
        with open(file_path, 'r') as file:  # Відкриваємо файл для читання
            for line in file:  # Читаємо кожен рядок у файлі
                logs.append(parse_log_line(line))  # Додаємо розібраний рядок логу до списку
    except FileNotFoundError:
        print("File not found.")  # Обробляємо виняток, якщо файл не знайдено
        sys.exit(1)  # Виходимо з програми з кодом помилки 1
    except Exception as e:
        print(f"Error reading file: {e}")  # Обробляємо інші винятки, які можуть виникнути при читанні файлу
        sys.exit(1)  # Виходимо з програми з кодом помилки 1
    return logs  # Повертаємо список зі завантаженими логами

# Функція для фільтрації логів за рівнем логування
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level]  # Фільтруємо логи за вказаним рівнем логування

# Функція для підрахунку кількості логів за рівнем логування
def count_logs_by_level(logs: list) -> dict:
    counts = {'INFO': 0, 'DEBUG': 0, 'ERROR': 0, 'WARNING': 0}  # Ініціалізуємо лічильники для кожного рівня логування
    for log in logs:  # Проходимося по кожному лозі
        counts[log['level']] += 1  # Збільшуємо лічильник для відповідного рівня логування
    return counts  # Повертаємо словник з кількістю логів для кожного рівня логування

# Функція для відображення кількості логів для кожного рівня
def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17} | {count:<9}")

# Функція для відображення деталей логів для певного рівня
def display_logs(logs: list, level: str):
    print(f"\nДеталі логів для рівня '{level}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py/path/to/logfile.log [level]")
        
