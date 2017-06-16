class Node:
  def __init__(self,initdata):
      self.data = initdata
      self.next = None

class LinkedList:
	def __init__( self ):
		self.head = None
		self.tail = None
		self.left=None
		self.leftt=None
	
	def add(self,data):
		new_node=Node(data)
		if data<0:
			if self.left==None:		
				self.left=new_node
			if self.leftt!=None:
				self.leftt.next=new_node
			self.leftt=new_node
	        else:
                    if self.head == None:
                        self.head = new_node
		    if self.tail != None:
			self.tail.next = new_node
		    self.tail = new_node
	def reverseList(self):
		if self.head == None or self.head.next == None:
			return self.head
		
		to_do = self.head.next
		reversed_list = self.head
		reversed_list.next = None
		self.tail = reversed_list
		while to_do != None:
			temp = to_do
			to_do = to_do.next
			temp.next = reversed_list
			reversed_list = temp
		self.head = reversed_list
	
	def recursiveReverse(self, node):
		if node == None or node.next == None:
			return node
		reversed_list = self.recursiveReverse(node.next)
		node.next.next = node
		node.next = None
		return reversed_list

	def printList(self):
		node = self.head
		while node != None:
			print(node.data)
			node = node.next

l = LinkedList()

l.add( 10 )
l.add( 11 )
l.add( 12 )
l.add(-1)
l.add(-3)
l.printList()
l.reverseList()
l.printList()
