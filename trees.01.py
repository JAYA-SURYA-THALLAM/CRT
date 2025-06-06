class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.data=None

# tree=Node()
# tree.data=1
# tree.left=Node()
# tree.left.data=2
# tree.right=Node()
# tree.right.data=3
# print(tree.data)
# print(tree.left.data)
# print(tree.right.data)

    def inorder_traversal(self,Node):
        if Node:
            self.inorder_traversal(Node.left)
            print(Node.data)
            self.inorder_traversal(Node.right)
    def preorder_traversal(self,Node):
        if Node:
            print(Node.data,end=" ")
            self.preorder_traversal(Node.left)
            self.preorder_traversal(Node.right)
            print(Node.data,end=" ")  
    def postorder_traversal(self,Node):
        if Node:
            self.postorder_traversal (Node.left)
            self.postorder_traversal(Node.right)
            print(Node.data,end=" ")
    def sum_of_nodes(self,Node):
        if Node is None:
            return 0
        return Node.data +self.sum_of_nodes(Node.left)+self.sum_of_nodes(Node.right)                     
    def count_nodes(self,Node):
        if(Node is None):
            return 0
        return 1+self.count_nodes(Node.left)+self.count_nodes(Node.right)
    def height(self,Node):
        if Node is None:
            return 0
        else:
            return max(self.height(Node.left),self.height(Node.right)+1)
        
tree=Node()
tree.data=1
tree.left=Node()
tree.left.data=2
tree.right=Node()
tree.right.data=3
tree.left.left=Node()
tree.left.left.data=4
tree.left.right=Node()
tree.left.right.data=5
tree.right.left=Node()
tree.right.left.data=6
tree.right.right=Node()
tree.right.right.data=7
tree.inorder_traversal(Node=tree)
tree.preorder_traversal(Node=tree)
tree.postorder_traversal(Node=tree)
print(tree.sum_of_nodes(Node=tree))
print(tree.count_nodes(Node=tree.right))
print(tree.count_nodes(Node=tree.left))
print(tree.count_nodes(Node=tree))
print(tree.height(Node=tree.left))
print(tree.height(Node=tree.right))
print(tree.height(Node=tree))