#수학여행 참가 학생수, 한방에 배정할수있는 최대 수
attend_num, each_room_max = map(int, input().split(' '))

boys = [0] * 6
girls = [0] * 6

#성별(여 0, 남 1), 학년
for i in range(attend_num):
    gender, grade = map(int, input().split(' '))
    
    if gender == 0:
        girls[grade - 1] += 1
    
    else:
        boys[grade - 1] += 1

#방 배정 시작
