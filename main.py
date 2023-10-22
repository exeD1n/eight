class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def update_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
        else:
            print(f"Контакт с именем {name} не найден.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Контакт с именем {name} удален.")
        else:
            print(f"Контакт с именем {name} не найден.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Имя: {name}, Телефон: {self.contacts[name]}")
        else:
            print(f"Контакт с именем {name} не найден.")

    def list_contacts(self):
        for name, phone in self.contacts.items():
            print(f"Имя: {name}, Телефон: {phone}")

# Пример использования
phonebook = Phonebook()
phonebook.add_contact("John", "555-1234")
phonebook.add_contact("Alice", "555-5678")
phonebook.add_contact("Bob", "555-9876")

phonebook.list_contacts()

# Изменить номер для контакта "Alice"
phonebook.update_contact("Alice", "555-9999")

# Удалить контакт "John"
phonebook.delete_contact("John")

# Вывести список контактов после изменения и удаления
phonebook.list_contacts()
