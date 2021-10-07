import unittest
from tiny_raytracer import Material
from vector import Vector


class MaterialTests(unittest.TestCase):
    def setUp(self):
        self.albedo = Vector(1.0, 0.8, 0.0, 0.3)
        self.name = "test"
        self.diffuse_color = Vector(0.8, 0.7, 0.3)
        self.specular_exponent = 100
        self.refractive_index = 1.2
        self.material = Material(
            self.name,
            self.refractive_index,
            self.albedo,
            self.diffuse_color,
            self.specular_exponent,
        )
        self.material_string = '{"name": "test", "refractive_index": 1.2, "albedo": "[1.0, 0.8, 0.0, 0.3]", "diffuse_color": "[0.8, 0.7, 0.3]", "specular_exponent": 100}'
        self.material_dict = {
            "name": "test",
            "refractive_index": 1.2,
            "albedo": [1.0, 0.8, 0.0, 0.3],
            "diffuse_color": [0.8, 0.7, 0.3],
            "specular_exponent": 100,
        }

    def test_constructors_arguments(self):
        material1 = Material(self.material_dict)
        material2 = Material(self.material_string)
        self.assertTrue(material1, material2)

    def test_to_json(self):
        self.assertTrue(self.material.to_json(), self.material_string)


unittest.main()
