def test(s):

	x = []
	# O(n)
	for i in range(0, len(s)):
		if s[i] == "(":
			x.append(i)
		else:
			if len(x) == 0:
				return i
			x.pop()	

	# O(1)
	if len(x) != 0:
		return len(s) - 1 # Last char is invalid parenthes
	
	return -1

def test_test(s):
	print s + " resulted to " + str(test(s))

test_test("((())())()")
test_test(")()(")
test_test("()(")