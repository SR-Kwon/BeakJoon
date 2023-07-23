round = int(input())
Chang, Sang = 100, 100
for i in range(round):
    C, S = map(int, input().split())
    if C == S:
        pass
    elif C > S:
        Sang -= C
    elif S > C:
        Chang -= S
print(Chang)
print(Sang)