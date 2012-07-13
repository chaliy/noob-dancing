# 4 people
# 1, 2, 5, 10 - time this people use to get on the other side
# Max two people at once
# Single lighter, they should bring every time

from collections import deque

pp = [10,5,2,1]
pp2 = []

def move(p1, p2):    
    if p1 > p2:
        return p1
    return p2    
    

r = 0;
#r += moveback(0,1)

#first pair
p1 = pp.pop()
p2 = pp.pop()

r += move(p1,p2)

pp2.append(p1)
pp2.append(p2)

