num = int(input())
line = input().split()
for i in range(num):
    line[i] = int(line[i])
print(min(line), max(line))