def user_input():
    while True:
        try:
            a_input = input('How can I help you?')
        finally:
            pass
        a_input = a_input.split()
        elements_not_of_roman = ['A', 'B', 'E', 'F', 'G', 'H', 'J', 'K', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W',
                                 'Y', 'Z']
        if len(a_input) == 3:
            if a_input[0] == 'Please' and a_input[1] == 'convert':
                if a_input[-1].isdigit() and int(a_input[-1]) >= 0 and int(a_input[-1]) <= 3999 and a_input[-1][0] != '0':
                    dic1 = {0: ('', 'M', 'MM', 'MMM'),
                            1: ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
                            2: ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
                            3: ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')}
                    rom = []
                    rom.append(dic1[0][int(int(a_input[-1]) / 1000 % 10)])
                    rom.append(dic1[1][int(int(a_input[-1])  / 100 % 10)])
                    rom.append(dic1[2][int(int(a_input[-1])  / 10 % 10)])
                    rom.append(dic1[3][int(int(a_input[-1])  % 10)])
                    s = ''
                    for i in rom:
                        s = s + i
                    print (f'Sure! It is {s}')
                    exit()
                elif a_input[-1].isalpha() and a_input[-1].isupper():
                    not_in_roman = [i for i in a_input[-1] if i not in "IVXLCDM"]
                    qelement = [i for i in a_input[-1] if i * 4 in a_input[-1]]
                    if not_in_roman + qelement != []:
                        print('Hey, ask me something that\'s not impossible to do!')
                        exit()
                    else:
                                omit = -1
                                result = 0
                                convert = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
                                string = a_input[-1]
                                if string in convert:
                                    print(convert[string])
                                    exit()
                                else:
                                    for i in range(len(string)):
                                        if i == omit:
                                            pass
                                        elif i <= len(string) - 2:
                                            if convert[string[i]] < convert[string[i+1]]:
                                                result += convert[string[i+1]] - convert[string[i]]
                                                omit = i+1
                                            else:
                                                result += convert[string[i]]
                                        else:
                                            result += convert[string[i]]

                                            dic1 = {0: ('', 'M', 'MM', 'MMM'),
                                                    1: ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
                                                    2: ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
                                                    3: ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')}
                                            rom = []
                                            rom.append(dic1[0][int(int(result) / 1000 % 10)])
                                            rom.append(dic1[1][int(int(result) / 100 % 10)])
                                            rom.append(dic1[2][int(int(result) / 10 % 10)])
                                            rom.append(dic1[3][int(int(result) % 10)])
                                            s = ''
                                            for i in rom:
                                                s = s + i
                                            if a_input[-1] == s:
                                                    print(f'Sure! It is {result}')
                                                    exit()
                                            else:

                                                print('Hey, ask me something that\'s not impossible to do!')
                                                exit()
                else:
                    print('Hey, ask me something that\'s not impossible to do!')
                    exit()
            else:
                print('I don\'t get what you want, sorry mate!')
                exit()
        elif len(a_input) == 5:
            if a_input[0] == 'Please' and a_input[1] == 'convert' and a_input[3] == 'using':
                if a_input[-1].isalpha():
                    qelement = [i for i in a_input[-1] if i * 4 in a_input[-1]]
                    a = list(a_input[-1])
                    n = len(a)
                    for i in range(n):
                        if a.count(a[i]) != 1:
                            test = 0
                        else:
                            test = 1
                    if test == 0 or qelement != []:
                        print('Hey, ask me something that\'s not impossible to do!')
                        exit()
                    else:
                            if a_input[2].isdigit() and int(a_input[2]) > 0 and a_input[2][0] != '0':
                                #situation1
                                number = int(a_input[2])
                                s2 = a_input[-1][::-1]
                                result2 = {}
                                default = 1
                                if s2:
                                    for index2 in range(0, len(s2), 2):
                                        rom2 = s2[index2]
                                        result2[rom2] = default
                                        if index2 < (len(s2) - 1):
                                            next = s2[index2 + 1]
                                            result2[rom2 + next] = 4 * default
                                            result2[next] = 5 * default
                                        if index2 + 1 < (len(s2) - 1):
                                            nnext = s2[index2 + 2]
                                            result2[rom2 + nnext] = 9 * default
                                            result2[nnext] = 10 * default
                                        default *= 10
                                dict = result2
                                s1 = a_input[2]



                                rom_dict_num = {a: b for b, a in dict.items()}
                                result3 = ''
                                key = rom_dict_num.keys()
                                key = sorted(key, reverse = True)
                                number = int(number)
                                for i in key:
                                    while number >= i:
                                        result3 += rom_dict_num.get(i)
                                        number -= i
                                roman = result3
                                print(f'Sure! It is {result3}')
                                exit()



                            elif a_input[2].isalpha():
                                s2 = a_input[-1][::-1]
                                result2 = {}
                                default = 1
                                if s2:
                                    for index2 in range(0, len(s2),2):
                                        rom2 = s2[index2]
                                        result2[rom2] = default
                                        if index2 < (len(s2) - 1):
                                            next = s2[index2 + 1]
                                            result2[rom2 +next] = 4 * default
                                            result2[next] = 5 * default
                                        if index2 + 1 < (len(s2) - 1):
                                            nnext = s2[index2 + 2]
                                            result2[rom2 + nnext] = 9 * default
                                            result2[nnext] = 10 * default
                                        default *= 10
                                dict = result2
                                s1 = a_input[2]
                                if s1:
                                    result1 = 0
                                    index1 = 0
                                    while index1 < len(s1):
                                        rom1 = s1[index1]
                                        if rom1 in dict:
                                            num_of_rom1 = dict[rom1]
                                        else:
                                            print('Hey, ask me something that\'s not impossible to do!')
                                            quit()
                                        if index1 < (len(s1) - 1):
                                            next1 = s1[index1 + 1]
                                            num_of_next1 = dict[next1]
                                            if num_of_next1 > num_of_rom1:
                                                result1 += num_of_next1 - num_of_rom1
                                                index1 += 2
                                                continue
                                        result1 += num_of_rom1
                                        index1 += 1
                                else:
                                    print('Hey, ask me something that\'s not impossible to do!')
                                    quit()
                                num = result1

                                rom_dict_num = {a: b for b, a in dict.items()}
                                result3 = ''
                                key = rom_dict_num.keys()
                                key = sorted(key, reverse = True)
                                number = int(num)
                                for i in key:
                                    while number >= i:
                                        result3 += rom_dict_num.get(i)
                                        number -= i
                                roman = result3
                                if a_input[2] == roman:
                                    print(f'Sure! It is {num}')
                                    quit()
                                else:
                                    print('Hey, ask me something that\'s not impossible to do!')
                                    quit()


                            else:
                                print('Hey, ask me something that\'s not impossible to do!')
                                quit()
                else:
                    print('Hey, ask me something that\'s not impossible to do!')
                    quit()
            else:
                print('I don\'t get what you want, sorry mate!')
                quit()
        elif len(a_input) == 4:
            if a_input[0] == 'Please' and a_input[1] == 'convert' and a_input[-1] == 'minimally':
                if a_input[2].isalpha():
                    print('Hey, ask me something that\'s not impossible to do!')#I CANNOT DO THIS
                    quit()

                else:
                    print('Hey, ask me something that\'s not impossible to do!')
                    quit()
            else:
                print('I don\'t get what you want, sorry mate!')
                quit()
        else:
            print('I don\'t get what you want, sorry mate!')
            quit()


user_input()

