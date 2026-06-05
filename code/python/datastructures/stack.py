class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class LL_Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        self.top = Node(data,self.top)
    
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

class Array_Stack:
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
    a = LL_Stack()
    a.push(10)
    a.push(20)
    a.push(30)

    a.printall()

    print(a.pop())
    print(a.pop())
    print(a.pop())

    a.printall()

if __name__ == "__main__":
    main()