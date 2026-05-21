"""
Lightweight AI Engine for GULMAFY
Modern similarity scoring & smart recommendations
"""
import numpy as np
from rapidfuzz import fuzz
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

class SimilarityAI:
    """Lightweight similarity-based AI for weed identification"""
    
    def __init__(self):
        self.scaler = MinMaxScaler(feature_range=(0, 100))
    
    def calculate_morphology_similarity(self, user_features, weed_features):
        """
        Calculate similarity between user input and weed morphology
        Uses weighted scoring for each morphology attribute
        """
        if not weed_features or not user_features:
            return 0
        
        similarity_scores = []
        weights = {
            "bentuk_batang": 0.12,
            "tipe_daun": 0.15,
            "warna_daun": 0.10,
            "tipe_akar": 0.13,
            "habitat": 0.15,
            "bunga": 0.12,
            "pola_pertumbuhan": 0.13,
        }
        
        total_weight = 0
        weighted_score = 0
        
        for key, weight in weights.items():
            user_val = str(user_features.get(key, "")).lower().strip()
            weed_val = str(weed_features.get(key, "")).lower().strip()
            
            if user_val and weed_val:
                # Use RapidFuzz for smart string matching
                ratio = fuzz.token_set_ratio(user_val, weed_val) / 100.0
                weighted_score += ratio * weight
                total_weight += weight
            elif not user_val:
                # If user didn't input this feature, give neutral weight
                total_weight += weight
        
        if total_weight == 0:
            return 0
        
        return min(100, (weighted_score / total_weight) * 100)
    
    def calculate_habitat_match(self, user_habitat, weed_habitats):
        """Calculate habitat matching score"""
        if not user_habitat or not weed_habitats:
            return 0
        
        user_h = str(user_habitat).lower().strip()
        
        habitats_list = weed_habitats if isinstance(weed_habitats, list) else [str(weed_habitats)]
        
        max_score = 0
        for weed_h in habitats_list:
            weed_h = str(weed_h).lower().strip()
            score = fuzz.token_set_ratio(user_h, weed_h) / 100.0
            max_score = max(max_score, score)
        
        return max_score * 100
    
    def calculate_confidence(self, morphology_score, habitat_score, user_features_count, max_features=7):
        """
        Calculate AI confidence based on:
        - Morphology matching
        - Habitat matching
        - Number of features provided
        """
        # Base confidence from morphology
        morphology_confidence = morphology_score * 0.5
        
        # Habitat confidence
        habitat_confidence = habitat_score * 0.3 if habitat_score > 0 else 0
        
        # Feature completeness bonus
        completeness = min(user_features_count / max_features, 1.0)
        completeness_bonus = completeness * 20
        
        total_confidence = morphology_confidence + habitat_confidence + completeness_bonus
        
        return min(100, max(0, total_confidence))
    
    def rank_weeds(self, user_features, weed_database):
        """
        Rank weeds based on similarity to user input
        Returns top matches with confidence scores
        """
        results = []
        
        for weed in weed_database:
            # Calculate morphology match
            morphology_score = self.calculate_morphology_similarity(
                user_features, 
                weed.get("morfologi", {})
            )
            
            # Calculate habitat match
            habitat_score = self.calculate_habitat_match(
                user_features.get("habitat"),
                weed.get("habitat", [])
            )
            
            # Calculate confidence
            feature_count = len([v for v in user_features.values() if v])
            confidence = self.calculate_confidence(
                morphology_score,
                habitat_score,
                feature_count
            )
            
            results.append({
                "weed": weed,
                "morphology_score": morphology_score,
                "habitat_score": habitat_score,
                "confidence": round(confidence, 1),
                "rank_score": (morphology_score * 0.6 + habitat_score * 0.4)  # For ranking
            })
        
        # Sort by confidence
        results = sorted(results, key=lambda x: x["confidence"], reverse=True)
        
        return results


