from random import randint
def throw():
    k1=randint(1,6)
    k2=randint(1,6)
    rez=k1+k2
    return rez

outs={2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
for i in range (1,1001):
    result=throw()
    if result==2:
        outs[2]+=1
    elif result==3:
        outs[3]+=1
    elif result==4:
        outs[4]+=1
    elif result==5:
        outs[5]+=1
    elif result==6:
        outs[6]+=1
    elif result==7:
        outs[7]+=1
    elif result==8:
        outs[8]+=1
    elif result==9:
        outs[9]+=1
    elif result==10:
        outs[10]+=1
    elif result==11:
        outs[11]+=1
    elif result==12:
        outs[12]+=1

print(outs)
