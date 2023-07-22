a = input()

cm = 10

for i in range(1, len(a)):
    cm += 10
    if a[i - 1] == a[i]:
        cm -= 5
    elif a[i - 1] != a[i]:
        pass
    
print(cm)