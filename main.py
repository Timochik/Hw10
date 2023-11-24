from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        # Валідація номера телефону (10 цифр)
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        # Додавання телефону до запису
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        result = self.find_phone(phone)
        if result:
            self.phones.remove(result)
            return self.phones

    def edit_phone(self, old_phone, new_phone):
        # Редагування телефону у запису
        new_phone_obj = Phone(new_phone)
        for idx, p in enumerate(self.phones):
            if p.value == old_phone:
                # Заміна старого телефону на новий
                self.phones[idx] = new_phone_obj
                return
        # Якщо телефон не знайдено, викидаємо виключення
        raise ValueError(f"Phone {old_phone} not found in the record")


    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        # Перевизначення методу для виведення запису
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        # Додавання запису до адресної книги
        self.data[record.name.value] = record

    def find(self, name):
        # Пошук запису за ім'ям
        return self.data.get(name)

    def delete(self, name):
        # Видалення запису за ім'ям
        if name in self.data:
            del self.data[name]