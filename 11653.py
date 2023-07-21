#소인수 분해 코드

def soin(num):
    x = 2
    while num >= x:
        if num % x == 0:
            print(x)
            num /= x
        else:
            x += 1
            
a = int(input())
soin(a)