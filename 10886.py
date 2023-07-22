#0 = not cute / 1 = cute

num = int(input())

result = 0
for i in range(num):
    result += int(input())
    
if result > num / 2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')