import requests

with open('data/step03.txt', 'r') as f:
    url = f.readline().strip()

folder = 'https://stepic.org/media/attachments/course67/3.6.3/'
text = ''

while text[:2] != 'We':
    r = requests.get(url)
    text = r.text
    url = folder + text
    print(text)

print('--------------')
print('Thats all. Check "output/step03.text')

with open('output/step03.txt', 'w') as f:
    f.write(text)


