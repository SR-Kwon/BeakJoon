while True:
    a = input().split()
    if a == ['0', '0']:
        break
    print(int(a[0]) + int(a[1]))