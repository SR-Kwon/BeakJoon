word = list(input())
rev = word.copy()
rev.reverse()

if word == rev:
    print(1)
else:
    print(0)