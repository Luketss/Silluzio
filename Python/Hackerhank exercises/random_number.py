import random
from random import choice

# WIN BIG IN LOTO XD

a = [x for x in range(1, 59)]
numbers = []

for escolhas in range(6):
    selection = choice(a)
    numbers.append(selection)
print(sorted(numbers))
