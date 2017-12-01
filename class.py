class Test(object):
    i = 3 # class (or static) variable
    @classmethod
    def g(cls, arg):
        # here we can use 'cls' instead of the class name (Test)
        if arg > cls.i:
            cls.i = arg # would the the same as  Test.i = arg1

ts=Test()
ts.g(5)
rt=Test()
print(rt.i)
print(ts.i)
rt.g(7)
print(rt.i)
print(ts.i)