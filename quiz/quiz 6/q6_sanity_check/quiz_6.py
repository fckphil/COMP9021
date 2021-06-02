# COMP9021 19T3 - Rachid Hamadi
# Quiz 6 *** Due Thursday Week 8
#
# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 



def size_of_largest_parallelogram():
    size = get_max()
    return size



# POSSIBLY DEFINE OTHER FUNCTIONS


try:

    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                              ).split()
                    )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]

def make_grid():
    l_grid = [x[:] for x in grid]
    m_grid = [x[:] for x in grid]
    r_grid = [x[:] for x in grid]
    for i in range(10):
        for j in range(10):
                if i > 0 and m_grid[i][j]:
                    if m_grid[i-1][j]:
                        m_grid[i][j] += m_grid[i - 1][j]
                    if j > 0 and r_grid[i-1][j-1]:
                        r_grid[i][j] += r_grid[i - 1][j - 1]
                    if j + 1 < 9 and l_grid[i-1][j+1]:
                        l_grid[i][j] += l_grid[i - 1][j + 1]
    return m_grid, r_grid, l_grid

def max_area1():
    set1 = []
    m_grid, r_grid, l_grid = make_grid()

    for i in range(1,10):
        c = int(100)
        for j in range(10):
            k = j
            while j < 10:
                if m_grid[i][j] >1:
                    a = m_grid[i][j]
                    if j+1 < 10:
                        j+=1
                        b = m_grid[i][j]
                        if m_grid[i][j] > 1 and j-1 < 9:
                            c = min(a,b,c)
                            d = abs(j - k +1)
                        else:
                            c = min(a,c)
                            d = abs(j- 1 - k + 1)  #length
                        if d >= 2:
                            area = d*c
                            set1.append(area)
                    else:
                        break
                else:
                    j += 1
                    k = j
            else: break
    x = max(set1)
    return x

def max_area2():
    set2 = []
    m_grid, r_grid, l_grid = make_grid()

    for i in range(1,10):
        c = int(100)
        for j in range(10):
            k = j
            while j < 10:
                if r_grid[i][j] >1:
                    a = r_grid[i][j]
                    if j+1 < 10:
                        j+=1
                        b = r_grid[i][j]
                        if r_grid[i][j] > 1 and j-1 < 9:
                            c = min(a,b,c)
                            d = abs(j - k +1)
                        else:
                            c = min(a,c)
                            d = abs(j- 1 - k + 1)  #length
                        if d >= 2:
                            area = d*c
                            set2.append(area)
                    else:
                        break
                else:
                    j += 1
                    k = j
            else:
                break
    y = max(set2)
    return b


def max_area3():


    set3 = []
    m_grid, r_grid, l_grid = make_grid()

    for i in range(10):
        c = int(100)
        for j in range(10):
            k = j
            while j < 10:
                if l_grid[i][j] >1:
                    a = l_grid[i][j]
                    if j+1 < 10:
                        j+=1
                        b = l_grid[i][j]
                        if l_grid[i][j] > 1 and j-1 < 9:
                            c = min(a,b,c)
                            d = abs(j - k +1)
                        else:
                            c = min(a,c)
                            d = abs(j- 1 - k + 1)  #length
                        if d >= 2:
                            area = d*c
                            set3.append(area)
                    else:
                        break
                else:
                    j += 1
                    k = j
            else: break
    z = max(set3)
    return c

def get_max():
    x = max_area1()
    y = max_area2()
    z = max_area3()
    d = max(x,y,z)
    return d





print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
         )
else:
    print('There is no parallelogram with horizontal sides.')

