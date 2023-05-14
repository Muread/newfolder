import random
import string

N = 2000000
table = [[random.random() for j in range(4)] for i in range(N)]

letters = string.ascii_lowercase[:5]
for row in table:
    row.append(random.choice(letters))

subset = [row for row in table if row[-1] in letters]
print(subset)