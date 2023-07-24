res = []
for i in range(10):
    temp = int(input()) % 42
    if temp in res:
        pass
    else:
        res.append(temp)
print(len(res))