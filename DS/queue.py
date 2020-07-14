class Queue:

    def __init__(self):
        self.queue = []
    
    def pop(self):
        if self.queue:
            self.queue.pop(0)
        else:
            print("Queue is empty")

    def push(self,data):
        self.queue.append(data)
    
    def printArray(self):
        print(self.queue)

obj = Queue()
obj.pop()
obj.push(1)
obj.push(122)
obj.push(512)
obj.printArray()
obj.pop()
obj.printArray()
obj.push(6612)
obj.printArray()
obj.pop()
obj.printArray()
