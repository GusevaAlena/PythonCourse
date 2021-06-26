def romanTOarabic(roman):
    digit = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    arabic = 0
    for d in range(len(roman)):
        try:
            if digit[roman[d]]<digit[roman[d+1]]:
                arabic-=digit[roman[d]]
            else:
                arabic+=digit[roman[d]]
        except IndexError:
            arabic+=digit[roman[d]]
    return arabic

user_input=input('Введите римское число: ')
rom=user_input.upper()
arabic=romanTOarabic(rom)
print(f'Арабское число {arabic}')
