def judge(a, b):
    la, lb = list(a), list(b)
    la.sort()
    lb.sort()
    if la == lb:
        print("Possible")
    else:
        print("Impossible")

num = int(input())

for i in range(num): 
    Line_a, Line_b = input().split()
    judge(Line_a, Line_b)