class RiskAnalyzer:
    def assess_risk(self, overlap_area, distance, voltage_kv, has_structure):
        score = 0

        score += 3 if overlap_area > 50 else 2 if overlap_area > 20 else 1
        score += 3 if distance < 5 else 2 if distance < 15 else 1
        score += 3 if voltage_kv >= 230 else 2 if voltage_kv >= 69 else 1

        if has_structure:
            score += 3

        if score >= 9:
            return "HIGH"
        elif score >= 6:
            return "MODERATE"
        return "LOW"