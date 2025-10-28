class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    # get
    def x(self):
        return self._x

    @x.setter
    # set
    def x(self, value):
        self._x += value

    @x.deleter
    # delete
    def x(self):
        self._x = None


foo = Foo("A")
print(foo.x)

foo.x = "R"
print(foo.x)


del foo.x

print(foo.x)
