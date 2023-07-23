num = int(input())

for i in range(num):
    line = list(input().split('X'))

    result = 0
    for i in line[:]:
        if i != '':
            result += len(i)*(len(i) + 1) / 2
    print(int(result))