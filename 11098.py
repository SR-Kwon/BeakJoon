n = int(input())

for i in range(n):
    p = int(input())
    price = [None] * p
    name = [None] * p
    for j in range(p):
        a = input().split()
        price[j] = int(a[0])
        name[j] = a[1]
    
    print(name[price.index(max(price))])