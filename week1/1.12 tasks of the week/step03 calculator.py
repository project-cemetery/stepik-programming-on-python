def calculate(a, b, op):
    result = 0

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == 'pow':
        result = a ** b
    elif op == '/':
        result = a / b
    elif op == 'mod':
        result = a % b
    elif op == 'div':
        result = a // b

    return result


try:
    print(calculate(float(input()), float(input()), input()))
except ZeroDivisionError as e:
    print('Деление на 0!')
