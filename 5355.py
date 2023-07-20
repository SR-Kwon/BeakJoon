#@는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다. 따라서, 화성에서는 수학 식의 가장 앞에 수가 하나 있고, 그 다음에는 연산자가 있다.

num = int(input())

for i in range(num):
    a  = input().split()
    result = float(a[0])
    for t in a[1:]:
        if t == '@':
            result *= 3
        elif t == '%':
            result += 5
        elif t == '#':
            result -= 7

    print(f'{result:.02f}')