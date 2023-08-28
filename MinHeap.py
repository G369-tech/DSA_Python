from heapq import *
if __name__=='__main__':
	max_heap=[]
	
	arr = [4,2,6]
	
	for i in range(len(arr)):
		heappush(max_heap,arr[i])
		
	print(max_heap[0])
	heappop(max_heap)
	print(max_heap[0])
	heappop(max_heap)
	print(max_heap[0])