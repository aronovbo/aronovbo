объявление функции
def print_initials(name, surname, middlename):
    print(surname.capitalize(),' ', name[:1].capitalize(),'.', middlename[:1].capitalize(),'.',sep='')


считываем данные
name = input()
surname = input()
middlename = input()

# вызываем функцию
print_initials(name, surname, middlename)



