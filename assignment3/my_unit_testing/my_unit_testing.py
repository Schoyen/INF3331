class UnitTest(object):
    """Class UnitTest implementing a small test framework for simple functions."""

    def __init__(self, func, args, kwargs, res):    # make test
        """Constructor in UnitTest.

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
            print ("[DEBUG] In %s UnitTest.__init__: Parameter func is not callable. Treating as a callable constant" % __name__)
            self.func = lambda a, b, num_rechecks=2: func

        # Store parameters in class
        self.args = args
        self.kwargs = kwargs
        self.res = res

    def __call__(self):                             # run test
        """Calling function in UnitTest

        Return:
            @value: boolean
                    Returns True if return value from self.func is equal to self.res.
                    Else, returns False
        """

        try: # Check if any errors were raised during calling of self.func
            return self.func(self.args[0], self.args[1], num_rechecks=self.kwargs["num_rechecks"]) == self.res
        except IndexError:
            return False
