room_num = [int(i) for i in input()]

final_set = 0
for i in range(0, 10):
    setnum = 0
    if i == 6 or i == 9:
        setnum = room_num.count(i) - 1
    else:
        setnum = room_num.count(i)
    
    if setnum > final_set:
        final_set = setnum

print(final_set)