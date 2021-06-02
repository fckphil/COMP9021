# COMP9021 19T3 - Rachid Hamadi
# Assignment 2 *** Due Sunday Week 10


# IMPORT ANY REQUIRED MODULE
import sys
import copy
from pprint import pprint
import csv
from maze import *

def make_array():
    b = []
    with open('maze_1.txt') as txt_file:
        for line in txt_file:
            if not line.isspace():
                b.append(list("".join(line.split())))
    a = []
    for each in b:
        each_line=list(map(lambda x: int(x), each))
        a.append(each_line)
    return a

def decode_maze():
    array = make_array()
    new_array = [[0] * (len(array[0])*2 -1) for _ in range(len(array)*2-1)]
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


def find(new_array,i,j,colour):
    if i in range(len(new_array)) and j in range(len(new_array[0])) and new_array[i][j] == 1:
        new_array[i][j] = colour
        for x,y in [(0,1), (0,-1), (1,0), (-1,0)]:
            find(new_array,i+x,j+y,colour)


class MazeError(Exception):
    def __init__(self, message):
        self.message = message


class Maze():
    def __init__(self, filename):
        self.filename = filename
        try:
            file = open(self.filename)
            self.original_files = file
        except FileNotFoundError:
            raise MazeError('Incorrect input.')

    def check_maze(self):
        code = self.original_files.readlines()
        new_code=[]
        for i in code:
            i = i.strip('\n')
            new_code.append(i.replace(' ', ''))
        row = []
        array = []
        for i in range(len(new_code)):
            for j in range(len(new_code[i])):
                if new_code[i][j] not in ('0', '1', '2', '3'):
                    raise MazeError('Incorrect input.')
                else:
                    row.append(int(new_code[i][j]))
            if len(row):
                array.append(row)
            row = []
        if 2 <= len(array) <= 41 and 2 <= len(array[0]) <= 31:
            k = len(array[0])
            for i in range(len(array)):
                if len(array[i]) != k:
                    raise MazeError('Incorrect input')
                for j in range(len(array[0])):
                    if i + 1 >= len(array):
                        if array[i][j] in range(2,4):
                            raise MazeError('Input does not represent a maze.')
                    if j + 1 >= len(array[0]):
                        if str(array[i][j]) in ('1', '3'):
                            raise MazeError('Input does not represent a maze.')
        else:
            raise MazeError('Incorrect input.')
        return array



    def gate(self):
        array = make_array()
        count = 0
        for j in range(len(array[0])):
            if array[0][j] == 0 or array[0][j] == 2:
                count += 1
            if array[-1][j] != 1:
                count += 1
        for i in range(len(array)):
            if array[i][0] == 0 or array[i][0] == 1:
                count += 1
            if array[i][-1] != 2:
                count += 1
        count = count - 4
        if count == 0:
            print('The maze has no gate.')
        elif count == 1:
            print('The maze has a single gate.')
        else:
            print(f'The maze has {count} gates.')


    def wall(self):
        new_array = decode_maze()
        colour = 4
        for i in range(len(new_array)):
            for j in range(len(new_array[0])):
                if new_array[i][j] == 1:
                    find(new_array,i,j,colour)
                    colour += 1
        set_of_wall = colour - 4
        if set_of_wall == 0:
            print('The maze has no wall.')
        elif set_of_wall == 1:
            print('The maze has walls that are all connected.')
        else:
            print(f'The maze has {set_of_wall} sets of walls that are all connected.')
        return set_of_wall



    def analyse(self):
        pass
        # REPLACE PASS ABOVE WITH YOUR CODE


    def display(self):
        pass
        # REPLACE PASS ABOVE WITH YOUR CODE

maze = Maze('some_filename')
maze.gate()
maze.wall()
