num = int(input())

for i in range(num):
    a, b = input().split()
    for t in b:
        print(t * int(a), end = '')
        
    print()