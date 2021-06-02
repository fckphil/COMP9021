def prime(n):
    list = []
    if n == 2:
        return n
    else:
        for i in range(2,n+1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                list.append(i)
    for i in list:
        b = i
        c = max(i, b)
    print(c)
        
prime(25)
prime(27)
prime(523)