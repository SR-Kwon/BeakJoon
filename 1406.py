import sys

class editor:
    def __init__(self, line):
        self.front_stack = list(line)
        self.end_stack = []
        
    def __str__(self) -> str:
        return ''.join(self.front_stack) + ''.join(self.end_stack[::-1])
    
    def move_corsor(self, state):
        if state == 'L':
            if self.front_stack:
                self.end_stack.append(self.front_stack.pop())
        elif state == 'R':
            if self.end_stack:
                self.front_stack.append(self.end_stack.pop())
    
    def remove(self):
        if self.front_stack:
            self.front_stack.pop()
        
    def insert(self, char):
        self.front_stack.append(char)

###main
my_editor = editor(sys.stdin.readline().rstrip())

for i in range(int(sys.stdin.readline().rstrip())):
    command = sys.stdin.readline().rstrip()
    
    if command[0] == 'L':
        my_editor.move_corsor('L')
        
    elif command[0] == 'D':
        my_editor.move_corsor('R')
        
    elif command[0] == 'B':
        my_editor.remove()
    
    elif command[0] == 'P':
        my_editor.insert(command[2])
    
    else: print('Unknown Command')
    
print(my_editor)