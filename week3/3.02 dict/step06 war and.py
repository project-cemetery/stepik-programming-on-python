from collections import Counter

cnt = Counter(input().lower().split())
for key in cnt:
    print(key, cnt[key])
