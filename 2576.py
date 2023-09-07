temp = []
for i in range(7):
    num = int(input())
    if num % 2 != 0:
        temp.append(num)

if temp == []:
    print(-1)
else:
    print(sum(temp))
    print(min(temp))