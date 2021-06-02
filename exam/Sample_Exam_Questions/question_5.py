# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 5


'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    # Insert your code here
    a = []
    b = 0
    c = [] #max month
    max_month = []
    with open('cpiai.csv') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            if line[0][:4] == str(year):
                a.append(float(line[-1]))
        b = max(a)      #max inflation
    with open('cpiai.csv') as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            if line[0][:4] == str(year) and line[-1] == str(b):
                c.append(int(line[0][5:7]))
    for i in c:
        max_month.append(months[i - 1])
    print(f'In {year}, maximum inflation was: {b}')
    print('It was achieved in the following months:',end = ' ')
    print(', '.join(max_month))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
