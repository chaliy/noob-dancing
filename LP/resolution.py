# coding=utf-8


def dispalyOp(op):
    if op == 'AND':
        return '˄'; # Conjunction
    if op == 'OR':
        return '˅'; # Disjunction
    if op == 'NOT':
        return '¬';
        
class Expr:
    def __init__(self):
        self.isBinary = False
        self.isUnary = False
        self.isUnknown = False
        
class BinaryExpr(Expr):
    def __init__(self, left, right, op):
        Expr.__init__(self)
        self.left = left
        self.right = right
        self.op = op # Connective
        self.isBinary = True
        
    def __repr__(self):
        return str(self.left) + ' ' + dispalyOp(self.op) + ' ' + str(self.right)

class UnaryExpr(Expr):
    def __init__(self, val, op):
        Expr.__init__(self)
        self.val = val
        self.op = op
        self.isUnary = True
        
    def __repr__(self):
        if self.op == 'NOT':
            return "¬" + str(self.val)


class UnknownExpr(Expr):
    def __init__(self, n):
        Expr.__init__(self)
        self.n = n
        self.isUnknown = True
    
    def __repr__(self):
        return self.n

class EmptyDisjunctionExpr(Expr):
    def __init__(self):
        Expr.__init__(self)
        
    def __repr__(self):
        return '□'

        
def isContrary(e1, e2):
    if e1.isUnary and e2.isUnknown:
        if e1.op == 'NOT' and e1.val == e2:
            return True
    if e1.isUnknown and e2.isUnary:
        if e1 == e2.val and e2.op == 'NOT':
            return True
    return False
        
def resolventa(e1, e2):
    # need something less stupid here,
    # kind of pattern matching should be good here
    if e1.isBinary and e2.isBinary:
        print "B B"
    if e1.isBinary and e2.isUnary:        
        if isContrary(e1.right, e2):
            return e1.left
        if isContrary(e1.left, e2):
            return e1.right
    if e1.isUnary and e2.isBinary:        
        if isContrary(e1, e2.right):
            return e2.left
        if isContrary(e1, e2.left):
            return e2.right
    if isContrary(e1, e2):
        return EmptyDisjunctionExpr()
    raise "Cannot resolve resolventa" 

    
# ˅ - OR
# ˄ - AND
# ¬ - NOT

p = UnknownExpr('p')
q = UnknownExpr('q')

f1 = BinaryExpr(UnaryExpr(p, 'NOT'), q, 'AND') # ¬p ˄ q
f2 = UnaryExpr(q, 'NOT') # ¬q
f3 = p # p

s1 = BinaryExpr(UnaryExpr(p, 'NOT'), q, 'AND') # ¬p ˄ q
s2 = UnaryExpr(q, 'NOT') # ¬q
s3 = p # p
s4 = resolventa(s1, s2)
s5 = resolventa(s3, s4)
print s5

print "Done"