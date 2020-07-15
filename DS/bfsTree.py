class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def bfs(self):
        if self.root is None:
            return 
        
        queue = []
        queue.append(self.root)    

        while(len(queue)>0):
            print(queue[0].data)

            obj = queue.pop(0)

            if obj.left is not None:
                queue.append(obj.left)

            if obj.right is not None:
                queue.append(obj.right)

tree = Tree()
tree.root = Node(1)
tree.root.left = Node(2)       
tree.root.right = Node(3)
tree.root.left.left = Node(4)  
tree.root.left.right = Node(5)       
tree.root.left.right.left = Node(15)


tree.bfs()