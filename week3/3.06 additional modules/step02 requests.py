import requests

with open('data/step02.txt', 'r') as f:
    url = f.readline().strip()

r = requests.get(url)

l = r.text.splitlines()
print(len(l))
