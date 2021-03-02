import math


class Vector2(object):

    def __init__(self, x=0.0, y=0.0):  # constructor
        self.x = x
        self.y = y

    def __str__(self):  # print method overloading
        return "(%s,%s)" % (self.x, self.y)

    def __neg__(self):  # A=-A
        self.x = self.x*-1
        self.y = self.y*-1
        return Vector2(self.x, self.y)

    def __add__(self, rhs):  # '+' operator overloading just call A+B
        return Vector2(self.x+rhs.x, self.y+rhs.y)

    def __sub__(self, rhs):  # '-' operator overloading just call A-B
        return Vector2(self.x-rhs.x, self.y-rhs.y)

    def __mul__(self, scalar):  # scalar must be positive
        return Vector2(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        return Vector2(self.x, self.y)

    '''@classmethod
    def from_points(cls,P1, P2):
        return cls(P2.x-P1.x, P2.y-P1.y)'''

    @staticmethod
    def from_points(P1, P2):
        return Vector2(P2.x-P1.x, P2.y-P1.y)

    def get_magnitude(self):
        return math.sqrt(float(self.x**2)+float(self.y**2))

    def normalize(self):
        magnitude = self.get_magnitude()
        self.x = self.x/magnitude
        self.y = self.y/magnitude
        return self.x, self.y


A = Vector2(10, 20)
B = Vector2(30, 35)
C = Vector2(15, 45)
A=A*(1/2)
print(A)

# # print(A)
# # print(B)
# # print(C)

AB = Vector2.from_points(A, B)
BC = Vector2.from_points(B, C)
# AC = Vector2.from_points(A, C)
print('print AB :', AB)
print('print BC :', BC)
# print('print AC :',AC)
AC = AB+BC  # method overloading + ,__add__
print(AC)
# print(AB.get_magnitude())
# AB.normalize()
# print(AB)

# calculating position
'''position=Vector2(A.x,A.y)
scalar=AB*.05
for n in range(20):
    position=position+scalar
    print(position)

print('position :',position)
# AB=AB/2
# print('divide :',AB)


'''
