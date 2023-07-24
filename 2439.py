num = int(input())
for i in range(num, 0, -1):
    print(' ' * (i - 1), end='')
    print('*' * (num - i + 1))