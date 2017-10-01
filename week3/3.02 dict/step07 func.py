result = {}
for i in range(int(input())):
    x = int(input())
    if x not in result.keys():
        result[x] = f(x)
    print(result[x])
