class SpatialObject:
    def __init__(self, geometry):
        self.geometry = geometry

    def area(self):
        return getattr(self.geometry, "area", 0)

    def length(self):
        return getattr(self.geometry, "length", 0)

    def intersects(self, other):
        return self.geometry.intersects(other.geometry)

    def intersection(self, other):
        return self.geometry.intersection(other.geometry)

    def distance_to(self, other):
        return self.geometry.distance(other.geometry)

    @abstractmethod
    def get_id(self):
        pass