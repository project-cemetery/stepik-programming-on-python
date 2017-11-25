def decompress(s):
    result = ''
    for i in range(len(s)):
        if not s[i].isdigit():
            j = i + 1
            cnt = ''
            while s[j].isdigit():
                cnt += s[j]
                if j + 1 < len(s):
                    j += 1
                else:
                    break
            cnt = int(cnt)
            result += s[i] * cnt
    return result


with open('data/step02.txt', 'r') as f:
    compressed_str = f.readline().strip()

s = decompress(compressed_str)
with open('output/step02.txt', 'w') as f:
    f.write(s)
