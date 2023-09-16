def set_additional(set_amount):
    for i in range(len(set_amount)):
        set_amount[i] += 1
    
    set_amount[6] += 1
    
    return set_amount

room_num = [int(i) for i in input()]

set_num = 0
set_amount = [0] * 9 #9를 6으로 생각 하기때문에 6을 2개 넣고 9를 없앰

for i in room_num:
    if i == 9: #9일때도 6이라고 생각하자
        i = 6
        
    if set_amount[i] == 0: #해당되는 숫자가 없을때 세 하나 추가
        set_num += 1
        set_additional(set_amount)
    
    set_amount[i] -= 1 #해당되는 숫자 사용해욥!
        
print(set_num)