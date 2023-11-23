import sys

class zero_stack:
    def __init__(self) -> None:
        self.stack = []
        
    def print_sum(self):
        if self.stack:
            print(sum(self.stack))
            
        else: print(0)
        
    def push(self, num):
        self.stack.append(num)
        
    def zero(self):
        if self.stack:
            self.stack.pop()

#### main

Z = zero_stack()

for i in range(int(sys.stdin.readline().rstrip())):
    command = int(sys.stdin.readline().rstrip())
    
    if command == 0:
        Z.zero()
    
    else:
        Z.push(command)
        
Z.print_sum()