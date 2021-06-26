init_str=input('Введите строку: ')
sum_num=0
for num in init_str:
    if num.isdigit():
        sum_num+=int(num)
print('Сумма цифр в строке равна: ',sum_num)
        
