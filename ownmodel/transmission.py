from spatial_object import SpatialObject

class TransmissionLineEasement(SpatialObject):
    def __init__(self, line_id, geometry, width_m, voltage_kv):
        super().__init__(geometry)
        self.line_id = line_id
        self.width_m = width_m
        self.voltage_kv = voltage_kv

    def get_corridor(self):
        """
        Returns the buffered corridor geometry around the transmission line.
        Width is divided by 2 since buffer expands equally on both sides.
        """
        return self.geometry.buffer(self.width_m / 2)

    def get_id(self):
        return self.line_id
