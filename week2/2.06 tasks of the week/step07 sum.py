numbers = [int(input())]
while sum(numbers) != 0:
    numbers.append(int(input()))

print(sum([x**2 for x in numbers]))
