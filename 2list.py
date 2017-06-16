class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.left=None
        self.leftt=None
    def add(self,data):
        if data<0:
            node=Node(data)
            if self.left==None:
                self.left=node
            if self.leftt!=None:
                self.leftt.next=node
            self.leftt=node
        else:
            node=Node(data)
            if self.head==None:
                self.head=node
            if self.tail!=None:
                self.tail.next=node
            self.tail=node
    def printList(self):
        k = self.head
        nodes=self.left
        while nodes != None:
            print(nodes.data)
            nodes = nodes.next
        print("2 nd list")
        while k != None:
            print(k.data)
            k = k.next
l = LinkedList()
l.add(1)
l.add(2)
l.add(-1)
l.add(-4)
l.printList()
