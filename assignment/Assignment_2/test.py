import copy
import sys
#array = [[1,0,2,2,1,2,3,0],[3,2,2,1,2,0,2,2],[3,0,1,1,3,1,0,0],[2,0,3,0,0,1,2,0],[3,2,2,0,1,2,3,2],[1,0,0,1,1,0,0,0]]
array = [[0,2,2,3,0,2,1,2,0,2,2,2],[2,2,2,2,2,3,1,1,1,0,3,2],[3,0,1,3,2,2,1,3,0,3,0,2],[3,1,2,3,2,2,2,3,2,3,3,0],\
         [0,0,1,0,0,0,1,0,0,0,0,0]]
# def gate(array):
#     array = array
#     count = 0
#     for j in range(len(array[0])):
#         if array[0][j] == 0 or array[0][j] == 2:
#             count += 1
#         if array[-1][j] != 1:
#             count += 1
#     for i in range(len(array)):
#         if array[i][0] == 0 or array[i][0] == 1:
#             count += 1
#         if array[i][-1] != 2:
#             count += 1
#     count = count - 4
#     print(count)
#
def find(new_array,i,j,colour):
    if i in range(len(new_array)) and j in range(len(new_array[0])) and new_array[i][j] == 1:
        new_array[i][j] = colour
        for x,y in [(0,1), (0,-1), (1,0), (-1,0)]:
            find(new_array,i+x,j+y,colour)


def decode_maze():
    new_array = [[0] * (len(array[0]) * 2 - 1) for _ in range(len(array) * 2 - 1)]
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == 0:
                pass
            elif array[i][j] == 1:
                new_array[i * 2][j * 2] = new_array[i * 2][j * 2 + 1] = new_array[i * 2][j * 2 + 2] = 1
            elif array[i][j] == 2:
                new_array[i * 2][j * 2] = new_array[i * 2 + 1][j * 2] = new_array[i * 2 + 2][j * 2] = 1
            elif array[i][j] == 3:
                new_array[i * 2][j * 2] = new_array[i * 2 + 1][j * 2] = \
                    new_array[i * 2][j * 2 + 1] = new_array[i * 2 + 2][j * 2] = new_array[i * 2][j * 2 + 2] = 1
    return new_array


def wall():
    new_array = decode_maze()
    colour = 4
    for i in range(len(new_array)):
        for j in range(len(new_array[0])):
            if new_array[i][j] == 1:
                find(new_array, i, j, colour)
                colour += 1
    set_of_wall = colour - 4
    if set_of_wall == 0:
        print('The maze has no wall.')
    elif set_of_wall == 1:
        print('The maze has walls that are all connected.')
    else:
        print(f'The maze has {set_of_wall} sets of walls that are all connected.')

wall()

