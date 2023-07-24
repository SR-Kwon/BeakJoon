T = int(input())
for i in range(T):
    W, H, num = map(int, input().split())
    num1 = num
    while num1 > W:
        num1 -= W
    YY = str(num1)
    
    XX = str((num - 1) // W + 1)
    if len(XX) == 1:
        XX = str('0')+str(XX)

    print(YY+XX)