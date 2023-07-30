#The time complexity of the add, remove, display, and peek methods are respectively O(1), O(n), O(n), and O(1). The space complexity of the entire code is O(size), where size is the user-input value for the size of the queue

class queue:
    try:
    	#Size of Queue
    	size = int(input("Enter Size of Queue:"))
    except:
    	pass

    
    #Declare Queue
    def __init__(self):
        self.a = []
    
    #Add Element in Queue
    def add(self):
        if len(self.a) == self.size:
            print("Queue is Full.")
        else:
            try:
            	element = input("Enter Element:")
            	self.a.append(element)
            except:
            	print("Enter Valid Input.....")
    
    #Remove Element in Queue
    def remove(self):
        if not self.a:
            print("Queue is Empty.")
        else:
            self.a.pop(0)
    
    #Display Queue
    def display(self):
          if not self.a:
          	print("Queue is Empty.")
          else:
          	print("Queue:")
          	for i in range(0,len(self.a)):
          		print(f"      {self.a[i]}    ")
    #Peek
    def peek(self):
         if len(self.a)==0:
          	print("Queue is Empty.")
         else:
          	print(f"First Element of Queue is: {self.a[0]}")
            	

q = queue()

while True:
    print("1 Add")
    print("2 Remove")
    print("3 Display")
    print("4 Peek")
    print("5 Exit")
    try:
    	if q.size==0:
    		print("Enter Valid Input...")
    		break
    	else:
    		ch = int(input("Enter Choice:"))
    except:
    	print("Enter Valid Input...")
    	break
    if ch == 1:
        q.add()
    elif ch==2:
    	q.remove()
    elif ch==3:
    	q.display()
    elif ch==4:
    	q.peek()
    elif ch == 5:
        print("Exit....")
        break
    else:
    	print("Enter Valid Choice....")