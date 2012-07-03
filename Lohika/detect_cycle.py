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
        if b.next == None:
            return False
            
        b = b.next.next
        
    return False

n1 = Node("A1", None)
n2 = Node("A2", n1)
n3 = Node("A3", n2)
nh = Node("A4", n3)

n1.next = n3

# n4 -> n3 -> n2 -> n1 -> n3 -> n2

print detect_cycle(nh)

#print_list(l)
#l2 = reverse(l)
#print_list(l2)