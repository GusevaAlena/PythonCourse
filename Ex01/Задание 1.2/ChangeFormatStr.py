init_string=input('Введите строку в формате "Фамилия Имя Отчество": ')
splitted_string=init_string.split()
surname=splitted_string[0]
name_let=splitted_string[1][:1]
patr_let=splitted_string[2][:1]
print(f'{surname} {name_let}.{patr_let}.')
