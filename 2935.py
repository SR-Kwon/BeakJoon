def cal(a, b, symbol):
    if symbol == '+':
        return a + b
    elif symbol == '*':
        return a*b
    else: print("Haven't learned it yet")
    return None

a = int(input())
symbol = input()
b = int(input())

print(cal(a,b,symbol))