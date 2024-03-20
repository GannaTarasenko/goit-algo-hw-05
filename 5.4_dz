# Декоратор для обробки помилок введення користувача
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Incomplete command. Enter both name and phone."

    return inner

# Структура зберігання контактів
contacts = {}

# Функція для додавання контакту
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Функція для видалення контакту
@input_error
def delete_contact(name, contacts):
    del contacts[name]
    return "Contact deleted."

# Функція для отримання номеру телефону по імені контакту
@input_error
def get_phone(name, contacts):
    return contacts[name]

# Функція для виведення усіх контактів
@input_error
def show_all_contacts(contacts):
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result

# Головна функція обробки команд
def process_command(command, contacts):
    if command.startswith("add"):
        args = command.split()[1:]
        return add_contact(args, contacts)
    elif command.startswith("delete"):
        name = command.split()[1]
        return delete_contact(name, contacts)
    elif command.startswith("phone"):
        name = command.split()[1]
        return get_phone(name, contacts)
    elif command == "all":
        return show_all_contacts(contacts)
    else:
        return "Invalid command."

# Основний цикл взаємодії з користувачем
while True:
    user_input = input("Enter a command: ")
    print(process_command(user_input, contacts))