class SmartRecommendationEngine:
    """AI-powered recommendations for weed control"""
    
    @staticmethod
    def get_best_control_method(weed_data, habitat, danger_level):
        """
        Recommend best control method based on:
        - Weed characteristics
        - Habitat
        - Danger level
        """
        recommendations = []
        
        # Danger level 4-5: Aggressive methods
        if danger_level >= 4:
            if habitat == "Sawah":
                recommendations.append({
                    "method": "Kimia (Herbisida Selektif)",
                    "priority": "UTAMA",
                    "effectiveness": 95,
                    "reason": "Gulma berbahaya di sawah memerlukan kontrol cepat dengan herbisida"
                })
            recommendations.append({
                "method": "Kombinasi Mekanis + Kimia",
                "priority": "TINGGI",
                "effectiveness": 90,
                "reason": "Kontrol menyeluruh untuk gulma dengan tingkat bahaya tinggi"
            })
        
        # Danger level 2-3: Moderate methods
        elif danger_level >= 2:
            recommendations.append({
                "method": "Kultur Teknis + Pengendalian Manual",
                "priority": "SEDANG",
                "effectiveness": 75,
                "reason": "Efektif untuk tingkat bahaya sedang dengan environmental care"
            })
            if habitat in ["Tegalan", "Kebun"]:
                recommendations.append({
                    "method": "Pengendalian Manual",
                    "priority": "SEDANG",
                    "effectiveness": 70,
                    "reason": "Cocok untuk area non-sawah dengan populasi menengah"
                })
        
        # Danger level 1: Gentle methods
        else:
            recommendations.append({
                "method": "Pemantauan & Pengendalian Manual",
                "priority": "RENDAH",
                "effectiveness": 60,
                "reason": "Gulma dengan populasi rendah dapat dikendalikan secara manual"
            })
        
        return recommendations
    
    @staticmethod
    def get_herbicide_recommendation(weed_name, habitat, danger_level, weed_data=None):
        """
        Smart herbicide recommendation
        """
        recommendations = []
        
        # Check weed database for specific herbicides
        if weed_data:
            if "herbisida" in weed_data:
                for herb in weed_data["herbisida"][:3]:
                    recommendations.append({
                        "name": herb,
                        "confidence": 90,
                        "source": "Database Spesifik"
                    })
        
        # Generic recommendations by habitat
        habitat_herbicides = {
            "Sawah": [
                {"name": "2,4-D", "confidence": 85, "dosis": "0.8 L/ha"},
                {"name": "Anilofos", "confidence": 88, "dosis": "2.5 L/ha"},
                {"name": "Pendimethalin", "confidence": 82, "dosis": "3.75 L/ha"}
            ],
            "Tegalan": [
                {"name": "Paraquat", "confidence": 80, "dosis": "1-2 L/ha"},
                {"name": "Glifosad", "confidence": 85, "dosis": "2-4 L/ha"},
                {"name": "Metolakhlor", "confidence": 80, "dosis": "2.5 L/ha"}
            ],
            "Kebun": [
                {"name": "Glifosad", "confidence": 80, "dosis": "2-4 L/ha"},
                {"name": "Parakuat + Diquat", "confidence": 78, "dosis": "1.5-3 L/ha"}
            ]
        }
        
        if habitat in habitat_herbicides:
            for herb in habitat_herbicides[habitat][:3]:
                if herb not in recommendations:
                    recommendations.append(herb)
        
        return recommendations[:3]  # Return top 3


class InsightGenerator:
    """Generate smart AI insights about weeds"""
    
    @staticmethod
    def generate_weed_insights(weed_data, danger_level, habitat):
        """Generate actionable insights about a weed"""
        insights = []
        
        # Danger level insight
        if danger_level == 5:
            insights.append({
                "type": "danger",
                "icon": "🚨",
                "title": "ANCAMAN KRITIS",
                "message": "Gulma ini sangat berbahaya. Tindakan pengendalian SEGERA diperlukan.",
                "severity": "critical"
            })
        elif danger_level >= 4:
            insights.append({
                "type": "danger",
                "icon": "⚠️",
                "title": "Tingkat Bahaya Tinggi",
                "message": "Gulma ini memerlukan strategi pengendalian agresif.",
                "severity": "high"
            })
        
        # Habitat insight
        if habitat:
            insights.append({
                "type": "habitat",
                "icon": "🌍",
                "title": f"Habitat: {habitat}",
                "message": f"Gulma ini optimal tumbuh di {habitat}. Jaga kondisi lahan.",
                "severity": "info"
            })
        
        # Invasiveness insight
        if danger_level >= 4:
            insights.append({
                "type": "invasive",
                "icon": "📈",
                "title": "Gulma Invasif",
                "message": "Gulma ini cepat menyebar. Monitor ketat dan kontrol proaktif diperlukan.",
                "severity": "warning"
            })
        
        # Benefit insight
        if weed_data and "manfaat" in weed_data and weed_data["manfaat"]:
            insights.append({
                "type": "benefit",
                "icon": "✅",
                "title": "Potensi Manfaat",
                "message": weed_data["manfaat"],
                "severity": "positive"
            })
        
        return insights


# Initialize AI engines as singletons
similarity_ai = SimilarityAI()
recommendation_engine = SmartRecommendationEngine()
insight_generator = InsightGenerator()
