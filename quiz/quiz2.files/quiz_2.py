# COMP9021 19T3 - Rachid Hamadi
# Quiz 2 *** Due Thursday Week 3


import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE HERE
############# reversed_dict_per_length
rever_dic = {}
for k, v in mapping.items():
    if v not in rever_dic:
        rever_dic[v]= [k]
    else:
        rever_dic[v].append(k)

for k1, v1 in rever_dic.items():
    len_v1 = len(v1)
    if len_v1 not in reversed_dict_per_length:
        reversed_dict_per_length[len_v1]= {}
        reversed_dict_per_length[len_v1][k1] = v1
    else:
        reversed_dict_per_length[len_v1][k1] = v1
################################ cycles
def cycle_func(d):
    while d:
        # Keep track of keys we've iterated through in this loop
        tracked = []
        # Take the next available key
        k = next(iter(d))
        while True:
            tracked.append(k)
            # print(tracked)
            # This key (the value of the previous key) must have already
            # been deleted, meaning it was part of a cycle or lead to
            # repetitions of an already discovered cycle
            try:
                v = d[k]
            except KeyError:
                for t in tracked:
                    if t in d:
                        del d[t]
                break
            if v in tracked:
                cycle = tracked[tracked.index(v):]
                cycles.append(cycle)
                for c in cycle:
                    del d[c]
                break
            if any(v in cycle for cycle in cycles):
                for t in tracked:
                    del d[t]
                break
            # Set the next key
            k = v
dic2 = mapping
cycle_func(dic2)


print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)


