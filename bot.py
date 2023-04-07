# +del phone, change phone
# add/del/change email
# search by name, by phone, by email

from manage_address_book import AddressBook, Record, Name, Phone, EMail 
address_book = AddressBook()

def help(*args):
    return \
"""menu:
    hello
    add contact  (name phone* email*)
    add phone    (name phone)
    change phone (name phone new phone) 
    delete phone (name phone)
    add email    (name email)
    change email (name new email)
    delete email (name)
    search       (text or name and/or phone and/or)
    show all
    exit (exit, close, good bye)
    """

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "Give me name and phone please"
        except KeyError:
            return "No such name"
        except ValueError:
            return "Enter user name"
    return wrapper

def say_hello(*args):
    return 'How can I help you?'

def exit(*args):
    return 'Good bye!'

def no_command(*args):
    return "Unknown operation, try again."

@input_error
def add_contact(*args):
    list_of_params = args[0].split()
    name = Name(list_of_params[0])
    if len(list_of_params) < 2:
        phone = None
        email = None
    elif len(list_of_params) < 3:
        phone = Phone(list_of_params[1])
        email = None
    else:     
        phone = Phone(list_of_params[1])
        email = EMail(list_of_params[2])
    record = Record(name)
    if phone:
        record.add_phone(phone)
    if email:
        record.add_email(email)
    address_book.add_record(record) 
    return f"Contact {list_of_params[0]} added successfully"

@input_error
def add_phone(*args):
    list_of_params = args[0].split()
    name = Name(list_of_params[0])
    phone = Phone(list_of_params[1])
    contact: Record = address_book.get(name.value)
    if contact:
        contact.add_phone(phone)
        return f'Name: {name.value} tel {phone.value} is added'
    else:
        return f'No contact {name}'

@input_error
def delete_phone(*args):
    list_of_params = args[0].split()
    name = Name(list_of_params[0])
    phone = Phone(list_of_params[1])
    contact: Record = address_book.get(name.value)
    if contact:
        contact.delete_phone(phone)
        return f'Name: {name.value} tel {phone.value} is deleted'
    else:
        return f'No contact Name: {name.value}'

@input_error
def change_phone(*args):
    list_of_params = args[0].split()
    name = Name(list_of_params[0])
    old_phone = Phone(list_of_params[1])
    new_phone = Phone(list_of_params[2])
    contact: Record = address_book.get(name.value)
    if contact:
        contact.change_phone(old_phone, new_phone)
        return f'Name: {name.value} tel {old_phone.value} is changed to {new_phone.value}'
    else:
        return f'No contact {name}'

@input_error
def add_email(*args):
    list_of_params = args[0].split()
    name = Name(list_of_params[0])
    email = EMail(list_of_params[1])
    contact: Record = address_book.get(name.value)
    if contact:
        contact.add_email(email)
        return f'Name: {name.value} email {email.value} is added'
    else:
        return f'No contact {name}'
    
@input_error
def change_email(*args):
    list_of_params = args[0].split()
    name = Name(list_of_params[0])
    email = EMail(list_of_params[1])
    contact: Record = address_book.get(name.value)
    if contact:
        old_email = contact.email
        contact.change_email(email)
        return f'Name: {name.value} tel {old_email.value} is changed to {email.value}'
    else:
        return f'No contact {name}'

@input_error
def delete_email(*args):
    list_of_params = args[0].split()
    name = Name(list_of_params[0])
    contact: Record = address_book.get(name.value)
    if contact:
        old_email = contact.email
        contact.delete_email()
        return f'Name: {name.value} email {old_email.value} is deleted'
    else:
        return f'No contact {name}'

@input_error
def search(*args):
    list_of_params = args[0].split()
    search_text = list_of_params[0]
    result_list = []
    for field in list_of_params[1:]:
        for record in address_book.values():
            if field == 'name':
                if record.name.value == search_text:
                    result_list.append(record)
            if field == 'email':
                if record.email.value == search_text:
                    result_list.append(record)
            if field == 'phone':
                if record.phone.value == search_text or search_text in [ph.value for ph in record.phones]:
                    result_list.append(record)
    if result_list:
        result = ''
        for contact in set(result_list):
            result += f"Name: {contact.name}, phone: {contact.phone}, email: {contact.email}, phones: {[ph.value for ph in record.phones]}" +'\n'
        return f"Following contact(s) contain search: {search_text}" + '\n' + result
    return f'Search: {search_text} is not found'

def show_all_contacts(*args):
    result = ''
    for record in address_book.values():
        result += f"Name: {record.name}, phone: {record.phone}, email: {record.email}, phones: {[ph.value for ph in record.phones]}" +'\n'
    if not result:
        return 'No contacts yet'
    return result

OPERATIONS = {
    add_contact: 'add contact',
    add_phone: 'add phone',
    delete_phone: 'delete phone',
    change_phone: 'change phone',
    add_email: 'add email',
    delete_email: 'delete email',
    change_email: 'change email',
    search: 'search',
    show_all_contacts: 'show all',
    say_hello: 'hello',
    exit: ['exit', 'close','goodbye'],
}

def get_operation(text: str):
    for operation, kword in OPERATIONS.items():
        if type(kword) == str:
            if text.lower().startswith(kword):
                return operation, text[len(kword):].strip()
        if type(kword) == list:
            for k in kword:
                if text.startswith(k):
                    return operation, text[len(kword):].strip()
    return no_command, None
     
def main():
    print(help())
    while True:
        user_input = input('>>> ')
        operation, data = get_operation(user_input)
        print(operation(data))
        if operation == exit:
            break

if __name__ == '__main__':
    main()