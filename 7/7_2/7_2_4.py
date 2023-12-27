# объявление функции
def print_initials(name, surname, middlename):
    print(surname.lower().capitalize(), ' ', name[0].upper(), '.', middlename[0].upper(), '.', sep='')


# считываем данные
name = input()
surname = input()
middlename = input()

# вызываем функцию
print_initials(name, surname, middlename)
