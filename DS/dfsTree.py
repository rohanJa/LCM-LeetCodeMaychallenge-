class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None


    def dfs(self, node):

        if node:
            self.dfs(node.left)
            self.dfs(node.right)
            print(str(node.data),end=' ')

obj = Tree()
obj.root = Node(1) 
obj.root.left = Node(2) 
obj.root.right = Node(3) 
obj.root.left.left = Node(4) 
obj.root.left.right = Node(5) 
obj.dfs(obj.root)