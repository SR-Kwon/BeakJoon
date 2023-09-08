'''
영식 요금제는 30초마다 10원씩 청구된다. 이 말은 만약 29초 또는 그 보다 적은 시간 통화를 했으면 10원이 청구된다. 만약 30초부터 59초 사이로 통화를 했으면 20원이 청구된다.

민식 요금제는 60초마다 15원씩 청구된다. 이 말은 만약 59초 또는 그 보다 적은 시간 통화를 했으면 15원이 청구된다. 만약 60초부터 119초 사이로 통화를 했으면 30원이 청구된다.

동호가 저번 달에 새악대로 T 통신사를 이용할 때 통화 시간 목록이 주어지면 어느 요금제를 사용 하는 것이 저렴한지 출력하는 프로그램을 작성하시오.
'''

#0시간 일때도 고려해야함
#개판이네 다시짜자

def compare(times):
    for time in times:
        price_영식 += (time // 30) * 10
        price_민식 += (time // 60) * 15
        print(price_민식,price_영식)
        
    if price_영식 > price_민식:
        print('M', price_민식)
    elif price_영식 < price_민식:
        print('Y', price_영식)
    else:
        print('Y M', price_영식)
        
    


call_num = int(input())
times = list(map(int,input().split()))

compare(times)