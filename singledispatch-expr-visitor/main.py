from ast import Add, Int, Mul
from visitors import Print, Eval


def main():
    expr = Add(Add(Int(4), Int(3)), Mul(Int(10), Add(Int(1), Int(1))))
    print("PRINT:", expr.accept(Print()))
    print("EVAL:", expr.accept(Eval()))


if __name__ == "__main__":
    main()
