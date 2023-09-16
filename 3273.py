#투포인터의 시작.

import sys

len = int(sys.stdin.readline())
int_set = list(map(int , sys.stdin.readline().split(" ")))
goal = int(sys.stdin.readline())
int_set.sort()

pair_num = 0
sp = 0
ep = len - 1

while sp < ep:
    sum = int_set[sp] + int_set[ep]
    if sum == goal:
        pair_num += 1
        sp += 1
    elif sum < goal:
        sp += 1
    else:
        ep -= 1
    
    
print(pair_num)