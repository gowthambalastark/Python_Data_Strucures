'''class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    l=[]
    def add(self,root,data):
        if data>root.data:
            if root.right==None:
                root.right=Tree(data)
            else:
                self.add(root.right,data)
        if data<root.data:
            if root.left==None:
                root.left=Tree(data)
            else:
                self.add(root.left,data)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            bst.l.append(root.data)
            self.inorder(root.right)
            
class Node(Tree):
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self) :
        self.head = None
        self.tail=None
    def add(self,data) :
        node = Node(data)
        if self.head==None :
            self.head = node
        if self.tail!=None:
            self.tail.next=node
            node.prev=self.tail
        self.tail=node
    def printit(self):
        p=self.head
        q=self.tail
        while p is not None:
            print(p.data)
            p=p.next
        while q is not None:
            print(q.data)
            q=q.prev


r=Tree(5)
i=bst()
i.add(r,4)
i.add(r,6)
i.add(r,7)
i.add(r,3)
i.inorder(r)
l=LinkedList()
[l.add(i) for i in bst.l]
l.printit()'''
l,l1=[],[1,2,3]
l.append(l1)
l1.remove(2)
print(l,l1)
