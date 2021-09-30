import math
import json


class Vector:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            vector = json.loads(args[0])
            self.components = vector
            self.size = len(vector)
        elif len(args) == 1 and isinstance(args[0], list):
            self.components = args[0]
            self.size = len(args[0])
        else:
            self.components = []
            for i in args:
                self.components.append(i)
            self.size = len(self.components)

    def __str__(self):
        return f"Vector{self.size}: {self.components}"

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        return json.dumps(self.components)

    @property
    def x(self):
        return self.components[0]

    @property
    def y(self):
        assert self.size >= 2
        return self.components[1]

    @property
    def z(self):
        assert self.size >= 3
        return self.components[2]

    @property
    def w(self):
        assert self.size >= 4
        return self.components[3]

    def dot(self, rhs):
        scalar_product = 0
        assert self.size == rhs.size
        for i in range(self.size):
            scalar_product += self.components[i] * rhs.components[i]
        return scalar_product

    def norm(self):
        return math.sqrt(self[0] * self[0] + self[1] * self[1] + self[2] * self[2])

    def normalize(self, length=1):
        assert self.size == 3
        return self / (length * self.norm())

    def cross(self, rhs):
        assert self.size == 3 and rhs.size == 3
        return Vector(
            self[1] * rhs[2] - self[2] * rhs[1],
            self[2] * rhs[0] - self[0] * rhs[2],
            self[0] * rhs[1] - self[1] * rhs[0],
        )

    def __add__(self, rhs):
        new_vec = []
        assert self.size == rhs.size
        for i in range(self.size):
            new_vec.append(self.components[i] + rhs.components[i])
        return Vector(*new_vec)

    def __sub__(self, rhs):
        new_vec = []
        assert self.size == rhs.size
        for i in range(self.size):
            new_vec.append(self.components[i] - rhs.components[i])
        return Vector(*new_vec)

    def __truediv__(self, divisor):
        new_vec = []
        for i in range(self.size):
            new_vec.append(self.components[i] / divisor)
        return Vector(*new_vec)

    def __getitem__(self, index):
        assert self.size > index
        return self.components[index]

    def __mul__(self, rhs):
        if isinstance(rhs, Vector):
            scalar_product = 0
            assert self.size == rhs.size
            for i in range(self.size):
                scalar_product += self.components[i] * rhs.components[i]
            return scalar_product
        else:
            new_vec = []
            for i in range(self.size):
                new_vec.append(self.components[i] * rhs)
            return Vector(*new_vec)

    def __rmul__(self, scalar):
        return self * scalar

    def __neg__(self):
        return self * -1

    def __eq__(self, rhs):
        if len(self.components) != rhs.size:
            return False
        for i in range(self.size):
            if self.components[i] != rhs.components[i]:
                return False
        return True
