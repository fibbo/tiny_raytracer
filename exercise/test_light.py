import unittest
from tiny_raytracer import Light
from vector import Vector


class LightTests(unittest.TestCase):
    def setUp(self):
        self.json_form = '{"position": "[3.0, 1.0, 2.0]", "intensity": 1.2}'
        self.light = Light(Vector(3.0, 1.0, 2.0), 1.2)
        self.light_dict = {"position": [3.0, 1.0, 2.0], "intensity": 1.2}
        self.light_string = self.json_form

    def test_constructors_arguments(self):
        light3 = Light(Vector(3.0, 1.0, 2.0), 1.2)
        light1 = Light(self.light_dict)
        light2 = Light(self.light_string)
        self.assertEqual(light1, light2)
        self.assertEqual(light2, light3)

    def test_to_json(self):
        self.assertEqual(self.light.to_json(), self.json_form)


unittest.main()
