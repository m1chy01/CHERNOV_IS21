#вариант 24. описать функцию RectPS(x1, x2, y1, y2, P, S), вычисляющую периметр P и площадь S прямоугольника со сторонами,
#параллельными осям координат, по координатам (x1, y1), (x2, y2) его противоположных вершин (x1, x2, y1, y2 - входные, P и S - выходные параметры
#вещественного типа). с помощью этой функции найти периметры и площади трех прямоугольников с данными противоположными вершинам.

def RectPS(x1,y1,x2,y2,Result):
    a = abs(x1-x2)
    b = abs(y1-y2)
    print("a = ", a)
    print("b = ", b)
    Result['P'] = 2*(a+b)
    Result['S'] = a*b
    return

x1, x2 = int(input("введите 1 число:")), int(input("введите 2 число:"))
y1, y2 = int(input("введите 3 число:")), int(input("введите 4 число:"))
R = {'P' : None, 'S' : None}
RectPS(x1,y1,x2,y2,R)
print('P = ', R['P'])
print('S = ', R['S'])