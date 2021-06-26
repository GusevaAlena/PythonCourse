
Xa=float(input('Введите координату вершины А по оси Х: '))
Ya=float(input('Введите координату вершины А по оси Y: '))
Xb=float(input('Введите координату вершины B по оси Х: '))
Yb=float(input('Введите координату вершины B по оси Y: '))
Xc=float(input('Введите координату вершины C по оси Х: '))
Yc=float(input('Введите координату вершины C по оси Y: '))
Xd=float(input('Введите координату вершины D по оси Х: '))
Yd=float(input('Введите координату вершины D по оси Y: '))
Xe=float(input('Введите координату вершины E по оси Х: '))
Ye=float(input('Введите координату вершины E по оси Y: '))

def CalcLength (x1,x2,y1,y2):
    l=((x1-x2)**2+(y1-y2)**2)**0.5
    return l

def CalcSquare (l1,l2,l3):
    p=(l1+l2+l3)/2
    s=(p*(p-l1)*(p-l2)*(p-l3))**0.5
    return s

lab=CalcLength(Xa,Xb,Ya,Yb)
lbc=CalcLength(Xb,Xc,Yb,Yc)
lac=CalcLength(Xa,Xc,Ya,Yc)
lcd=CalcLength(Xc,Xd,Yc,Yd)
lad=CalcLength(Xa,Xd,Ya,Yd)
lde=CalcLength(Xd,Xe,Yd,Ye)
lae=CalcLength(Xa,Xe,Ya,Ye)

Sabc=CalcSquare(lab,lbc,lac)
Sacd=CalcSquare(lac,lcd,lad)
Saed=CalcSquare(lae,lde,lad)

Spent=Sabc+Sacd+Saed
Spent=float('{:.2f}'.format(Spent))
print(f'Площадь пятиугольника равна {Spent}')

