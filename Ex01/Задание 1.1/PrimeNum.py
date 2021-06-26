def isPrime(number):
    if number==1:return False
    for num in range(2,int(number**0.5)+1):
        if number%num==0:
            return False
    return True

low_num=int(input('Введите нижнюю границу диапазона: '))
high_num=int(input('Введите верхнюю границу диапазона: '))
num_list=range(low_num,high_num+1)
for n in num_list:
    if isPrime(n):
        print(n)

