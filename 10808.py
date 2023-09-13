text = list(input())

for i in range(97, 122):
    print(text.count(chr(i)), end=' ')
print(text.count(chr(122)))