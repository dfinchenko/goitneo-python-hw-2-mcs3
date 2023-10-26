def input_error(func):
    '''
    Обробка винятків
    '''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Missing arguments."
        except KeyError:
            return "Contact not found."
    return inner

@input_error
def add_contact(args, contacts):
    '''
    Додає новий контакт до словника контактів
    '''
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    '''
    Оновлює номер телефону існуючого контакту
    '''
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact updated."
    else:
        return f"Not found."

@input_error
def show_phone(args, contacts):
    '''
    Відображає номер телефону контакту
    '''
    [name] = args
    if name in contacts:
        return f"{contacts[name]}"
    else:
        return f"Not found."

@input_error
def show_all(contacts):
    '''
    Відображає всі збережені контакти
    '''
    if contacts:
        all_contacts = []
        for name, phone in contacts.items():
            all_contacts.append(f"{name}: {phone}")
        return "\n".join(all_contacts)
    else:
        return "No contacts stored."
    
def parse_input(user_input):
    '''
    Обробляє введені дані, розділяючи рядок на команду та аргументи
    '''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    '''
    Головна функція, де знаходиться логіка бота
    '''
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")  # Отримання команди від користувача
        command, *args = parse_input(user_input)  # Парсинг команди

        # Перевірка команд та відповідна дія
        if command in ["close", "exit"]:
            print("Good bye!")
            break  # Вихід
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))  # Додавання нового контакту
        elif command == "change":
            print(change_contact(args, contacts))  # Зміна існуючого контакту
        elif command == "phone":
            print(show_phone(args, contacts))  # Відображення номеру телефону контакту
        elif command == "all":
            print(show_all(contacts))  # Відображення всіх контактів
        else:
            print("Invalid command.")

# Точка входу
if __name__ == "__main__":
    main()