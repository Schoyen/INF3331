class UnitTest(object):
    """
    Class UnitTest implementing a small testing framework for functions.
    """

    def __init__(self, func, args, kwargs, res):    # make test
        """
        ----------------------------------------------------------------------------------------
        UnitTest.__init__(self, func, args, kwargs, res)

        Constructor in UnitTest.

        If the input func isn't a callable function, we convert it to a lambda-function returning
        the constant supplied as input func.

        Input:
            @param1: func
                     A callable function (or constant that will be treated as a function)
            @param2: args
                     A list of arguments to func
            @param3: kwargs
                     A dictionary with extra additional arguments to func
            @param4: res
                     A correct value to test return value of func
        """

        # Check if @param1 is a callable function
        if callable(func):
            self.func = func
        else:
            self.func = lambda *args, **kwargs: func

        # Store parameters in class
        self.args = args
        self.kwargs = kwargs
        self.res = res

    def __call__(self):                             # run test
        """
        ----------------------------------------------------------------------------------------
        UnitTest.__call__(self)

        Calling function in UnitTest.

        Return:
            @value: boolean
                    Returns True if return value from self.func is equal to self.res.
                    Else, returns False
        """

        try: # Check if any errors were raised during calling of self.func
            if self.kwargs != None and self.args != None:
                return self.func(*self.args, **self.kwargs) == self.res

            elif self.kwargs != None and self.args == None:
                return self.func(**self.kwargs) == self.res

            elif self.kwargs == None and self.args != None:
                return self.func(*self.args) == self.res

            else:
                return self.func() == self.res

        except IndexError:
            return False



if __name__ == '__main__':
    # Outputting documentation in UniTest
    print (UnitTest.__doc__)
    print (UnitTest.__init__.__doc__)
    print (UnitTest.__call__.__doc__)

    # Short and simple testing of the module
    func = lambda a, b, c: a + b + c
    func_const = 6
    func_no_param = lambda: 0
    func_no_args = lambda a=2: a
    func_all = lambda a, b, c=3: a * b + c
    func_random = lambda a=1, b=2, c=3: a + b + c
    a = 1
    b = 2
    c = 3
    res = 6
    unit = UnitTest(func, [a, b, c], None, res)
    assert unit(), "[ERROR] %g != %d" % (func(a, b, c), res)
    unit = UnitTest(func_const, [a, b, c], None, res)
    assert unit(), "[ERROR] %g != %d" % (func_const, res)
    unit = UnitTest(func_no_param, None, None, 0)
    assert unit(), "[ERROR] %g != %d" % (func_no_param(), 0)
    unit = UnitTest(func_no_args, None, {'a': 3}, 3)
    assert unit(), "[ERROR] %g != %d" % (func_no_args(3), 3)
    unit = UnitTest(func_all, [1, 2], {'c': 3}, 5)
    assert unit(), "[ERROR] %g != %d" % (func_all(1, 2, 3), 5)

    unit = UnitTest(func_random, None, {'c': 5, 'b': 2, 'a': 1}, 8)
    assert unit(), "[ERROR] %g != %d" % (func_random(a=1, b=2, c=5), 8)
