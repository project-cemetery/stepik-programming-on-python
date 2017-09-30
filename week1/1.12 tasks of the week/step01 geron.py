def get_triangle_area_by_geron(a, b, c):
    p = (a + b + c) / 2

    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


print(get_triangle_area_by_geron(int(input()), int(input()), int(input())))
