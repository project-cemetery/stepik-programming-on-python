def get_indexes(lst, item):
    indexes = []
    for i in range(len(lst)):
        if lst[i] == item:
            indexes.append(i)

    return sorted(indexes)


numbers = [int(i) for i in input().split()]
number = int(input())

positions = get_indexes(numbers, number)

if len(positions) > 0:
    for pos in positions:
        print(pos, end=' ')
else:
    print('Отсутствует')
