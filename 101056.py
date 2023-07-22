cookie, num, money = map(int, input().split())

if (cookie * num) > money:
    print((cookie * num) - money)
else: print(0)