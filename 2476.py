def get_price():
    temp = input()
    a = [int(num) for num in temp.split()]
    a.sort()

    if a[0] == a[1] and a[1] == a[2]:
        return(10000+a[0]*1000)
    elif a[0] == a[1]:
        return(1000 + a[0] * 100)
    elif a[1] == a[2]:
        return(1000 + a[1] * 100)
    else:
        return(100 * a[2])
    
times = int(input())
temp = []
for i in range(times):
    temp.append(get_price())

print(max(temp))