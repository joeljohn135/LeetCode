class Solution:
	def isValid(self, s) :
		stack = []
		for brac in s:

			if brac == '(':
				stack.append(brac)
			elif brac == '{':
				stack.append(brac)
			elif brac == '[':
				stack.append(brac)
                
			else:
				if not stack:
					return False
				top = stack.pop()
				if top=='(' and brac == ')':
					continue
				elif top=='{' and brac == '}':
					continue
				elif top=='[' and brac == ']':
					continue
				else:
					return False

		if len(stack)>0:
			return False
		else:
			return True
    
         
