# 세그먼트 트리 활용해서 풀자
from functools import reduce
N, M, K = map(int, input().split())
line = []
for i in range(N):
    line.append(int(input()))
    
while M > 0 or K > 0:
    a, b, c = map(int, input().split())
    
    if a == 1: #변경
        line[b - 1] = c
        M -= 1
    
    elif a == 2: #곱 구하기
        print(reduce(lambda x, y: x * y, line[b - 1: c]))
        K -= 1
        
#뭐여이게