import node

class Stack_Linked_List:
    def __init__(self):
        self.top = None

    def push(self,data):
        self.top = node.Node(data,self.top)
    
    def pop(self):
        if self.top == None:
            raise "stack emtpy"
        data = self.top.data
        self.top = self.top.next
        return data
    
    def printall(self):
        print("Elements of the stack ")
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next
        print()

class Stack_Array:
    def __init__(self):
        self.arr = []

    def push(self,data):
        self.arr.append(data)

    def pop(self):
        if self.arr == []:
            raise "stack emtpy"
        data = self.arr.pop()
        return data      

def main():
    a = Stack_Linked_List()
    a.push(10)
    a.push(20)
    a.push(30)

    a.printall()

    print("popped" , a.pop())
    print("popped" , a.pop())
    print("popped" , a.pop())
    print()

    a.printall()

if __name__ == "__main__":
    main()