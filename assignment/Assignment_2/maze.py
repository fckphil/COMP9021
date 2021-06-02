import sys
import copy
from maze import *
sys.setrecursionlimit(10000)


def explor(list, x, y, m, list2):
    if not (0 <= x < len(list)) or not (0 <= y < len(list[0])):
        return
    if list[x][y] in m:
        return
    else:
        list2.append([x, y])
    list[x][y] = m[0]
    explor(list, x + 1, y, m, list2)
    explor(list, x, y + 1, m, list2)
    explor(list, x - 1, y, m, list2)
    explor(list, x, y - 1, m, list2)


def no_back(list, dot, pool):
    x, y = dot
    if 1 <= x < len(list) - 1 and 1 <= y < len(list[0]) - 1:
        if list[x][y] != 0:
            return
        if int(list[x + 1][y] != 0) + int(list[x - 1][y] != 0) + int(list[x][y + 1] != 0) + int(
                list[x][y - 1] != 0) == 3:
            list[x][y] = 6
            no_back(list, (x + 1, y), pool)
            no_back(list, (x - 1, y), pool)
            no_back(list, (x, y + 1), pool)
            no_back(list, (x, y - 1), pool)
            pool.append((x, y))
        else:
            return
    elif x == 0 or y == 0 or x == len(list) - 1 or y == len(list[0]) - 1:
        if list[x][y] == 0:
            list[x][y] = 6
            pool.append((x, y))


class MazeError(Exception):
    def __init__(self, err):
        Exception.__init__(self, err)


