class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
		
class SinglyLinkedList:
	def __init__(self):
		self.head=None
	
	def insert_at_beginning(self,data):
		new_node=Node(data)
		
		if self.head==None:
			self.head=new_node
		else:
			new_node.next=self.head
			self.head=new_node
	
	def display(self):
		current=self.head
		while(current!=None):
			print(f"Data:{current.data}")
			current=current.next
	
	def Middle_Element(self):
		current=self.head
		l=[]
		while(current!=None):
			l.append(current.data)
			current=current.next
		l.sort()
		print("Middle of Given Singly_Linked_List is:",l[len(l)//2])
		
s1=SinglyLinkedList()

for i in range(1,6):
	s1.insert_at_beginning(i)

s1.display()
s1.Middle_Element()