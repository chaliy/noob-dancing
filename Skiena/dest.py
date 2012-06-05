import math

def dest(p1, p2):
	return math.sqrt(math.pow(p2[0] - p1[0],2) + math.pow(p2[1] - p1[1], 2))

p1 = (1.0,2.0)
p2 = (3.0,4.0)
print dest(p1, p2)

from Tkinter import *

master = Tk()
w = Canvas(master, width=200, height=200)
w.pack()
w.create_line(10, 20, 30, 40)
#w.create_point()
#w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

mainloop()