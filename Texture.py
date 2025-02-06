import numpy as np

class Texture:
    def value(self, u: float, v: float, p: np.ndarray) -> np.ndarray:
        pass

class ConstantTexture(Texture):
    def __init__(self, color: np.ndarray):
        self.color = color
    def value(self, u: float, v: float, p: np.ndarray) -> np.ndarray:
        return self.color

class CheckerTexture(Texture):
    def __init__(self, t0: Texture, t1: Texture):
        self.even = t0
        self.odd = t1
    def value(self, u: float, v: float, p:np.ndarray) -> np.ndarray:
        sines: float = np.sin(10*p[0]) * np.sin(10*p[1]) * np.sin(10*p[2])
        if sines < 0:
            return self.odd.value(u, v, p)
        else:
            return self.even.value(u, v, p)

class ImageTexture(Texture):
    def __init__(self, pixels, nx, ny):
        self.data = pixels
        self.nx = nx
        self.ny = ny
    def value(self, u: float, v: float, p: np.ndarray) -> np.ndarray:
        i: int = int(u*self.nx)
        j: int = int(v*self.ny)
        i = 0 if i < 0 else self.nx-1 if i > self.nx-1 else i
        j = 0 if j < 0 else self.ny-1 if j > self.ny-1 else j

        rgb: np.ndarray = self.data[j, i] / 255.0
        return rgb