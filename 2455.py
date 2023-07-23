people = 0
line = []
for i in range(4):
    a, b = map(int, input().split())
    people = people - a + b
    line.append(people)
    
print(max(line))