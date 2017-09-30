numbers = []

while True:
    x = int(input())
    numbers.append(x)
    if x == 0:
        break

print(sum(numbers))
