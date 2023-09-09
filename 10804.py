array = list(range(1, 21))

for i in range(10):
    head, tail = map(int, input().split())
    head -= 1
    
    reversed_portion = array[head:tail][::-1]

    array[head:tail] = reversed_portion
    
print(' '.join(map(str, array)))