#Singly Linked List


#Create a node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    #Insert at the begining
    def insertAtBeginning(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    #Insert at the end
    def insertAtEnd(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
        
    #Insert at the specific position
    def insert_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for i in range(position - 1):
            if current is None:
                raise ValueError("Position out of bounds")
            current = current.next

        new_node.next = current.next
        current.next = new_node
    
    #Delete at the beginning
    def deleteAtBeginning(self):
    	if self.head==None:
    		print('Singly_Linked_List is Empty.')
    		return
    	ptr=self.head
    	self.head=self.head.next
    
    #Delete at the end
    def deleteAtEnd(self):
    	if self.head==None:
    		print('Singly_Linked_List is Empty.')
    		return
    	ptr=self.head
    	ptr2=ptr.next
    	while(ptr2.next):
    		ptr=ptr2
    		ptr2=ptr.next
    	ptr.next=None
    #Delete at the specific position
    def delete_position(self,position):
        if self.head==None:
        	print("Singly_Linked_List is Empty.")
        	return
        if position==0:
        	current=self.head
        	self.head=current.next
        	return
        current = self.head
        for i in range(position-1):
            if current is None:
                raise ValueError("Position out of bounds")
            current = current.next

        
        current.next = current.next.next	
     
    #Sort
    def sort(self):
    	current=self.head
    	ptr=None
    	
    	if self.head==None:
    		print("Singly_Linked_List is Empty.")
    		return
    	
    	while(current!=None):
    		
    		ptr=current.next
    		while(ptr!=None):
    			if current.data>ptr.data:
    				temp=current.data
    				current.data=ptr.data
    				ptr.data=temp
    			ptr=ptr.next
    		current=current.next
    				

    		
    	
    #Display Node
    def display(self):
    	   if self.head==None:
    	   	print("Singly_Linked_List is Empty.")
    	   else:
    	   	current=self.head
    	   	print("Singly Linked List is:")
    	   	print("____________")
    	   	while(current!=None):
    	   		print(current.data,"->",end=" ")
    	   		current=current.next
    	   	print()
    	   	
    	   
    	   
    	   
l=LinkedList()

while True:
	print("1.Add_Beginning")
	print("2.Add_End")
	print("3.Add_Any_Position")
	print("4.Delete_Beginning")
	print("5.Delete_End")
	print("6.Delete_Position")
	print("7.Sort")
	print("8.Display")
	print("9.Exit")
	try:
		ch=int(input("Enter Choice:"))
	except:
		print("Enter Valid Input....")
		break
	if ch==1:
		try:
			new_data=input("Enter Node:")
		except:
			print("Enter Valid Input....")
			break
		l.insertAtBeginning(new_data)
	if ch==2:
		try:
			new_data=input("Enter Node:")
		except:
			print("Enter Valid Input....")
			break
		l.insertAtEnd(new_data)
	if ch==3:
		try:
			new=int(input("Enter Position:"))
		except:
			print("Enter Valid Input....")
			break
		try:
			new_data=input("Enter Node:")
		except:
			print("Enter Valid Input....")
			break
		try:
			l.insert_position(new_data,new)
		except:
			print("Index Out of Bounds.")
			break
	if ch==4:
		l.deleteAtBeginning()
	if ch==5:
		l.deleteAtEnd()
	if ch==6:
		try:
			position=int(input("Enter Position:"))
		except:
			print("Enter Valid Input....")
			break
		try:
			l.delete_position(position)
		except:
			print("Enter Valid Input...")
			break
	if ch==7:
		l.sort()
	if ch==8:
		l.display()
	if ch==9:
		print("Exit Successfully.....")
		break
	if ch==0 or ch>9:
		print("Enter Valid Input...")
		break
	
