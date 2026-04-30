from shapely.geometry import Point, Polygon, LineString

class SpatialObject:
    def __init__(self, geometry):
        self.geometry = geometry

    @property
    def area(self):
        return self.geometry.area

    @property
    def length(self):
        return self.geometry.length

    def intersects(self, other):
        if isinstance(other, SpatialObject):
            return self.geometry.intersects(other.geometry)
        else:
            return self.geometry.intersects(other)

    def intersection(self, other):
        if isinstance(other, SpatialObject):
            return self.geometry.intersection(other.geometry)
        else:
            return self.geometry.intersection(other)

    def distance(self, other):
        if isinstance(other, SpatialObject):
            return self.geometry.distance(other.geometry)
        else:
            return self.geometry.distance(other)
