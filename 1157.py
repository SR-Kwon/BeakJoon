res = list(input().upper())
res.sort()

word = []
count = []
for i in res[:]:
    if i in word:
        count[word.index(i)] += 1
    else:
        word.append(i)
        count.append(1)
        
if count.count(max(count)) != 1:
    print("?")
    
else:
    print(word[count.index(max(count))])