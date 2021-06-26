name=input('Введите имя: ')
male=input('Введите пол (м или ж): ')
age=int(input('Введите возраст: '))
if male=='м':
    if (age==1)or(age/10>1 and age%10==1):
        print(f'Его зовут {name}. Ему {age} год')
    elif (age==2 or age==3 or age==4) or (age/10>1 and (age%10==2 or age%10==3 or age%10==4)):
        print(f'Его зовут {name}. Ему {age} года')
    else:
        print(f'Его зовут {name}. Ему {age} лет')
elif male=='ж':
    if (age==1)or(age/10>1 and age%10==1):
        print(f'Её зовут {name}. Ей {age} год')
    elif (age==2 or age==3 or age==4) or (age/10>1 and (age%10==2 or age%10==3 or age%10==4)):
        print(f'Её зовут {name}. Ей {age} года')
    else:
        print(f'Её зовут {name}. Ей {age} лет')
    

