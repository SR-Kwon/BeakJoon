# 1이 루트인 tree구조 첫재줄에 몇개를 입력 받을지 하고 나머지에 상위, 하위 순으로 연결

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
class tree:
    def __init__(self, head):
        self.head = head
        
    def insert(self, mother, child):
        if mother == head:
            current_node = self.head
                
head = Node(1)


