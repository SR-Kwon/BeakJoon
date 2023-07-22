#시간을 HH MM 입력하면 45분을 뺀 시간을 출력하는 프로그램

hour, min = map(int, input().split())

if((min - 45) < 0):
    min += 15
    hour -= 1
    if(hour <0):
        hour += 24

else: min -= 45


print(hour, min)