import math
def lcm(a, b):
    return a * b / math.gcd(a, b)


num = int(input())

for i in range(num):
    a, b = map(int, input().split())
    print(int(lcm(a, b)))