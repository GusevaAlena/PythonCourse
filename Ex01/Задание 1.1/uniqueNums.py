def isUnique(n):
    c=str(n)
    if (c[0]!=c[1] and c[0]!=c[2] and c[0]!=c[3]) and (c[1]!=c[2] and c[1]!=c[3]) and c[2]!=c[3]:
        return True
    return False

num_list=range(1000,10000)
for num in num_list:
    if isUnique(num)==True:
        print(num)
