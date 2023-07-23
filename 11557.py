import operator

mt_count = int(input())

for i in range(mt_count):
    dic = {}
    school_num = int(input())
    for j in range(school_num):
        key, val = input().split()
        dic[key] = int(val)
        
    d1 = sorted(dic.items(), key=operator.itemgetter(1), reverse = True)
    my_list = list(d1)
    print(my_list[0][0])