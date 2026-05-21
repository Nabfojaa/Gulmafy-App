"""
Rule-based expert system for weed identification
"""
from utils.database_utils import load_gulma_database

class ExpertSystem:
    """Expert system for weed identification"""
    
    def __init__(self):
        self.database = load_gulma_database()
        self.weights = {
            "batang": 20,
            "daun": 25,
            "habitat": 20,
            "akar": 15,
            "bunga": 15,
            "pertumbuhan": 5
        }
    
    def normalize_feature(self, feature):
        """Normalize feature for comparison"""
        return feature.lower().strip()
    
    def calculate_match_score(self, gulma, user_features):
        """Calculate how well a weed matches user features"""
        total_score = 0
        matched_features = 0
        
        # Check bentuk batang
        if user_features.get("bentuk_batang"):
            batang_norm = self.normalize_feature(user_features["bentuk_batang"])
            gulma_batang = self.normalize_feature(str(gulma["morfologi"]["batang"]))
            
            if batang_norm in gulma_batang or self._similar_string(batang_norm, gulma_batang):
                total_score += self.weights["batang"]
                matched_features += 1
        
        # Check tipe daun
        if user_features.get("tipe_daun"):
            daun_norm = self.normalize_feature(user_features["tipe_daun"])
            gulma_daun = self.normalize_feature(str(gulma["morfologi"]["daun"]))
            ciri_daun = [self.normalize_feature(c) for c in gulma.get("ciri_khas", [])]
            
            if any(daun_norm in c or self._similar_string(daun_norm, c) for c in ciri_daun):
                total_score += self.weights["daun"]
                matched_features += 1
            elif daun_norm in gulma_daun:
                total_score += self.weights["daun"] * 0.7
                matched_features += 0.7
        
        # Check warna daun (simplified)
        if user_features.get("warna_daun"):
            warna_norm = self.normalize_feature(user_features["warna_daun"])
            if warna_norm in self.normalize_feature(str(gulma["morfologi"]["daun"])):
                total_score += self.weights["daun"] * 0.5
                matched_features += 0.5
        
        # Check habitat
        if user_features.get("habitat"):
            habitat_norm = self.normalize_feature(user_features["habitat"])
            gulma_habitat = [self.normalize_feature(h) for h in gulma["habitat"]]
            
            if any(habitat_norm in h or self._similar_string(habitat_norm, h) for h in gulma_habitat):
                total_score += self.weights["habitat"]
                matched_features += 1
            elif any(h in habitat_norm for h in gulma_habitat):
                total_score += self.weights["habitat"] * 0.7
                matched_features += 0.7
        
        # Check tipe akar
        if user_features.get("tipe_akar"):
            akar_norm = self.normalize_feature(user_features["tipe_akar"])
            gulma_akar = self.normalize_feature(str(gulma["morfologi"]["akar"]))
            
            if akar_norm in gulma_akar or self._similar_string(akar_norm, gulma_akar):
                total_score += self.weights["akar"]
                matched_features += 1
        
        # Check bunga
        if user_features.get("bunga"):
            bunga_norm = self.normalize_feature(user_features["bunga"])
            gulma_bunga = self.normalize_feature(str(gulma["morfologi"]["bunga"]))
            
            if bunga_norm in gulma_bunga or self._similar_string(bunga_norm, gulma_bunga):
                total_score += self.weights["bunga"]
                matched_features += 1
        
        # Check pola pertumbuhan
        if user_features.get("pola_pertumbuhan"):
            pola_norm = self.normalize_feature(user_features["pola_pertumbuhan"])
            ciri_khas = [self.normalize_feature(c) for c in gulma.get("ciri_khas", [])]
            
            if any(pola_norm in c or self._similar_string(pola_norm, c) for c in ciri_khas):
                total_score += self.weights["pertumbuhan"]
                matched_features += 1
        
        # Calculate confidence score
        max_possible = sum(self.weights.values()) if user_features else 1
        confidence = (total_score / max_possible * 100) if max_possible > 0 else 0
        
        return {
            "gulma": gulma,
            "score": total_score,
            "confidence": round(confidence, 1),
            "matched_features": matched_features
        }
    
    def _similar_string(self, str1, str2):
        """Check if two strings are similar (fuzzy matching)"""
        # Simple fuzzy matching - check if one is substring of other
        if len(str1) < 3 or len(str2) < 3:
            return False
        
        # Check overlapping characters
        common = sum(str1.count(c) for c in set(str1) if c in str2)
        similarity = common / max(len(str1), len(str2))
        
        return similarity > 0.5
    
    def identify_weed(self, user_features):
        """Identify weed based on user features"""
        results = []
        
        for gulma in self.database:
            result = self.calculate_match_score(gulma, user_features)
            if result["score"] > 0:
                results.append(result)
        
        # Sort by confidence score
        results.sort(key=lambda x: x["confidence"], reverse=True)
        
        return results
    
    def get_identification_with_threshold(self, user_features, threshold=20):
        """Get identification results above threshold"""
        results = self.identify_weed(user_features)
        
        # Filter by threshold
        filtered_results = [r for r in results if r["confidence"] >= threshold]
        
        return filtered_results if filtered_results else results[:3]

# Create singleton instance
expert_system = ExpertSystem()
