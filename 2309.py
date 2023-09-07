import itertools

키 = []
for i in range(9):
    키.append(int(input()))

조합 = itertools.combinations(키, 7)
for set in 조합:
    if sum(set) == 100:
        sorted_tuple = sorted(set, reverse = False)
        break

for i in sorted_tuple:
    print(i)