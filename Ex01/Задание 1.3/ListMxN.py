m=int(input('Введите значение m: '))
n=int(input('Введите значение n: '))

for x in range(1,m+1):
    print('\t')
    for y in range(1,n+1):
        print(x**y,end='\t')
