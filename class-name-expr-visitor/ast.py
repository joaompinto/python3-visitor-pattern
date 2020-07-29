class Expr(object):
    def accept(self, visitor):
        method_name = "visit_{}".format(self.__class__.__name__.lower())
        visit = getattr(visitor, method_name)
        return visit(self)


class Int(Expr):
    def __init__(self, value):
        self.value = value


class Add(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Mul(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right
