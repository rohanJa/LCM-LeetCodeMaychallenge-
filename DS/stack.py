class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.stack :
            return self.stack.pop(-1)
        else:
            print("Stack is empty")
    
    def push(self, data):      
        self.stack.append(data)
    
    def printStack(self):
        print(self.stack)

obj = Stack()

obj.pop()
obj.printStack()
obj.push(4)
obj.push(14)
obj.push(24)
obj.printStack()
obj.pop()
obj.printStack()
