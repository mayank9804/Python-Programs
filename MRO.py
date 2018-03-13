# Src : https://makina-corpus.com/blog/metier/2014/python-tutorial-understanding-python-mro-class-search-path
# Follow the link to know more about Python 2 and Python3 Method Resolution Order
class A:
    def foo(self):
        print('A')

class B(A):
    def foo(self):
        print('B')
        super(B, self).foo()
        print('x')

class C(A):
    def foo(self):
        print('C')
        super(C, self).foo()
        print('x2')

class D(B,C):
    def foo(self):
        print('D')
        super(D, self).foo()

d = D()
d.foo()
