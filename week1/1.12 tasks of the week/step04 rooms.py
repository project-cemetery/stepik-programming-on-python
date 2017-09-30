def get_circle_area(r):
    return 3.14 * (r ** 2)


def get_triangle_area(a, b, c):
    p = (a + b + c) / 2

    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def get_rectangle_area(a, b):
    return a * b


form = input()

area = 0

if form == 'треугольник':
    area = get_triangle_area(float(input()), float(input()), float(input()))
elif form == 'прямоугольник':
    area = get_rectangle_area(float(input()), float(input()))
elif form == 'круг':
    area = get_circle_area(float(input()))

print(area)
