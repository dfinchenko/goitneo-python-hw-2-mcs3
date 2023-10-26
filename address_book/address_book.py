from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)

    def validate(self):
        '''
        Валідація
        '''
        if len(self.value) == 10 and self.value.isdigit():
            return True
        else:
            raise ValueError("Phone number must be 10 digits long")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        '''
        Додавання телефонів
        '''
        phone = Phone(phone_number)
        if phone.validate():
            self.phones.append(phone)

    def remove_phone(self, phone_number):
        '''
        Видалення телефонів
        '''
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return True
        return False  

    def edit_phone(self, old_number, new_number):
        '''
        Редагування телефонів
        '''
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
                return True
        return False

    def find_phone(self, phone_number):
        '''
        Пошук телефону
        '''
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        '''
        Додавання записів
        '''
        if isinstance(record, Record):
            self.data[record.name.value] = record

    def find(self, name):
        '''
        Пошук записів за іменем
        '''
        return self.data.get(name)

    def delete(self, name):
        '''
        Видалення записів за іменем
        '''
        if name in self.data:
            del self.data[name]

def main():
    '''
    Головна функція, де знаходиться логіка
    '''
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")


# Точка входу
if __name__ == "__main__":
    main()