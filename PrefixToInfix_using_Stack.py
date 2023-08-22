def Pre_Infix(expr):
	stack=[]
	operators=set(['-','+','*','/','^'])
	for char in reversed(expr):
		if char.isalnum():
			stack.append(char)
		elif char in operators:
			s1=stack.pop()
			s2=stack.pop()
			new_expr=f'({s1}{char}{s2})'
			stack.append(new_expr)
		else:
			print("Enter Valid Input.....")
			return False
	print(f"Infix:{stack.pop()}")


try:
	expr=input("Enter Prefix_Expression:")
except:
	print("Enter Valid Input....")
Pre_Infix(expr)