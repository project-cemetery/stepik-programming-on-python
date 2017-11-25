d = int(input())
dic = set()

for i in range(d):
    dic.add(input().lower())

l = int(input())
lines = set()

for j in range(l):
    lines.add(input().lower())

words = list()

for line in lines:
    words.extend(line.split())

output = set()

for w in words:
    if w not in dic:
        output.add(w)

for w in output:
    print(w)
