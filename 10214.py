T = int(input())

for i in range(T):
    yon_total, ko_total = 0, 0
    for j in range(9):
        yon, ko = map(int, input().split())
        yon_total += yon
        ko_total += ko
  
    if yon_total == ko_total: print('Draw')
    elif yon_total > ko_total: print('Yonsei')
    else: print('Korea')