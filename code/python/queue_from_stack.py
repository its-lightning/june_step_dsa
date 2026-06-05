import python.datastructures.stack as stack

class queue:
    def __init__(self):
        self.a = stack.LL_Stack()
        self.b = stack.LL_Stack()
    
    def enqueue(self,data):

        print(self.a.printall(),"\n",self.b.printall())

        while self.a.top:
            temp = self.a.pop()
            print(temp)
            self.b.push(temp)

        print(self.a.printall(),"\n",self.b.printall())

        self.a.push(data)

        print(self.a.printall(),"\n",self.b.printall())

        while self.b.top:
            self.a.push(self.b.pop())

        print(self.a.printall(),"\n",self.b.printall())
        print()

    def dequeue(self):
        if not self.a.top:
            self.a.pop()
        else:
            raise "queue empty"
        
def main():
    a = queue()

    a.enqueue(30)
    a.enqueue(20)
    a.enqueue(10)

    print(a.dequeue())
    print(a.dequeue())
    print(a.dequeue())

if __name__ == "__main__":
    main()