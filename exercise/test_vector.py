import unittest
import math

from vector import Vector


class VectorTests(unittest.TestCase):
    def setUp(self):
        self.a = Vector(1.0, 1.0, 1.0)
        self.b = Vector(3.0, 4.0, 5.0)

    def test_x_prop(self):
        self.assertEqual(self.b.x, 3.0)

    def test_y_prop(self):
        self.assertEqual(self.b.y, 4.0)

    def test_z_prop(self):
        self.assertEqual(self.b.z, 5.0)

    def test_addition(self):
        c = self.a + self.b
        self.assertEqual(c, Vector(4.0, 5.0, 6.0))

    def test_subtraction(self):
        c = self.a - self.b
        self.assertEqual(c, Vector(-2.0, -3.0, -4.0))

    def test_division(self):
        c = self.a / 3
        v = 1 / 3
        self.assertEqual(c, Vector(v, v, v))

    def test_equality(self):
        self.assertNotEqual(self.a, self.b)

    def test_dot_product(self):
        c = self.a.dot(self.b)
        self.assertEqual(c, 12.0)
        c = self.b.dot(self.a)
        self.assertEqual(c, 12.0)

    def test_norm(self):
        c = self.a.norm()
        self.assertEqual(c, math.sqrt(3))
        c = self.a.normalize().norm()
        self.assertEqual(c, 1.0)

    def test_cross_product(self):
        c = self.a.cross(self.b)
        self.assertEqual(c, Vector(1, -2, 1))

    def test_normalize(self):
        c = self.a.normalize()
        v = 1 / math.sqrt(3)
        self.assertEqual(c, Vector(v, v, v))

    def test_getitem(self):
        self.assertEqual(self.a[0], 1.0)
        self.assertEqual(self.a[1], 1.0)
        self.assertEqual(self.a[2], 1.0)

        self.assertEqual(self.b[0], 3.0)
        self.assertEqual(self.b[1], 4.0)
        self.assertEqual(self.b[2], 5.0)

    def test_additive_inverse(self):
        self.assertEqual(-self.a, Vector(-1.0, -1.0, -1.0))

    def test_scalar_multiplication(self):
        c = self.a * 3
        self.assertEqual(c, Vector(3.0, 3.0, 3.0))
        c = 3 * self.a
        self.assertEqual(c, Vector(3.0, 3.0, 3.0))


unittest.main()
