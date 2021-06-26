def factorial(n):
    n=int(n)
    if n<0:
        raise Exception('Число должно быть положительным')
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
user_input = input('Введите число: ')
print(f'Факториал от {user_input} равен {factorial(user_input)}')
