#abcdefghijklmnopqrstuvwxyz
line = [-1] * 26
temp = input().upper()
for i in range(len(temp)):
    if line[ord(temp[i]) - 65] == -1:
        line[ord(temp[i]) - 65] = i

print(" ".join(str(num) for num in line))