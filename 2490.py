# 입력
# 첫째 줄부터 셋째 줄까지 각 줄에 각각 한 번 던진 윷짝들의 상태를 나타내는 네 개의 정수(0 또는 1)가 빈칸을 사이에 두고 주어진다.
# 출력
# 첫째 줄부터 셋째 줄까지 한 줄에 하나씩 결과를 도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E로 출력한다.

def validate(stat):
    if stat.count('0') == 0:
        print("E")
    elif stat.count('0') == 1:
        print("A")
    elif stat.count('0') == 2:
        print("B")
    elif stat.count('0') == 3:
        print("C")
    elif stat.count('0') == 4:
        print("D")

for i in range(3):
    yut = list(input().split())
    validate(yut)