def get_strange_sequence(length):
    sequence = []
    for i in range(1, length + 1):
        for j in range(i):
            sequence.append(i)
            if len(sequence) == length:
                break
        else:
            continue
        break

    return sequence


for param in get_strange_sequence(int(input())):
    print(param, end=' ')
