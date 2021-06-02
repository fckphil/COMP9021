# COMP9021 19T3 - Rachid Hamadi
# Quiz 4 *** Due Thursday Week 5
#
# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends
#   and around parentheses and commas, is a valid word.


import sys
import re


def is_valid_symbol(word):
    return re.search('[^a-zA-Z_]', word) == None


def is_valid_char(char):
    return re.search('[^a-zA-Z_,\(\) ]', char) == None


def get_form_tree(word):
    raw_leaves = list(word)
    tree = []
    currentSymbol = ''
    while(not len(raw_leaves) == 0):
        char = raw_leaves.pop(0)
        if (not is_valid_char(char)):
            # 不合法字符返回 False
            return False
        elif char == ' ':
            # 空格过滤
            continue
        elif is_valid_symbol(char):
            # symbol 拼接
            currentSymbol += char
        elif char == '(' or char == ',':
            # 遇到 ( 和 , 拼接的 symbol 和自己入栈
            if not currentSymbol == '':
                tree.append(currentSymbol)
                currentSymbol = ''
            tree.append(char)
        elif char == ')':
            # 遇到右括号构造子树
            if not currentSymbol == '':
                tree.append(currentSymbol)
                currentSymbol = ''
            leaves = []
            while True:
                # 叶子进一个数组
                leaf = tree.pop()
                if leaf == '(':
                    # 找到第一个 (
                    break
                if not leaf == ',':
                    leaves.insert(0, leaf)
            node = tree.pop()
            # 子树入栈
            tree.append({node: leaves})
    return tree[0]


def is_valid_tree(tree, arity):
    if (type(tree) == type({})):
        for key in tree:
            if (not is_valid_tree(tree[key], arity)):
                return False
    elif (type(tree) == type([])):
        if (not len(tree) == arity):
            return False
        for sub_tree in tree:
            if (not is_valid_tree(sub_tree, arity)):
                return False
    return True


def is_valid(word, arity):
    try:
        tree = get_form_tree(word)
    except:
        return False
    else:
        if (not type(tree) == type({})):
            # 正常解析出字典类型
            return False
        else:
            return is_valid_tree(tree, arity)
    return True


try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')
