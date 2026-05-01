from risk import RiskAnalyzer
from report import Report

class EasementChecker:
    def __init__(self, parcels, easements):
        self.parcels = parcels
        self.easements = easements
        self.risk_analyzer = RiskAnalyzer()

    def find_affected_parcels(self):
        results = []

        for parcel in self.parcels:
            for easement in self.easements:
                corridor = easement.get_corridor()

                if parcel.intersects(corridor):
                    overlap_geom = parcel.intersection(corridor)
                    overlap_area = overlap_geom.area

                    distance = parcel.distance(corridor)
                    has_structure = overlap_area > 10

                    risk = self.risk_analyzer.assess_risk(
                        overlap_area,
                        distance,
                        easement.voltage_kv,
                        has_structure
                    )

                    results.append({
                        "parcel_id": parcel.get_id(),
                        "owner": parcel.owner,
                        "parcel_area": parcel.area,
                        "overlap_area": overlap_area,
                        "risk": risk,
                        "barangay": parcel.barangay.name,
                        "municipality": parcel.barangay.municipality.name,
                        "province": parcel.barangay.municipality.province.name
                    })

        return Report(results)
