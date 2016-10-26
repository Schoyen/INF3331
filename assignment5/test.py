
class MyObject(object):

    def __init__(self, obviously):
        self.cat = obviously

    def __call__(self):
        pass

class SubObject(MyObject):

    def __init__(self, obviously):
        self.__init__(obviously)

    def __call__(self):
        pass

    class InternalClass(object):

        def __init__(self):
            pass

        def somefunc(self):
            pass

        def 1_lol(self):
            pass

def foo():
    print ("YOLO")

def defedef():
    print ("Balle")

    def defidef():
        print ("HAHHA")

        def deffelef():
            pass

            def deffind():
                pass

# def haha()
 # def lol()

# Regular comment

adef bleh()
a = def ab():
    print ('yolo')

def a_1():
    pass

def 1_a():
    pass
def _a():
    pass # def test()

_b()
