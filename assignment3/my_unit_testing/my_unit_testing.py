class UnitTest(object):
    """Class UnitTest implementing a small testing framework for functions.

    This class contains functions for testing the return value of external function
    with arbitrary arguments and keyword arguments.

    Attributes:
        func: A callable function.
        args: An argument or an argument list.
        kwargs: A dictionary of optional keyword arguments. The key in the dictionary
            should correspond to the name of the optional keyword argument in func.
        res: An expected result from callind func with args and kwargs.
    """

    def __init__(self, func, args, kwargs, res):    # make test
        """Constructor for class UnitTest.

        The constructor initalizes input arguments in class UnitTest. If func is a
        constant or non-callable, the constructor converts func to a callable
        lambda-function with the same number of arguments as in args and kwargs.

        Args:
            func: A callable function or constant.
            args: An argument or an argument list to func.
            kwargs: A dictionary of keyword arguments with key value equal to the
                keyword arguments in func.
            res: An expected result from func(*args, **kwargs)
        """

        # Check if func is a callable function
        if callable(func):
            self.func = func
        else:
            self.func = lambda *args, **kwargs: func

        # Store parameters in class
        self.args = args or []
        self.kwargs = kwargs or {}
        self.res = res

    def __call__(self):                             # run test
        """Calling function for class UnitTest

        The __call__ function tries to call the function func by splatting args and
        kwargs as arguments.

        Return:
            @value: boolean
                    Returns True if return value from self.func is equal to self.res.
                    Else, returns False
        """

        try: # Check if any errors were raised during calling of self.func
            return self.func(*self.args, **self.kwargs) == self.res

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
