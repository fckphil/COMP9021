# COMP9021 19T3 - Rachid Hamadi
# Sample Exam 2


def remove_consecutive_duplicates(word):
    '''
    >>> remove_consecutive_duplicates('')
    ''
    >>> remove_consecutive_duplicates('a')
    'a'
    >>> remove_consecutive_duplicates('ab')
    'ab'
    >>> remove_consecutive_duplicates('aba')
    'aba'
    >>> remove_consecutive_duplicates('aaabbbbbaaa')
    'aba'
    >>> remove_consecutive_duplicates('abcaaabbbcccabc')
    'abcabcabc'
    >>> remove_consecutive_duplicates('aaabbbbbaaacaacdddd')
    'abacacd'
    '''
    # Insert your code here (the output is returned, not printed out)               
    i = 0
    word = list(word)
    while i < (len(word)-1):
        if word[i] == word[i+1]:
            del word[i]
        else:
            i += 1
    word = ''.join(word)
    # print('\'',end='')
    return word
    # print('\'',end='')

            
if __name__ == '__main__':
    import doctest
    doctest.testmod()