class Maze():
    def __init__(self, filename):
        self.filename = filename
        try:
            file = open(self.filename)
            self.original_files = file
        except FileNotFoundError:
            raise MazeError('Incorrect input.')
        self.check_maze()
        # self.pre_check()
        self.decode_maze()
        self.pillars()
        self.maze_wall_num()
        self.maze_area()
        self.maze_gate()
        self.maze_inaccessible_areas()
        self.maze_blocker()
        self.maze_path()
        self.draw_path()

    def check_maze(self):
        code = self.original_files.readlines()
        line = []
        code_list = []
        for i in range(len(code)):
            for j in range(len(code[i])):
                if code[i][j] == ' ' or code[i][j] == '\n':
                    continue
                elif code[i][j] not in ('0', '1', '2', '3'):
                    raise MazeError('Incorrect input.')
                else:
                    line.append(int(code[i][j]))
            if len(line) != 0:
                code_list.append(line)
            line = []

        lenght = len(code_list[0])
        if not (2 <= len(code_list) <= 41) or not (2 <= lenght <= 31):
            raise MazeError('Incorrect input.')
        for i in range(len(code_list)):
            if len(code_list[i]) != lenght:
                raise MazeError('Incorrect input.')
            for j in range(len(code_list[i])):
                if i == len(code_list) - 1:
                    if code_list[i][j] == 2 or code_list[i][j] == 3:
                        raise MazeError('Input does not represent a maze.')
                if j == len(code_list[i]) - 1:
                    if code_list[i][j] == 1 or code_list[i][j] == 3:
                        raise MazeError('Input does not represent a maze.')

        self.code_list = code_list

    def decode_maze(self):
        code_list = self.code_list
        maze_map = [[0] * (len(code_list[0]) * 2 - 1) for _ in range(len(code_list) * 2 - 1)]
        for i in range(len(code_list)):
            for j in range(len(code_list[0])):
                if code_list[i][j] == 0:
                    pass
                elif code_list[i][j] == 1:
                    maze_map[i * 2][j * 2] = maze_map[i * 2][j * 2 + 1] = maze_map[i * 2][j * 2 + 2] = 1
                elif code_list[i][j] == 2:
                    maze_map[i * 2][j * 2] = maze_map[i * 2 + 1][j * 2] = maze_map[i * 2 + 2][j * 2] = 1
                elif code_list[i][j] == 3:
                    maze_map[i * 2][j * 2] = maze_map[i * 2 + 1][j * 2] = maze_map[i * 2][j * 2 + 1] = \
                        maze_map[i * 2 + 2][j * 2] = maze_map[i * 2][j * 2 + 2] = 1
        from pprint import pprint
        self.maze_map = copy.deepcopy(maze_map)

    def maze_wall_num(self):
        maze1 = copy.deepcopy(self.maze_map)
        count = 0
        for i in range(len(maze1)):
            for j in range(len(maze1[0])):
                if maze1[i][j] == 1:
                    explor(maze1, i, j, [0], [])
                    count += 1
        self.wall_num_list = count
        print()

    def maze_area(self):
        maze1 = copy.deepcopy(self.maze_map)
        area_num_list = []
        for i in range(len(maze1)):
            for j in range(len(maze1[0])):
                pool = []
                if maze1[i][j] == 0:
                    explor(maze1, i, j, [1], pool)
                    area_num_list.append(pool)
        while [] in area_num_list:
            area_num_list.remove([])
        self.area_num_list = area_num_list

    def maze_gate(self):
        maze1 = copy.deepcopy(self.maze_map)
        gate_list = []
        for i in range(len(maze1)):
            for j in range(len(maze1[1])):
                if maze1[i][j] == 0:
                    if i == 0 or i == len(maze1) - 1:
                        if j % 2 == 1:
                            gate_list.append([i, j])
                    if j == 0 or j == len(maze1[i]) - 1:
                        if i % 2 == 1:
                            gate_list.append([i, j])
        self.gate_list = gate_list
        return gate_list

    def maze_inaccessible_areas(self):
        area_list = self.area_num_list
        inacc = []
        path = []
        for i in range(len(area_list)):
            count = 0
            for j in range(len(area_list[i])):
                x, y = area_list[i][j]
                if x == 0 or y == 0 or y == (len(self.maze_map[0]) - 1) or x == (len(self.maze_map) - 1):
                    if x % 2 == 0 and y % 2 == 0:
                        continue
                    else:
                        count += 1
            if count == 0:
                inacc.append(area_list[i])
            elif count == 2:
                path.append(area_list[i])
        self.inacc = inacc
        self.possible_path = path

    def maze_blocker(self):
        inacc = copy.deepcopy(self.inacc)
        maze1 = copy.deepcopy(self.maze_map)
        block_list = []
        temp = []
        for i in inacc:
            for j in i:
                temp.append(j)

        for i in range(1, len(maze1) - 1):
            for j in range(1, len(maze1[0]) - 1):
                x, y = i, j
                if [i, j] in temp:
                    continue
                if int(maze1[x + 1][y] != 0) + int(maze1[x - 1][y] != 0) + int(maze1[x][y + 1] != 0) + int(
                        maze1[x][y - 1] != 0) == 3:
                    no_back(maze1, (x, y), block_list)
        self.block_list = copy.deepcopy(block_list)
        self.maze_with_block = copy.deepcopy(maze1)
        final = []
        count = 0
        for i in range(len(block_list)):
            x, y = block_list[i]
            if maze1[x][y] == 6:
                explor(maze1, x, y, [0, 1], final)
                count += 1
        self.blocker_num = count

    def pillars(self):
        maze1 = copy.deepcopy(self.code_list)
        pillars = []
        for i in range(len(maze1)):
            for j in range(len(maze1[i])):
                if maze1[i][j] == 0:
                    if i == 0 and j == 0:
                        pillars.append([i, j])
                    elif i == 0 and maze1[i][j - 1] in (0, 2):
                        pillars.append([i, j])
                    elif j == 0 and maze1[i - 1][j] in (0, 1):
                        pillars.append([i, j])
                    elif maze1[i][j - 1] in (0, 2) and maze1[i - 1][j] in (0, 1):
                        pillars.append([i, j])
        self.pillar_list = copy.deepcopy(pillars)

    def maze_path(self):
        maze1 = copy.deepcopy(self.maze_with_block)
        possible_path = copy.deepcopy(self.possible_path)
        pillar = self.pillar_list
        for i in pillar:
            x, y = i
            maze1[x * 2][y * 2] = 1
        for i in range(len(possible_path)):
            temp = []
            for j in range(len(possible_path[i])):
                x, y = possible_path[i][j]
                if maze1[x][y] == 0:
                    temp.append(possible_path[i][j])
            possible_path[i] = temp

        def check_status(maze1, x, y):
            count = 0
            if x == 0 or x == len(maze1) - 1:
                count = int(maze1[x][y + 1] != 0) + int(maze1[x][y - 1] != 0)
            elif y == 0 or y == len(maze1[0]) - 1:
                count = int(maze1[x + 1][y] != 0) + int(maze1[x - 1][y] != 0)
            else:
                count = int(maze1[x + 1][y] != 0) + int(maze1[x - 1][y] != 0) + int(maze1[x][y + 1] != 0) + int(
                    maze1[x][y - 1] != 0)
            if count == 2:
                return True
            else:
                return False

        final_path1 = []

        for i in range(len(possible_path)):
            a = 1
            for j in range(1, len(possible_path[i]) - 1):
                x, y = possible_path[i][j]
                a = a * int(check_status(maze1, x, y))
            if a == 1:
                final_path1.append(possible_path[i])
        self.final_path = final_path1

    def analyse(self):
        gates = len(self.gate_list)
        wall = self.wall_num_list
        areas = len(self.area_num_list) - len(self.inacc)
        aa = self.inacc
        inaccessible_areas = 0
        for i in range(len(aa)):
            for j in range(len(aa[i])):
                x, y = aa[i][j]
                if x % 2 == 1 and y % 2 == 1:
                    inaccessible_areas += 1
        blocker = self.blocker_num
        path = len(self.final_path)

        if not gates:
            print('The maze has no gate.')
        elif gates == 1:
            print('The maze has a single gate.')
        else:
            print(f'The maze has {gates} gates.')

        if not wall:
            print('The maze has no wall.')
        elif wall == 1:
            print('The maze has walls that are all connected.')
        else:
            print(f'The maze has {wall} sets of walls that are all connected.')

        if not inaccessible_areas:
            print('The maze has no inaccessible inner point.')
        elif inaccessible_areas == 1:
            print('The maze has a unique inaccessible inner point.')
        else:
            print(f'The maze has {inaccessible_areas} inaccessible inner points.')

        if not areas:
            print('The maze has no accessible area.')
        elif areas == 1:
            print('The maze has a unique accessible area.')
        else:
            print(f'The maze has {areas} accessible areas.')

        if not blocker:
            print('The maze has no accessible cul-de-sac.')
        elif blocker == 1:
            print('The maze has accessible cul-de-sacs that are all connected.')
        else:
            print(f'The maze has {blocker} sets of accessible cul-de-sacs that are all connected.')

        if not path:
            print('The maze has no entry-exit path with no intersection not to cul-de-sacs.')
        elif path == 1:
            print('The maze has a unique entry-exit path with no intersection not to cul-de-sacs.')
        else:
            print(f'The maze has {path} entry-exit paths with no intersections not to cul-de-sacs.')
        return self.maze_map

    def draw_maze_wall(self):
        maze1 = copy.deepcopy(self.code_list)
        maze2 = copy.deepcopy(maze1)
        wall_list = []
        for i in range(len(maze1)):
            for j in range(len(maze1[0])):
                a = j
                while maze1[i][a] == 1 or maze1[i][a] == 3:
                    maze1[i][a] = 0
                    a += 1
                if a - j >= 1:
                    draw = [(j, i), (a, i)]
                    wall_list.append(draw)
        for i in range(len(maze2[0])):
            for j in range(len(maze2)):
                a = j
                while maze2[a][i] == 2 or maze2[a][i] == 3:
                    maze2[a][i] = 0
                    a += 1
                if a - j >= 1:
                    draw = [(i, j), (i, a)]
                    wall_list.append(draw)
        return wall_list

    def draw_path(self):
        temp_path = copy.deepcopy(self.final_path)
        maze1 = copy.deepcopy(self.maze_map)
        # 这一步是在干什么锤子
        for i in range(len(temp_path)):
            for j in range(len(temp_path[i])):
                x, y = temp_path[i][j]
                if x == 0:
                    temp_path[i].append([x - 1, y])
                elif y == 0:
                    temp_path[i].append([x, y - 1])
                elif x == len(maze1) - 1:
                    temp_path[i].append([x + 1, y])
                elif y == len(maze1[0]) - 1:
                    temp_path[i].append([x, y + 1])
        # 又创建了两个新的空列表
        temp1 = []
        temp2 = []
        #
        for i in range(len(temp_path)):
            aa = copy.deepcopy(sorted(temp_path[i], key=lambda x: (x[0], x[1])))
            bb = copy.deepcopy(sorted(temp_path[i], key=lambda x: (x[1], x[0])))
            aa_list = [aa[0]]
            bb_list = [bb[0]]
            for i in range(len(aa)):
                if aa[i][-1] - aa_list[-1][-1] == 1 and aa[i][0] == aa_list[-1][0]:
                    aa_list.append(aa[i])
                else:
                    if len(aa_list) > 1:
                        temp1.append((aa_list[0], aa_list[-1]))
                    aa_list = [aa[i]]
                if bb[i][0] - bb_list[-1][0] == 1 and bb[i][1] == bb_list[-1][1]:
                    bb_list.append(bb[i])
                else:
                    if len(bb_list) > 1:
                        temp2.append((bb_list[0], bb_list[-1]))
                    bb_list = [bb[i]]
                if len(aa_list) > 1 and i == len(aa) - 1:
                    temp1.append((aa_list[0], aa_list[-1]))
                if len(bb_list) > 1 and i == len(aa) - 1:
                    temp2.append((bb_list[0], bb_list[-1]))
        temp1 = sorted(temp1, key=lambda x: (x[0]))
        temp1.extend(sorted(temp2, key=lambda x: (x[0][1])))

        print(temp1)
        self.draw_path_list = temp1

    def display(self):
        a = self.filename
        a = a.split('.')
        tex_name = a[0] + '.tex'
        tex = open(tex_name, 'w')

        tex.write('''\\documentclass[10pt]{article}
\\usepackage{tikz}
\\usetikzlibrary{shapes.misc}
\\usepackage[margin=0cm]{geometry}
\\pagestyle{empty}
\\tikzstyle{every node}=[cross out, draw, red]

\\begin{document}

\\vspace*{\\fill}
\\begin{center}
\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n''')

        tex.write('% Walls\n')  # draw wall
        wall_list = self.draw_maze_wall()
        for i in wall_list:
            (x1, y1), (x2, y2) = i
            tex.write(f'    \\draw ({x1},{y1}) -- ({x2},{y2});\n')

        tex.write('% Pillars\n')  # draw pillars
        pillars = self.pillar_list
        for i in pillars:
            x, y = i
            tex.write(f'    \\fill[green] ({y},{x}) circle(0.2);\n')

        tex.write('% Inner points in accessible cul-de-sacs\n')  # inner point
        cross = self.block_list
        cross.sort()
        for i in range(len(cross)):
            x1, y1 = cross[i]
            if x1 % 2 == 1 and y1 % 2 == 1:
                tex.write(f'    \\node at ({y1/2},{x1/2}) {{}};\n')

        tex.write('% Entry-exit paths without intersections\n')  # path
        path = self.draw_path_list
        for i in range(len(path)):
            (x1, y1), (x2, y2) = path[i]
            tex.write(f'    \draw[dashed, yellow] ({y1/2},{x1/2}) -- ({y2/2},{x2/2});\n')

        tex.write('''\\end{tikzpicture}
\\end{center}
\\vspace*{\\fill}
\\end{document}\n''')


maze = Maze('maze_1.txt')
maze.display()