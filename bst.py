class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def addit(self,root,v):
        if root is None:
            root=v
        else:
            if root.data>=v.data:
                if root.left is None:
                    root.left=v
                else:
                    self.addit(root.left,v)
            if root.data<v.data:
                if root.right is None:
                    root.right=v
                else:
                    self.addit(root.right,v)
    def height(self,root):
        if root is None:
            return 0

        print(max((self.height(root.left),self.height(root.left)))+1)
        print(self.height(root.left))
        print("ad" ,self.height(root.right))

    def inorder_t(self,root):
        if root is not None:
            self.inorder_t(root.left)
            print(root.data)
            self.inorder_t(root.right)
    def preorder_t(self,root):
        if root is not None:
            print(root.data)
            self.preorder_t(root.left)
            self.preorder_t(root.right)
    def postorder_t(self,root):
        if root is not None:
            self.postorder_t(root.left)
            self.postorder_t(root.right)
            print(root.data)
    #def delete(self,root,v):
        #if v<root.data:
            #self.delete(root.left,v)
        #elif v>root.data:
            #self.delete(root.right,v)
        #elif v==root.data:
            #if root.left is None and root.right is None:
                #root.data=None
                #root.left=None
                #root.right=None
            #elif root.left is None:
                #return root.
f=Tree(3)
g=bst()
g.addit(f,Tree(4))
g.addit(f,Tree(2))
g.addit(f,Tree(6))
g.addit(f,Tree(2))
g.addit(f,Tree(1))
print("Inorder")
g.height(f)
#g.inorder_t(f)
#print("Preorder")
#g.preorder_t(f)
#print("Postorder")
#g.postorder_t(f)
