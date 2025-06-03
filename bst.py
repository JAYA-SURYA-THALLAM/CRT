class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
class bst:
    def __init__(self):
        self.root=None

    def insert(self,data,root):
        #if root is empty
        if(root is None):
            #create a node
            return Node(data)

#if data<root ---->left recursion call
        if data<root.data:
            root.left=self.insert(data,root.left)
        elif data>root.data :
            root.right=self.insert(data,root.right)
        return root               
    def inorder_traversal(self,root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data,end=" ")
            self.inorder_traversal(root.right)
    def preorder_traversal(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
    def postorder_traversal(self,root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data,end=" ")
    # def search_in_bst(self,root) :
    #     print(root.data,end=" ")
    # def search_in_bst(self,root,key):
    #     if(root.data==key):
    #         return True
    #     if(root is None):
    #         return False
    #     if (key<root.data):
    #         return self.search_in_bst(root.left,key)
    #     elif(key>root.data):
    #         return self.search_in_bst(root.right,key)
    #     else:
    #         return True
    def height(self,root):
        if(root is None):
            return 0
        else:
            return 1+max(self.height(root.left),self.height(root.right))                   
                    
bst_tree=bst() #object for above class name
root=None
root=bst_tree.insert(20,root)
root=bst_tree.insert(30,root)
root=bst_tree.insert(69,root)
bst_tree.inorder_traversal(root)
bst_tree.preorder_traversal(root)
bst_tree.postorder_traversal(root)
print("\n")
# search_ans=bst_tree.search_in_bst

