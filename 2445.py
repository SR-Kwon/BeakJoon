num = int(input())

for i in range(1, num + 1):
    print('*' * i, end='')
    print(' ' * ((num - i) * 2), end='')
    print('*' * i)
    
for i in range(num - 1, 0, -1):
    print('*' * i, end='')
    print(' ' * ((num - i) * 2), end='')
    print('*' * i) 