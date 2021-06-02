# COMP9021 19T3 - Rachid Hamadi
# Quiz 7 *** Due Thursday Week 9
#
# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out"
# (has exactly one neighbour in the shape).

from collections import defaultdict
from random import seed, randrange
import sys



dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s
# that make it with 2. We "colour" the second shape we find by
# replacing all the 1s that make it with 3.
def find(i,j,colour):
    if i in range(10) and j in range(10) and grid[i][j] == 1:
        grid[i][j] = colour
        for x,y in [(0,1), (0,-1), (1,0), (-1,0)]:      # direction: East, West, North, South
            find(i+x, j+y, colour)
# print(grid)


def colour_shapes():
    # pass
    # Replace pass above with your code
    colour = 2
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 1:
                find(i,j,colour)
                colour = colour + 1

    return colour



def max_number_of_spikes(nb_of_shapes):
    dict = defaultdict(int)
    for x in range(10):
        for y in range(10):
            if grid[x][y] != 0:
                count = 0
                for(a,b) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # direction: East, West, North, South
                    a_x = x+a
                    a_y = y+b
                    if a_x in range(10) and a_y in range(10) and grid[a_x][a_y] == grid[x][y]:
                        count += 1
                    else:
                        continue
                if count == 1:
                    dict[grid[x][y]] = dict[grid[x][y]] + 1
    if dict.values():
         return max(dict.values())
    else:
        return 0



# Possibly define other functions here    


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
print('Here is the grid that has been generated:')
display_grid()
nb_of_shapes = colour_shapes()
print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(nb_of_shapes)
     )
