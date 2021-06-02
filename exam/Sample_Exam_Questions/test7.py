num = [0,1,2,3,4,5,6,7,8,9]
height = 5
d=0
for i in range(1,height+1):
    print(' '*(height-i),end='')
    for j in range((i-1)*2+1):
        print(d,end='')
        d=(d+1)%10
    print()
