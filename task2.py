# выислить площадь круга и прямоугольника!
def straightforward(a,b):
    a=int(input('Ведите сторону прямоугольника: '))
    b=int(input('Ведите сторону прямоугольника: '))
    s=a*b
    return s
def circle(r):
    p=3.14
    d=int(input('введите радиус круга: '))
    s2=p*d
    return s2
print(straightforward(2,4),':',circle(5))
