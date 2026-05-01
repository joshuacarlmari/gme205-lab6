class Report:
    def __init__(self, results):
        self.results = results

    def generate_table(self):
        print("\n=== AFFECTED PARCELS REPORT ===\n")

        for r in self.results:
            print(f"Parcel: {r['parcel_id']}")
            print(f"Owner: {r['owner']}")
            print(f"Parcel Area: {r['parcel_area']:.2f}")
            print(f"Overlap Area: {r['overlap_area']:.2f}")
            print(f"Risk Level: {r['risk']}")
            print(f"Location: {r['barangay']}, {r['municipality']}, {r['province']}")
            print("-----------------------------")

    def summary(self):
        total = len(self.results)
        high = sum(1 for r in self.results if r["risk"] == "HIGH")
        moderate = sum(1 for r in self.results if r["risk"] == "MODERATE")
        low = sum(1 for r in self.results if r["risk"] == "LOW")

        print("\n=== SUMMARY ===")
        print(f"Total Affected Parcels: {total}")
        print(f"High Risk Parcels: {high}")
        print(f"Moderate Risk Parcels: {moderate}")
        print(f"Low Risk Parcels: {low}")
