num = int(input())
vote = input()

if num == 1:
    print(vote)
else:
    if vote.count('A') > vote.count('B'):
        print('A')
    elif vote.count('A') < vote.count('B'):
        print('B')
    elif vote.count('A') == vote.count('B'):
        print('Tie')