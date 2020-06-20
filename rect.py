class Rect():
    def __init__(self, a=0, b=0):
        assert (((a is int or a is float) and a > 0)
            and ((b is int or b is float) and b > 0)),\
            f"a = {a} and b = {b} must be a number !"
        self._a = a
        self._l = b 

    def area(self):
        return self._a * self._l

# r1 = Rect()
r2 = Rect("hey", 2)

# print(f"Area: {r1.area()}")
print(f"Area: {r2.area()}")