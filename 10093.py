def 사이_수_출력(low, high):
    temp = []
    for i in range(high - low - 1):
        temp.append(low + i + 1)
        
    print(' '.join(map(str, temp)))
    
    

num1, num2 = map(int, input().split())

if num1 < num2:
    print(num2 - num1 - 1)
    사이_수_출력(num1, num2)
elif num2 < num1:
    print(num1 - num2 - 1)
    사이_수_출력(num2, num1)
else:
    print(0)