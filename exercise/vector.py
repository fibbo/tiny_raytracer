import math


class Vector:
    # TODO: Implement constructor

    # TODO: Implement __str__

    # TODO: Implement properties

    # TODO: Implement dot product

    # TODO: Implement norm

    # TODO: Implement normalize

    # TODO: Implement cross product

    # TODO: Implement __add__

    # TODO: Implement __sub__ (subtraction)

    # TODO: Implement division (which special function name is the correct one?)

    # TODO: Implement __mul__ (multiplication)

    # TODO: Try vector * scalar and scalar * vector

    # TODO: Implement __neg__ (additive inverse)

    # TODO: Implement __eq__

    # TODO: Implement __getitem__

    pass


def tests():
    a = Vector(1, 0, 0)
    b = Vector(2, 1, 1)
    c = Vector(3, 4, 5)

    assert a == Vector(1, 0, 0)

    res1 = 2 * b
    res2 = b * 2

    assert res1 == Vector(4, 2, 2)
    assert res1 == res2

    assert -b == Vector(-2, -1, -1)
    assert b == Vector(2, 1, 1)

    n = a.normalize()

    assert n.norm() == 1.0

    assert a.dot(c) == c.dot(a)

    assert b.cross(c) == Vector(1, -7, 5)
    assert c.cross(b) == -b.cross(c)

    assert a + b == Vector(3, 1, 1)

    d = Vector(1, 2, 3, 4)
    e = d * 2
    assert e == Vector(2, 4, 6, 8)
    assert e / 2 == d

    print("All tests successful")


if __name__ == "__main__":
    tests()
