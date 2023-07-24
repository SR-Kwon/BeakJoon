p = int(input())
table_2d = [input().split() for _ in range(p)]
for i in table_2d:
    i[1] = int(i[1])
    i[2] = int(i[2])
    i[3] = int(i[3])

table_2d.sort(key=lambda x:x[1])
table_2d.sort(key=lambda x:x[2])
table_2d.sort(key=lambda x:x[3])

print(table_2d[-1][0])
print(table_2d[0][0])