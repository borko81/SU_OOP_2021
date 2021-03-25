from itertools import zip_longest

l_1 = [1, 2]
l_2 = [1, 2, 3]

print(list(zip_longest(l_1, l_2, fillvalue='_')))