import numpy as np

class Hit:
    def __init__(self, t, point=None, normal=None, material=None):
        self.t = t
        self.point = point
        self.normal = normal
        self.material = material

no_hit = Hit(np.inf)

class Hitable:
    def __init__(self, material = None):
        self.material = material
    def intersect(self, ray):
        pass

class Scene(Hitable):
    def __init__(self, surfs, bg_color=np.array([0.2, 0.3, 0.5])):
        self.surfs = surfs
        self.bg_color = bg_color
    def intersect(self, ray):
        closest_hit = no_hit
        for surf in self.surfs:
            hit = surf.intersect(ray)
            if hit.t < closest_hit.t:
                closest_hit = hit
        
        return closest_hit

class Sphere(Hitable):
    def __init__(self, center, radius, material):
        super().__init__(material = material)
        self.center = center
        self.radius = radius
    def intersect(self, ray):
        # pre-compute
        r_sq = pow(self.radius, 2)

        l = self.center - ray.origin
        s = l.dot(ray.direction)
        l_sq = l.dot(l)
        if s < 0 and l_sq > r_sq:
          return no_hit
        m_sq = l_sq - pow(s, 2)
        if m_sq > r_sq:
          return no_hit
        q = np.sqrt(r_sq - m_sq)
        if l_sq > r_sq:
          t = s - q
        else:
          t = s + q
        ray_direction_normalized = np.divide(ray.direction, np.linalg.norm(ray.direction))
        point = ray.origin + t * ray_direction_normalized
        surface_normal = point - self.center
        return Hit(t, point, np.divide(surface_normal,np.linalg.norm(surface_normal)), self.material)