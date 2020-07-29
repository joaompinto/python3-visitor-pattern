from ast import *
from functools import singledispatchmethod

class Visitor(object):
    pass


class Eval(Visitor):

    # Default handler, will handle the Int
    @singledispatchmethod
    def visit(self, a):
        return a.value

    @visit.register
    def _(self, a: Add):
        return a.left.accept(self) + a.right.accept(self)

    @visit.register
    def _(self, a: Mul):
        return a.left.accept(self) * a.right.accept(self)


class Print(Visitor):

    # Default handler, will handle the Int
    @singledispatchmethod
    def visit(cls, a):
        return a.value

    @visit.register
    def _(self, a: Add):
        return "(+ {} {})".format(a.left.accept(self), a.right.accept(self))

    @visit.register
    def _(self, a: Mul):
        return "(* {} {})".format(a.left.accept(self), a.right.accept(self))



