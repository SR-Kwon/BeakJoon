
a = 0
for i in range(5):
    temp = int(input())
    if temp < 40:
        a += 40
    else:
        a += temp
    
print(int(a/5))