import math
import sys
from vector import Vector
import requests as req

float_max = sys.float_info.max


class SceneBase:
    def __str__(self):
        raise NotImplementedError(
            "This function should be implemented in derived classes."
        )

    def to_json(self):
        raise NotImplementedError(
            "This function should be implemented in derived classes."
        )

    def from_json(self, json):
        raise NotImplementedError(
            "This function should be implemented in derived classes."
        )


class Scene(SceneBase):
    # TODO: Implement constructor

    # TODO: Implement __getitem__

    # TODO: Implement __str__

    # TODO: Implement to_json

    # TODO: Implement from_json
    pass


class Light(SceneBase):
    # TODO: Implement constructor

    # TODO: Implement __str__

    # TODO: Implement to_json

    pass


class Material(SceneBase):
    # TODO: Implement constructor

    # TODO: Implement __str__

    # TODO: Implement to_json

    pass


class Sphere(SceneBase):
    # TODO: Implement constructor

    # TODO: Implement __str__

    # TODO: Implement to_json

    pass


def ray_sphere_intersect(origin, direction, sphere):
    l = sphere.center - origin
    tca = l.dot(direction)
    d2 = l.dot(l) - tca * tca
    if d2 > sphere.radius * sphere.radius:
        return (False, 0)
    thc = math.sqrt(sphere.radius * sphere.radius - d2)
    t0 = tca - thc
    t1 = tca + thc
    if t0 < 1e-3:
        t0 = t1
    if t0 < 1e-3:
        return (False, 0)

    return (True, t0)


def reflect(incoming, normal):
    return incoming - normal * 2.0 * (incoming.dot(normal))


def refract(incoming, normal, eta_t, eta_i=1.0):
    cosi = -max(-1.0, min(1.0, incoming.dot(normal)))
    if cosi < 0:
        return refract(incoming, -normal, eta_i, eta_t)
    eta = eta_i / eta_t
    k = 1 - eta * eta * (1 - cosi * cosi)
    if k < 0:
        return Vector(1, 0, 0)
    else:
        return incoming * eta + normal * (eta * cosi - math.sqrt(k))


def scene_intersect(origin, direction, spheres):
    spheres_dist = float_max
    hit = None
    normal = None
    material = None
    for sphere in spheres:
        res = ray_sphere_intersect(origin, direction, sphere)
        if res[0] and res[1] < spheres_dist:
            spheres_dist = res[1]
            hit = origin + direction * spheres_dist
            normal = (hit - sphere.center).normalize()
            material = sphere.material

    checkerboard_dist = float_max
    if abs(direction.y) > 1e-3:
        d = -(origin.y + 4) / direction.y
        pt = origin + direction * d
        if (
            d > 1e-3
            and abs(pt.x) < 10
            and pt.z < -10
            and pt.z > -30
            and d < spheres_dist
        ):
            checkerboard_dist = d
            hit = pt
            normal = Vector(0, 1, 0)
            diffuse_color = (
                Vector(0.3, 0.3, 0.3)
                if (int(0.5 * hit.x + 1000) + int(0.5 * hit.z)) & 1
                else Vector(0.3, 0.2, 0.1)
            )
            material = Material("checkerboard", 1, Vector(1, 0, 0, 0), diffuse_color, 0)

    return (min(spheres_dist, checkerboard_dist) < 1000, hit, normal, material)


def cast_ray(origin, direction, spheres, lights, depth=0):

    if depth > 4:
        return Vector(0.2, 0.7, 0.8)
    has_hit, point, normal, material = scene_intersect(origin, direction, spheres)
    if not has_hit:
        return Vector(0.2, 0.7, 0.8)

    reflect_dir = reflect(direction, normal).normalize()
    refract_dir = refract(direction, normal, material.refractive_index).normalize()
    reflect_color = cast_ray(point, reflect_dir, spheres, lights, depth + 1)
    refract_color = cast_ray(point, refract_dir, spheres, lights, depth + 1)

    diffuse_light_intensity = 0
    specular_light_intensity = 0
    for light in lights:
        light_dir = (light.position - point).normalize()

        has_hit, shadow_pt, _, _ = scene_intersect(point, light_dir, spheres)
        if has_hit and (shadow_pt - point).norm() < (light.position - point).norm():
            continue

        diffuse_light_intensity += light.intensity * max(0.0, light_dir.dot(normal))
        specular_light_intensity += (
            math.pow(
                max(0.0, -reflect(-light_dir, normal).dot(direction)),
                material.specular_exponent,
            )
            * light.intensity
        )
    return (
        material.diffuse_color * diffuse_light_intensity * material.albedo[0]
        + Vector(1.0, 1.0, 1.0) * specular_light_intensity * material.albedo[1]
        + reflect_color * material.albedo[2]
        + refract_color * material.albedo[3]
    )


def render(scene):
    width = 400
    height = 200
    fov = math.pi / 3.0
    framebuffer = width * height * [None]
    for j in range(height):
        for i in range(width):
            dir_x = (i + 0.5) - width / 2.0
            dir_y = -(j + 0.5) + height / 2.0
            dir_z = -height / (2.0 * math.tan(fov / 2.0))
            framebuffer[i + j * width] = cast_ray(
                Vector(0, 0, 0),
                Vector(dir_x, dir_y, dir_z).normalize(),
                scene["spheres"],
                scene["lights"],
            )

    with open("out.ppm", "wb") as f:
        f.write(bytearray(f"P6 {width} {height} 255\n", "ascii"))
        counter = 0
        for vec in framebuffer:
            counter += 1
            max_c = max(vec[0], max(vec[1], vec[2]))
            if max_c > 1:
                vec = vec * 1 / max_c
            vec = bytes([int(255 * vec[0]), int(255 * vec[1]), int(255 * vec[2])])
            f.write(vec)


def read_scene(url):
    lights = []
    spheres = []
    materials = {}

    # TODO: Get text from url and parse the scene

    return Scene(lights=lights, spheres=spheres)


def write_scene_to_file(scene, file_name):
    with open(file_name, "w") as f:
        scene_string = scene.to_json()
        f.write(scene_string)


def load_scene_from_file(file_name):
    scene = Scene()
    with open(file_name, "r") as f:
        for line in f:
            scene.from_json(line)
            return scene


def main():
    scene = read_scene(
        "https://gist.githubusercontent.com/fibbo/1cee2353e67dba182f8f3c6d275c23ba/raw/1b43758911f801d2369c59004360e66826832f92/scene_01.txt"
    )

    print(scene)
    render(scene)


main()