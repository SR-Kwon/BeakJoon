import sys

class my_stack:
    def __init__(self):
        self.stack = []
        
    def push(self, num):
        self.stack.append(num)
        
    def pop(self):
        if self.stack:
            print(self.stack.pop())
        else:
            print(-1)
            
    def size(self):
        print(len(self.stack))
        
    def empty(self):
        print(1 if self.stack == [] else 0)
        
    def top(self):
        if self.stack:
            print(self.stack[-1])
        else:
            print(-1)
            
#####main
S = my_stack()

for i in range(int(sys.stdin.readline().rstrip())):
    command = list(sys.stdin.readline().rstrip().split())
    
    if command[0] == 'push':
        S.push(command[1])
        
    elif command[0] == 'pop':
        S.pop()
        
    elif command[0] == 'size':
        S.size()
    
    elif command[0] == 'empty':
        S.empty()
    
    elif command[0] == 'top':
        S.top()
        
    else: print('Unknown Command')