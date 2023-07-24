start = int(input())
end = int(input())
result =[]
for i in range(start, end + 1):
    for j in range(1, i + 1):
        if i == j ** 2:
            result.append(i)
            
if len(result) == 0:
    print(-1)
    
else:
    print(sum(result))
    print(result[0])