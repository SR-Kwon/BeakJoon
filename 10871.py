T, num = map(int, input().split())
line = input().split()
for i in line[:]:
    if int(i) >= num:
        line.remove(i)

print(' '.join(line))