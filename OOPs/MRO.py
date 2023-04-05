class P:
    pass


class A(P):
    pass


class B(A):
    pass


class X(P):
    pass


class Y(X):
    pass


class C(B, Y):
    pass


print(C.mro())