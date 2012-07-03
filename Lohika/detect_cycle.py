# Linked list, how to detect cycle
class Node:    
	def __init__(self, data, next):
		self.data = data
		self.next = next

def print_list(head):
	while head:
		print head.data,		
		head = head.next
	print

def detect_cycle(head):
    a = head
    b = head.next
    while a and b:
        print a.data + " - " + b.data
        if a == b:
            return True
        a = a.next
        b = b.next.next if b.next else None        
        
    return False
    
n6 = Node("A6", None)
n5 = Node("A5", n6)
n4 = Node("A4", n5)
n3 = Node("A3", n4)
n2 = Node("A2", n3)
nh = Node("A1", n2)

n5.next = n2

# n1 -> n2 -> n3 -> n4 -> n5 -> n2 -> n3

print detect_cycle(nh)