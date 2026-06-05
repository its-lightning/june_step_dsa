class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class LL_Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,data):
        new_node = Node(data,None)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.front == None:
            raise "queue emtpy"
        temp = self.front.data
        self.front = self.front.next
        return temp

class Array_Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self,data):
        self.arr.append(data)

    def dequeue(self):
        if self.arr == []:
            raise "stack emtpy"
        data = self.arr.pop(0)
        return data

class Circular_LL_Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,data):
        new_node = Node(data,None)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front
    
    def dequeue(self):
        if self.front == None:
            raise "queue emtpy"
        temp = self.front.data
        self.front = self.front.next
        return temp

class Circular_Array_Queue:
    def __init__(self,size):
        self.arr = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0
        self.size = size

    def enqueue(self,data):
        print(self.arr)
        if self.count == self.size:
            raise "queue full"

        self.arr[self.rear] = data
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        print(self.arr)
        if self.count == 0:
            raise "queue emtpy"
        data = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return data

def main():
    a = Circular_Array_Queue(5)

    a.enqueue(10)
    a.enqueue(20)
    a.enqueue(30)
    a.enqueue(10)
    a.enqueue(20)
    print(a.dequeue())
    print(a.dequeue())
    a.enqueue(30)

    print(a.dequeue())

if __name__ == "__main__":
    main()