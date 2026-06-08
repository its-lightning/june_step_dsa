import node

class Dequeue_DLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue_rear(self,data):
        self.printall()
        new_node = node.Node_2pointer(data,None,None)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.previous = self.rear
            self.rear = new_node
    
    def dequeue_front(self):
        self.printall()
        if self.front == None:
            raise "queue empty"
        temp = self.front.data
        if self.front.next == None:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.previous = None
        
        return temp
    
    def enqueue_front(self,data):
        self.printall()
        new_node = node.Node_2pointer(data,None,None)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.front.previous = new_node
            new_node.next = self.front
            self.front = new_node

    def dequeue_rear(self):
        self.printall()
        if self.front == None:
            raise "queue empty"
        temp = self.rear.data
        if self.rear.previous == None:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.previous
            self.rear.next = None
        return temp
    
    def printall(self):
        temp = self.front
        while temp:
            print(temp.data,end = " ")
            temp = temp.next
        
        print("\t\t\t",end="")

        temp = self.rear
        while temp:
            print(temp.data,end = " ")
            temp = temp.previous
        
        print()

def main():
    a = Dequeue_DLL()

    print("\n=== enqueue_rear ===")
    a.enqueue_rear(10)
    a.enqueue_rear(20)
    a.enqueue_rear(30)
    a.printall()

    print("\npopped :", a.dequeue_front())   # 10
    a.printall()

    print("\npopped :", a.dequeue_rear())    # 30
    a.printall()

    print("\n=== enqueue_front ===")
    a.enqueue_front(5)
    a.enqueue_front(1)
    a.printall()

    print("\npopped :", a.dequeue_front())   # 1
    a.printall()

    print("\npopped :", a.dequeue_rear())    # 20
    a.printall()

    print("\n=== single node tests ===")

    b = Dequeue_DLL()

    b.enqueue_rear(100)
    b.printall()

    print("\npopped :", b.dequeue_front())   # 100
    b.printall()

    b.enqueue_front(200)
    b.printall()

    print("\npopped :", b.dequeue_rear())    # 200
    b.printall()

    print("\n=== alternating operations ===")

    c = Dequeue_DLL()

    c.enqueue_front(10)
    c.enqueue_rear(20)
    c.enqueue_front(5)
    c.enqueue_rear(30)
    c.printall()

    print("\npopped :", c.dequeue_front())   # 5
    c.printall()

    print("\npopped :", c.dequeue_rear())    # 30
    c.printall()

    print("\npopped :", c.dequeue_front())   # 10
    c.printall()

    print("\npopped :", c.dequeue_rear())    # 20
    c.printall()


if __name__ == "__main__":
    main()