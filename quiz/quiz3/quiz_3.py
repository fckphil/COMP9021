# COMP9021 19T3 - Rachid Hamadi
# Quiz 3 *** Due Thursday Week 4


# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys
import numpy as np

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# INSERT YOUR CODE HERE

path = str('0' * nb_of_leading_zeroes + f'{int(code):o}')
nodes = []  # using a list to record which position has been visited
nodes.append((0, 0))  # adding the original node to the list


def switch(x, y):  # this function uses to switch on to off or off to on
    if (x, y) not in nodes:
        nodes.append((x, y))
    else:
        nodes.remove((x, y))


x, y = 0, 0
for i in path:
    if i == '0':  # move N
        y += 1
        switch(x, y)
    elif i == '1':  # move NE
        x += 1
        y += 1
        switch(x, y)
    elif i == '2':  # move E
        x += 1
        switch(x, y)
    elif i == '3':  # move SE
        x += 1
        y -= 1
        switch(x, y)
    elif i == '4':  # move S
        y -= 1
        switch(x, y)
    elif i == '5':  # move SW
        x -= 1
        y -= 1
        switch(x, y)
    elif i == '6':  # move W
        x -= 1
        switch(x, y)
    elif i == '7':  # move NW
        x -= 1
        y += 1
        switch(x, y)

if nodes:
    #print(nodes)
    max_x = nodes[0][0]
    max_y = nodes[0][1]
    min_x = max_x
    min_y = max_y
    for a in nodes:  # recording the bounds of the matrix
        if a[0] > max_x:
            max_x = a[0]
        elif a[0] < min_x:
            min_x = a[0]
        if a[1] > max_y:
            max_y = a[1]
        elif a[1] < min_y:
            min_y = a[1]
    #print(max_x, max_y, min_x, min_y)
    column = max_x - min_x + 1
    row = max_y - min_y + 1
    #print(row, column)
    matrix = np.zeros((row, column), dtype=int)  # create a row*column size matrix
    #print(matrix)
    for b in nodes:
        xx = b[0] - min_x
        yy = b[1] - min_y
        #print(xx, yy)
        matrix[yy][xx] = 1
    for m in matrix:  # mirror inversion
        for j in range(column // 2):
            m[j], m[column - 1 - j] = m[column - 1 - j], m[j]
    #print(matrix)
    for row in matrix:
        for column in row:
            if column == 0:
                print(off, end='')
            elif column == 1:
                print(on, end='')
        print()

else:  # if all the nodes on the situation 'off', then print nothing
    print()