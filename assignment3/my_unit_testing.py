class UnitTest(object):
    def __init__(self, func, args, kwargs, res):    # make test

        if callable(func):
            self.func = func
        else:
            print ("[DEBUG] In %s UnitTest.__init__: Parameter func is not callable. Treating as a callable constant" % __name__)
            self.func = lambda a, b, num_rechecks=2: func # TODO: Check if number of arguments in lambda can be arbitrary

        self.args = args
        self.kwargs = kwargs
        self.res = res

    def __call__(self):                             # run test
        try:
            return self.func(self.args[0], self.args[1], num_rechecks=self.kwargs["num_rechecks"]) == self.res
        except IndexError:
            return False
