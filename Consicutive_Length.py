class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def findit(root,prev,leng):
    if root is None:
        return leng
    cv=root.data
    if prev == cv-1:
       print(root.data)
       return max(findit(root.left,cv,leng+1),findit(root.right,cv,leng+1))
    nonc= max(findit(root.left,cv,1),findit(root.right,cv,1))
    return max(nonc,leng)
root = Node(10)
root.left = Node(11)
root.right = Node(9)
root.left.left = Node(13)
root.left.right = Node(12)
root.right.left = Node(13)
root.right.right = Node(8) 
print( "Maximum Consecutive Increasing Path Length is") 
print(findit(root,root.data,0))
