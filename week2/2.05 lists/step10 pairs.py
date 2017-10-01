def get_sum_pairs(data):
    return [data[i - 1] + data[(i + 1) % len(data)] for i in range(len(data))] if len(data) > 1 else data[0]


for param in get_sum_pairs([int(x) for x in input().strip().split()]):
    print(param, end=' ')
