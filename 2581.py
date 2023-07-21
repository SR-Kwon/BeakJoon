def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

a = int(input())
b = int(input())

result = 0
res = []
for i in range(a, (b + 1)):
    if is_prime_number(i) == True:
        res.append(i)

if len(res) == 0:
    print('-1')
else:
    print(sum(res))
    print(res[0])