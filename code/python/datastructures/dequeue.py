import node

class Dequeue_LL:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue_front(self,data):
        new_node = node.Node(data,None)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue_front(self):
        if self.front == None:
            raise "queue emtpy"
        temp = self.front.data
        self.front = self.front.next
        return temp
    
    def enqueue_back(self,data):
        new_node = node.Node(data,None)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue_back(self):
        if self.front == None:
            raise "queue emtpy"
        temp = self.front.data
        self.front = self.front.next
        return temp
