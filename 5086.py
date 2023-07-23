while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    #첫 번째 숫자가 두 번째 숫자의 약수이다.
    if b % a == 0:
        print('factor')
    #첫 번째 숫자가 두 번째 숫자의 배수이다.
    elif a % b == 0:
        print('multiple')
    #첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.
    else:
        print('neither')
