from shapely.geometry import Polygon, LineString

from admin_units import Province, Municipality, Barangay
from parcel import Parcel
from transmission import TransmissionLineEasement
from checker import EasementChecker


def main():

    province = Province("Metro Manila")
    municipality = Municipality("Quezon City", province)
    brgy1 = Barangay("Barangay 1", municipality)
    brgy2 = Barangay("Barangay 2", municipality)

    parcels = [
    Parcel(
        "2931",
        "Juan Dela Cruz",
        brgy1,
        Polygon([(0,0), (10,0), (10,10), (0,10)])
    ),

    Parcel(
        "2932",
        "Maria Santos",
        brgy2,
        Polygon([(12,0), (20,0), (20,10), (12,10)])
    ),

    Parcel(
        "2933",
        "Pedro Reyes",
        brgy1,
        Polygon([
            (8, 2),
            (14, 2),
            (14, 12),
            (8, 12)
        ])
    )
]

    easements = [
        TransmissionLineEasement(
            "TL-01",
            LineString([(12,-5), (12,15)]),
            width_m=6,
            voltage_kv=230
        )
    ]

    checker = EasementChecker(parcels, easements)
    report = checker.find_affected_parcels()

    report.generate_table()
    report.summary()


if __name__ == "__main__":
    main()