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
    def vertical(self,l):
        if len(l)!=0:
            k=l.pop(0)
            print(k.data)
            if k.left is not None:
                l.append(k.left)
            if k.right is not None:
                l.append(k.right)
            self.vertical(l)
f=Tree(2)
g=bst()
g.addit(f,Tree(1))
g.addit(f,Tree(3))
#g.addit(f,Tree(4))
#g.addit(f,Tree(5))
#g.addit(f,Tree(5))
g.vertical([f])
        
        


