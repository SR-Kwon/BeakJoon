Line_a = list(input())
Line_b = list(input())

for i in Line_a[:]:
    if i in Line_b:
        Line_a.remove(i)
        Line_b.remove(i)
        
print(len(Line_a) + len(Line_b))