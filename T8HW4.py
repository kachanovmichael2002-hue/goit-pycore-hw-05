from typing import Callable, Dict, List


# ===========================================
# Декоратор для обробки помилок введення
# ===========================================
def input_error(func: Callable) -> Callable:
    """
    Декоратор для обробки помилок введення користувача.
    Ловить KeyError, ValueError, IndexError і повертає
    повідомлення замість аварійного завершення.
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "This contact does not exist."
        except IndexError:
            return "Enter user name."

    return inner


# ===========================================
# Команди бота
# ===========================================
@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Додає контакт у словник contacts."""
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."


@input_error
def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Змінює номер телефону існуючого контакту."""
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Contact {name} updated."


@input_error
def get_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """Повертає номер телефону контакту."""
    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"{name}'s phone: {contacts[name]}"


@input_error
def show_all(contacts: Dict[str, str]) -> str:
    """Показує всі контакти."""
    if not contacts:
        return "No contacts yet."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


# ===========================================
# Основна частина
# ===========================================
def main() -> None:
    contacts: Dict[str, str] = {}
    print("Hello! This is your assistant bot. Type 'help' for commands.")
    while True:
        user_input = input(">>> ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input.startswith("add"):
            args = user_input.split()[1:]  # відділяємо команду від аргументів
            print(add_contact(args, contacts))
        elif user_input.startswith("change"):
            args = user_input.split()[1:]
            print(change_contact(args, contacts))
        elif user_input.startswith("phone"):
            args = user_input.split()[1:]
            print(get_phone(args, contacts))
        elif user_input == "show all":
            print(show_all(contacts))
        elif user_input == "help":
            print(
                "Commands:\n"
                "add [name] [phone] - add new contact\n"
                "change [name] [phone] - change contact's phone\n"
                "phone [name] - get phone number\n"
                "show all - list all contacts\n"
                "exit - quit"
            )
        else:
            print("Unknown command. Type 'help' for commands.")


# ===========================================
if __name__ == "__main__":
    main()