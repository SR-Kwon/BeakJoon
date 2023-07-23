# #주어진 정수를 서로다른 자연수의 합으로 나타내는 최대

# num = int(input())
# count = 0

# if num == 2:
#     print(1)
#     quit()
# if num == 3:
#     print(2)
#     quit()
    
# for n in range(num):
#     count += 1
#     if (n * (n + 1)) / 2 > num:
#         count -= 2
#         break
    
# print(count)
s = int(input())
total = 0
count = 0

while True:
    count += 1
    total += count
    if total > s:
        break

print(count-1)