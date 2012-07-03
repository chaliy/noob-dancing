# Linked list, how to detect cycle
class Node:    
	def __init__(self, data, next):
		self.data = data
		self.next = next

def detect_cycle(head):
    a = head
    b = head.next
    while a and b and a != b:    
        print a.data + " - " + b.data           
        a = a.next
        b = b.next.next if b.next else None        
        
    return a == b
    
n6 = Node("A6", None)
n5 = Node("A5", n6)
n4 = Node("A4", n5)
n3 = Node("A3", n4)
n2 = Node("A2", n3)
nh = Node("A1", n2)

n5.next = n2

# n1 -> n2 -> n3 -> n4 -> n5 -> n2 -> n3

print "with cycle result: " + str(detect_cycle(nh))

n23 = Node("A3", None)
n22 = Node("A2", n23)
n2h = Node("A1", n22)

print "without cycle result: " + str(detect_cycle(n2h))

n3h = Node("A1", None)
n3h.next = n3h

print "with cycle 1el result: " + str(detect_cycle(n3h))