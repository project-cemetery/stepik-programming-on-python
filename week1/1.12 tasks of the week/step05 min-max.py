def get_max_min_middle(data):
    sorted_data = sorted(data)

    return sorted_data[2], sorted_data[0], sorted_data[1]


for param in get_max_min_middle(int(input()) for _ in range(3)):
    print(param)
