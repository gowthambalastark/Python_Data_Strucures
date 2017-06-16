class Node:
    def __init__(self,data):
            self.data=data
            self.next=None
            self.prev=None
class Linklist:
    def __init__(self):
        self.head=None
        self.tail=None

    def add(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
            self.prev=None
            self.next=None
        if self.tail != None:
            self.tail.next=node
            self.tail.next.prev=self.tail
        self.tail=node
        #self.tail.next=None
    def print(self):
        ll=[]
        t=self.head
        while t!=None:
            print(t.data)
            t=t.next

    def reverseit(self):
        if self.head==None or self.head.next==None:
            return self.head
        rl=self.head
        td=self.head.next
        rl.prev=None
        rl.next=None
        while td!=None:
            t=td
            td=td.next
            rl.prev=t
            t.next=rl
            rl=t
        self.head=rl

    def delet(self,k):
        if self.head.data==k:
            t=self.head
            self.head=t.next
            t.prev=None
        else:
            t=self.head.next
            while t!=None:
                if t.data==k and t.next!=None:
                    tmp=t.prev
                    tmp.next=t.next
                    t.next.prev=tmp
                    break
                elif t.data==k and t.next==None:
                    tmp=t.prev
                    tmp.next=None
                    t.prev=None
                    break
                else:
                    t=t.next
    def sea(self,k):
          c=0
          f=0
          t=self.head
          while t!=None:
              c+=1
              if t.data==k:
                  f=1
                  print("Found in",c,"Position")
              t=t.next
          if f==0:print("Not there Bitch")

    def printList(self,v=[]):
	    node = self.head
	    while node != None:
	        if srt(node.data) not in self.v:
                    v.append(node.data)
                else:
                    node.prev.next=node.next
            node = node.next
 	
l=Linklist()
l.add(1)
l.add(2)
l.add(3)
l.print()
l.sea(1)
l.delet(3)
l.print()
