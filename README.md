# Minimal Raytracer

A basic Python version of [tinyraytracer](https://github.com/ssloy/tinyraytracer)

Physically based rendering is an approach that tries to render images by approximating/simulating the flow of light.
## Requirements

This program only relies on the `requests` library

1. `requests` library (`pip install requests`)

Otherwise it works with built-ins and default libraries.
## Exercise

There are several `TODO`s to be found in the code.

### `Vector`
A good first step is to make the `Vector` test work. To run the unit tests on the `Vector` class simply run

```
python test_vector.py
```

and look at the output. If everything works correctly all tests will succeed.

### `tiny_raytracer`

There are also `TODO` throughout this file.

1. Implement the classes `SceneBase`, `Scene`, `Light`, `Sphere`, `Material`

### Classes

Here an overview of the classes used in `tiny_raytracer.py`
#### `SceneBase`

Base class for all objects in the scene. It contains a `__str__` method and a `to_json` which all derived classes have to implement
#### `Scene`

A scene contains a list of `lights` and a list of `spheres`


#### `Lights`

A light is composed of a position (3D vector) and an intensity.

#### `Spheres`

A sphere is composed of a radius, a center (3D vector) and a material
