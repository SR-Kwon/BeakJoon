#주어진 정수를 서로다른 자연수의 합으로 나타내는 최대
##해결 안됨

def seperate(num):
    count = 0
    x = 1
    while num >= x:
        if (num - x) >= x:
            count += 1
            num -= x
            print(x)
        x += 1
        
    return count

num = int(input())
print('result :',seperate(num))