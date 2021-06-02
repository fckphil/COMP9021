from itertools import permutations
from itertools import combinations
import numpy as np
result = ''
word = 'aabbcc'
result = word[0]
item = []
list2 = []
list3 = []
final = []
for i in word[1:]:
    if i != result[-1]:
        result += i
# print(result)  = abc
for i in range(len(result)+1):
    a = result[i:]
    print(a)
    for j in range(1,len(a)+1):
        b = a[0]
        list1 = permutations(a, j)
        list2.append(list(list1))
        for row in list2:
            for char in row:
                if char[0] == b:
                    item.append(''.join(char))
    list2 = []
print(item)
for i in item:
    if i not in final:
        final.append(i)
final = sorted(final)
print(final)





