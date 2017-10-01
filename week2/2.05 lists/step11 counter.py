from collections import Counter


def get_repetitive_items(items):
    cnt = Counter(items)

    return [x for x in cnt if cnt[x] > 1]


print(' '.join([str(x) for x in get_repetitive_items([int(i) for i in input().split()])]))
