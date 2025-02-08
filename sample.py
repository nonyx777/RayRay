import numpy as np
from PIL import Image
from Hitable import Scene, Sphere
from Material import Lambertian, Metal, Dielectric
from cli import render
from Camera import Camera
from Texture import *
from Light import *

image = Image.open("earth.jpg")
image = image.convert("RGB")
image_array = np.array(image)

tan_texture = ConstantTexture(np.array([0.6, 0.6, 0.2]))
blue_texture = ConstantTexture(np.array([0.2, 0.2, 0.5]))
gray_texture = ConstantTexture(np.array([0.2, 0.2, 0.2]))
checker_texture = CheckerTexture(ConstantTexture(np.array([0.2, 0.3, 0.1])), ConstantTexture(np.array([0.9, 0.9, 0.9])))
image_texture = ImageTexture(image_array, image_array.shape[1], image_array.shape[0])
diffuse_light_texture = ConstantTexture(np.array([4.0, 4.0, 4.0]))

tan = Metal(tan_texture)
blue = Lambertian(image_texture)
gray = Lambertian(checker_texture)
transparent = Dielectric(1.5)
light = DiffuseLight(diffuse_light_texture)

scene = Scene([
    Sphere(np.array([-0.9, 0, 1]), 0.5, transparent),
    Sphere(np.array([-0.5,0,0]), 0.5, tan),
    Sphere(np.array([0.7,0,0]), 0.5, blue),
    Sphere(np.array([0,-40,0]), 39.5, gray),
    Sphere(np.array([0.2, 0.7, 1]), 0.5, light),
])

camera = Camera(np.array([3,1.2,5]), target=np.array([-0.5,0,0]), vfov=24, aspect=16/9, aperture=0.0)

render(camera, scene)