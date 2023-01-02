import random
import string

n = (1024**2)*100  # 1 Mb of text
chars = ''.join([random.choice(string.ascii_letters) for i in range(n)])

with open('textfile.txt', 'w+') as f:
    f.write(chars) 