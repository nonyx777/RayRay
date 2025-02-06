import numpy as np
from Hitable import Scene, Sphere
from Material import Lambertian, Metal, Dielectric
from cli import render
from Camera import Camera

tan = Metal(np.array([0.6, 0.6, 0.2]))
blue = Lambertian(np.array([0.2, 0.2, 0.5]))
gray = Lambertian(np.array([0.2, 0.2, 0.2]))
transparent = Dielectric(1.5)

scene = Scene([
    Sphere(np.array([-0.9, 0, 1]), 0.5, transparent),
    Sphere(np.array([-0.5,0,0]), 0.5, tan),
    Sphere(np.array([0.7,0,0]), 0.5, blue),
    Sphere(np.array([0,-40,0]), 39.5, gray),
])

camera = Camera(np.array([3,1.2,5]), target=np.array([-0.5,0,0]), vfov=24, aspect=16/9, aperture=0.5)

render(camera, scene)