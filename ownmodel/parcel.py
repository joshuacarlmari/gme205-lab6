from spatial_object import SpatialObject

class Parcel(SpatialObject):
    def __init__(self, lot_no, owner, barangay, geometry):
        super().__init__(geometry)

        self.lot_no = lot_no
        self.owner = owner
        self.barangay = barangay

        barangay.add_parcel(self)

    def cadastral_id(self):
        return (
            f"{self.barangay.municipality.province.name}-"
            f"{self.barangay.municipality.name}-"
            f"{self.barangay.name}-"
            f"{self.lot_no}"
        )

    def get_id(self):
        return self.cadastral_id()