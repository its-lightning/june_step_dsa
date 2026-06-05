class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    
class Node_2pointer:
    def __init__(self,data,previous = None,next = None):
        self.data = data
        self.previous = previous
        self.next = next