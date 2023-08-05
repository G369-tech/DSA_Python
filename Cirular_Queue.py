class CircularQueue():

	# constructor
	def __init__(self, size): # initializing the class
		self.size = size
		
		# initializing queue with none
		self.queue = [None for i in range(size)]
		self.front = self.rear = -1

	def enqueue(self, data):
		
		# condition if queue is full
		if ((self.rear + 1) % self.size == self.front):
			print(" Queue is Full\n")
			
		# condition for empty queue
		elif (self.front == -1):
			self.front = 0
			self.rear = 0
			self.queue[self.rear] = data
		else:
			
			# next position of rear
			self.rear = (self.rear + 1) % self.size
			self.queue[self.rear] = data
			
	def dequeue(self):
		if (self.front == -1): # condition for empty queue
			print ("Queue is Empty\n")
			
		# condition for only one element
		elif (self.front == self.rear):
			temp=self.queue[self.front]
			self.front = -1
			self.rear = -1
			return temp
		else:
			temp = self.queue[self.front]
			self.front = (self.front + 1) % self.size
			return temp

	def display(self):
	
		# condition for empty queue
		if(self.front == -1):
			print ("Queue is Empty")

		elif (self.rear >= self.front):
			print("Elements in the circular queue are:",
											end = " ")
			for i in range(self.front, self.rear + 1):
				print(self.queue[i], end = " ")
			print ()

		else:
			print ("Elements in Circular Queue are:",
										end = " ")
			for i in range(self.front, self.size):
				print(self.queue[i], end = " ")
			for i in range(0, self.rear + 1):
				print(self.queue[i], end = " ")
			print ()

		if ((self.rear + 1) % self.size == self.front):
			print("Queue is Full")
try:
    size=int(input("Enter Size of Queue:"))
except:
    print("Enter Valid Input.....")
# Driver Code
ob = CircularQueue(size)

# This code is contributed by AshwinGoel

while True:
    print("1 Add")
    print("2 Remove")
    print("3 Display")
    print("4 Exit")
    try:
        ch = int(input("Enter Choice:"))
    except:
    	print("Enter Valid Input...")
    	break
    if ch == 1:
        data=input("Enter Element of Circular_Queue:")
        ob.enqueue(data)
    elif ch==2:
    	ob.dequeue()
    elif ch==3:
    	ob.display()
    elif ch == 4:
        print("Exit Successfully....")
        break
    else:
    	print("Enter Valid Choice....")
