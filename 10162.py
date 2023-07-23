num = int(input())
        
A = num // 300
num %= 300
B = num // 60
num %= 60
C = num // 10
num %= 10
if num == 0:
    print(A, B, C)
else:
    print(-1)