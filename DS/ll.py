class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printArray(self):
        temp = self.head

        while(temp):
            print(temp.data)
            temp=temp.next

    def reverse(self):
        temp = self.head
        prev = None
        while(temp):
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
        self.head = prev

    def sort(self):
        length=0
        temp=self.head

        while(temp):
            temp=temp.next
            length+=1
        s=None
        for i in range(0,length):
            temp=self.head
            small=temp.data
            while(temp.next):
                if(temp.next.data<small):
                    small=temp.next.data
                    s=temp
            s.next=s.next.next
            temp=s.next
            temp=temp.next
l = LinkedList()
l.head = Node(1)
l.head.next = Node(3)
l.printArray()
l.reverse()
l.printArray()
l.sort()