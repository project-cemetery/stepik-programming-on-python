def avg_by_dividable(data, divider):
    filtered_data = [x for x in data if x % divider == 0]

    return sum(filtered_data) / len(filtered_data)


numbers = range(int(input()), int(input()) + 1)
print(avg_by_dividable(numbers, 3))


