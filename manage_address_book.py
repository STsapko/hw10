from collections import UserDict

class Field:

    def __init__(self,value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    pass

class EMail(Field):
    pass


class Phone(Field):
    pass


class Record:

    def __init__(self, 
                 name: Name, 
                 email: EMail=None, 
                 phone: Phone=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone):
        self.phone = phone
        self.phones.append(phone)

    def change_phone(self, old_phone, new_phone):
        if old_phone.value in [ph.value for ph in self.phones]:
            self.phones = [ph if ph.value != old_phone.value else new_phone for ph in self.phones]
        if self.phone.value == old_phone.value:
            self.phone = new_phone

    def delete_phone(self, phone_to_del):
        if phone_to_del.value in [ph.value for ph in self.phones]:
            self.phones = [ph for ph in self.phones if ph.value != phone_to_del.value]
        if self.phone.value == phone_to_del.value:
            self.phone = None

    def add_email(self, email):
        self.email = email

    def change_email(self, new_email):
        self.email = new_email

    def delete_email(self):
        self.email = None

class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record


if __name__ == "__main__":
    pass
    name = Name('a')
    record = Record(name)
    record.add_phone(Phone(1))
    record.add_phone(Phone(2))
    record.add_phone(Phone(3))
    # print(record.name, record.phone, record.phones)
    record.delete_phone(Phone(1))
    # print(record.name, record.phone, record.phones)
    # print(Phone(1).value)
    # print([ph for ph in record.phones if ph.value != Phone(1).value])
    record.change_phone(Phone(3), Phone(4))
    print(record.name, record.phone, [ph.value for ph in record.phones])
