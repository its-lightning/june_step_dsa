class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    
class Node_2pointer:
    def __init__(self,data,next = None,previous = None):
        self.data = data
        self.next = next
        self.previous = previous