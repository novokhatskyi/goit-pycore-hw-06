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
            if value.isdigit() and len(value) == 10:
                super().__init__(value)
            else:
                raise ValueError("Не правильний формат введення номеру, будь-ласка введіть номер з 10 цифр")
            

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def remove_phone (self, phone: Phone):
        # self.phones = list(filter(lambda p: p.value != phone.value, self.phones))
        new_phone = []
        for p in self.phones:
            if p.value != phone.value:
                new_phone.append(p)
                self.phones = new_phone
        return self.phones
    
    def edit_phone (self, old_phone: Phone, new_phone: Phone):
        for phone in self.phones:
            if phone.value == old_phone.value:
                self.phones.remove(phone)
                self.phones.append(new_phone)
                break
        return self.phones
    
    def search_phone (self, value):
        for phone in self.phones:
            if phone.value == value:
                return phone
        return None
         
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_name(self, name: str):
        return self.data.get(name)
    
    def dell_name(self, name: str):
        return self.data.pop(name)

if __name__ =="__main__":
    name_1 = Record("Oksana")
    name_1.add_phone(Phone("0973370717"))
    book = AddressBook()
    book.add_record(name_1)
    print(book.data["Oksana"])
    name_1.add_phone(Phone("1234567899"))
    print(book.data["Oksana"])
    name_2 = Record ("Oleksandr")
    name_2.add_phone(Phone("9876054321"))
    book.add_record(name_2)
    print(book)

