def lcm(a, b):
    c = a * b
    result = c

    while c > 0:
        if c % a == 0 and c % b == 0:
            result = c
        c -= 1

    return result


print(lcm(int(input()), int(input())))
