my_list = []
for i in range(9):
    my_list.append(int(input()))
    
print(max(my_list))
print(my_list.index(max(my_list)) + 1)