class Node:	
	def __init__(self, data, next):
		self.data = data
		self.next = next

def generate_list():
	return Node("A", Node("B", Node("C", Node("D", Node("E", Node("F", None))))))

def print_list(head):
	while head:
		print head.data,		
		head = head.next
	print

def reverse(head):
	prev = None
	# O(n)
	while head:
		next = head.next		
		head.next = prev
		if next == None:
			return head
		prev = head
		head = next		

l = generate_list()
print_list(l)
l2 = reverse(l)
print_list(l2)