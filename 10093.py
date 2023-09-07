#같은수일때 생각해보자 아직 못품

low, high = map(int, input().split())

if low > high:
    temp = low
    low = high
    high = temp
    
print(high - low - 1)
for i in range(high - low - 2):
    print(low + i + 1, end=' ')
print(high - 1)