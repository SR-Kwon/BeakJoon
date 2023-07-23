temp_a, temp_b = input().split()
a = list(map(int, temp_a))
b = list(map(int, temp_b))
a.reverse()
b.reverse()

max_length = max(len(a), len(b))
result = [0] * (max_length + 1)

for i in range(len(a)):
    result[i] += a[i]

for i in range(len(b)):
    result[i] += b[i]

    
for i in range(len(result)):
    if result[i] >= 10:
        result[i] -= 10
        result[i+1] += 1

result.reverse()
if result[0] == 0:
    del result[0]
    
for i in result[:]:
    print(i, end='')
print()

#####2안
# print(sum(map(int, input().split())))