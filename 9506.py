while True:
    a = int(input())
    if a == -1:
        break
    
    temp = []
    for i in range(1,a):
        if a % i == 0:
            temp.append(i)
    
    if len(temp) > 1 and sum(temp) == a:
        print(a,'= 1',end='')
        for i in temp[1:]:
            print(' +',i,end='')
        print()
    else:
        print(a, 'is NOT perfect.')