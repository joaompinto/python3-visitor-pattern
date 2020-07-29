class Visitor(object):
    pass


class Eval(Visitor):
    def visit_int(self, i):
        return i.value

    def visit_add(self, a):
        return a.left.accept(self) + a.right.accept(self)

    def visit_mul(self, a):
        return a.left.accept(self) * a.right.accept(self)


class Print(Visitor):
    def visit_int(self, i):
        return i.value

    def visit_add(self, a):
        return "(+ {} {})".format(a.left.accept(self), a.right.accept(self))

    def visit_mul(self, a):
        return "(* {} {})".format(a.left.accept(self), a.right.accept(self))



