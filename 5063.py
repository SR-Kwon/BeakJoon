def pred(r, e, c):
    if (e - r) > c:
        print('advertise')
    elif (e - r) == c:
        print('does not matter')
    else:
        print('do not advertise')

num = int(input())

for i in range(num):
    r, e, c = map(int, input().split())
    pred(r, e, c)