# coding=utf-8
import string

# Resolution Principle
# http://mathworld.wolfram.com/ResolutionPrinciple.html
        
class Expr(object):

    def isEmptyDisjunction(self): return isinstance(self, EmptyDisjunctionExpr)
    def isBinary(self): return isinstance(self, BinaryExpr)
    def isUnary(self): return isinstance(self, UnaryExpr)
    def isUnknown(self): return isinstance(self, UnknownExpr)
    
    # http://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
    def __eq__(self, other): 
        if type(other) is type(self): 
            return self.__dict__ == other.__dict__ 
        else: 
            return False 
 
    def __ne__(self, other): 
        return not self.__eq__(other) 

        
class BinaryExpr(Expr):
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op # Connective

    def _dispalyOp(self):
        if self.op == "AND":
            return "˄"; # Conjunction
        if self.op == "OR":
            return "˅"; # Disjunction
            
    def __repr__(self):
        return str(self.left) + " " + self._dispalyOp() + " " + str(self.right)

class UnaryExpr(Expr):
    def __init__(self, val, op):        
        self.val = val
        self.op = op
        
    def __repr__(self):
        if self.op == "NOT":
            return "¬" + str(self.val)


class UnknownExpr(Expr):
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return self.n

class EmptyDisjunctionExpr(Expr):
    
    def __repr__(self):
        return "□"
        
def isContrary(e1, e2):
    if e1.isUnary() and e2.isUnknown():
        if e1.op == "NOT" and e1.val == e2:
            return True
    if e1.isUnknown() and e2.isUnary():
        if e1 == e2.val and e2.op == "NOT":
            return True
    return False

def findConjunctions(e):
    if e.isBinary() and e.op == "OR":
        return [e.left, e.right]
    if (e.isUnary()) or e.isUnknown():
        return [e]

def resolvent(e1, e2):
    sc1 = findConjunctions(e1)
    sc2 = findConjunctions(e2)
    
    for sc1i in sc1:  
        for sc2i in sc2:
            if isContrary(sc1i, sc2i):
                sc1r = filter(lambda x: x != sc1i, sc1)
                sc2r = filter(lambda x: x != sc2i, sc2)
                if len(sc1r) == 0 and len(sc2r) == 0:
                    return EmptyDisjunctionExpr()
                if len(sc1r) == 1 and len(sc2r) == 0:
                    return sc1r[0]
                if len(sc1r) == 0 and len(sc2r) == 1:
                    return sc2r[0]
                if len(sc1r) == 1 and len(sc2r) == 1:
                    return BinaryExpr(sc1r[0], sc2r[0], "OR")
                raise Exception("Making resolvent from " + str(sc1r) + " and " + str(sc2r) + " failed")


def negation(e): return UnaryExpr(e, "NOT")
def conjunction(left, right): return BinaryExpr(left, right, "AND")
def disjunction(left, right): return BinaryExpr(left, right, "OR")

def findElementaryDisjunctions(e):
    if e.isBinary() and e.op == "IMPLICAITON":
        return disjunction(negation(e.left), e.right)
    return e

def disproveSet(ss):
    print "Disprove set of " + str(ss)    
    while True:
        e1 = ss[0]
        for e2 in filter(lambda x: x != e1, ss):
            ns = resolvent(e1, e2)
            print "    resolvent for " +  str(e1) + " and " + str(e2) + " is " + str(ns)
            if ns == None:
                continue
            if ns.isEmptyDisjunction():
                return "Disproved"
            ss.append(ns)
            ss.remove(e1)
            ss.remove(e2)
            break;
        else:
            return "Cannot disprove";        

p = UnknownExpr("p")
q = UnknownExpr("q")
r = UnknownExpr("r")
s = UnknownExpr("s")


print "Result: " + disproveSet([
    BinaryExpr(UnaryExpr(p, "NOT"), q, "OR"), # ¬p ˅ q
    UnaryExpr(q, "NOT"), # ¬q
    p # p
    ])


print "Result: " + disproveSet([
    BinaryExpr(p, q, "OR"), # p ˅ q
    BinaryExpr(UnaryExpr(p, "NOT"), r, "OR"), # ¬p ˅ r
    BinaryExpr(UnaryExpr(q, "NOT"), s, "OR"), # ¬q ˅ s
    UnaryExpr(r, "NOT"), # ¬r
    UnaryExpr(s, "NOT"), # ¬s
    ])

# ˅ - OR
# ˄ - AND
# ¬ - NOT