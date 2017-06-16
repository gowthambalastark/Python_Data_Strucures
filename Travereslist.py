class Node:
  def __init__(self,initdata):
      self.data = initdata
      self.next = None

class LinkedList:
    def __init__( self ):
        self.head = None
        self.tail = None
    def add(self,data):
        new_node=Node(data)
        if self.head == None:
            self.head = new_node
        if self.tail!=None:
            self.tail.next = new_node
        self.tail = new_node
        self.tail.next=None
    def traverse(self,n,m):
        q=self.head
        while q!=None:
            c=0
            for i in range(n):
                c+=1
                if q!=None:
                    print("Retain nodes:",q.data)
                    if c==n:
                        pass
                    else:
                        q=q.next
                else:
                    break
            if q!=None:
                k=q
                q=q.next
                for j in range(m):
                    if q!=None:
                        q=q.next
                    else:
                        k.next=None
                        break
                k.next=q
    def showit(self):
        q=self.head
        while q!=None:
            print(q.data)
            q=q.next
l=LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.add(6)
l.add(7)
l.add(8)
l.showit()
l.traverse(3,3)
l.showit()

        
	
