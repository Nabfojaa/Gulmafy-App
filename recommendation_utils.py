"""
Recommendation utilities for weed control
"""
from utils.database_utils import load_gulma_database

class RecommendationEngine:
    """Engine for generating weed control recommendations"""
    
    def __init__(self):
        self.database = load_gulma_database()
    
    def get_recommendations(self, gulma_name, attack_level=3, field_size=1, crop_type="Padi"):
        """
        Generate control recommendations
        
        Parameters:
        - gulma_name: Name of weed
        - attack_level: 1-5 severity level
        - field_size: Field size in hectares
        - crop_type: Type of crop
        """
        gulma = self._find_gulma(gulma_name)
        if not gulma:
            return None
        
        recommendations = {
            "gulma": gulma["nama"],
            "nama_ilmiah": gulma["nama_ilmiah"],
            "tingkat_bahaya": gulma["tingkat_bahaya"],
            "metode_mekanis": self._get_mekanis_recommendation(gulma, attack_level, field_size),
            "metode_biologis": gulma["pengendalian_biologis"],
            "metode_kultur": gulma["pengendalian_kultur_teknis"],
            "herbisida": self._get_herbisida_recommendation(gulma, field_size, attack_level),
            "prioritas": self._determine_priority(gulma, attack_level),
            "urgency": self._determine_urgency(gulma, attack_level)
        }
        
        return recommendations
    
    def _find_gulma(self, gulma_name):
        """Find weed by name"""
        for gulma in self.database:
            if gulma["nama"].lower() == gulma_name.lower():
                return gulma
        return None
    
    def _get_mekanis_recommendation(self, gulma, attack_level, field_size):
        """Generate mechanical control recommendation"""
        base_recommendation = gulma["pengendalian_mekanis"]
        
        if attack_level >= 4:
            additional = " (Intensitas serangan tinggi - perlukan tindakan cepat)"
        elif attack_level >= 3:
            additional = " (Serangan moderat - perlukan pengendalian rutin)"
        else:
            additional = " (Serangan ringan - pengendalian berkala)"
        
        # Add notes based on field size
        if field_size > 2:
            additional += f" - Untuk lahan {field_size} ha, pertimbangkan penggunaan mesin untuk efisiensi"
        
        return base_recommendation + additional
    
    def _get_herbisida_recommendation(self, gulma, field_size, attack_level):
        """Generate herbicide recommendation with dosage"""
        herbisida_list = []
        
        for i, herb in enumerate(gulma["herbisida"]):
            if i < len(gulma["dosis_herbisida"].split(",")):
                # Parse dosis if available
                dosis_str = gulma["dosis_herbisida"]
                
                rec = {
                    "nama": herb,
                    "dosis": dosis_str,
                    "waktu_aplikasi": gulma["waktu_aplikasi"],
                    "catatan": ""
                }
                
                # Add notes based on attack level
                if attack_level >= 4:
                    rec["catatan"] = "Serangan berat - pertimbangkan aplikasi berulang (7-10 hari)"
                elif attack_level >= 3:
                    rec["catatan"] = "Serangan moderat - satu kali aplikasi biasanya cukup"
                else:
                    rec["catatan"] = "Serangan ringan - monitor sebelum aplikasi"
                
                herbisida_list.append(rec)
        
        return herbisida_list
    
    def _determine_priority(self, gulma, attack_level):
        """Determine control priority"""
        if gulma["tingkat_bahaya"] >= 4 and attack_level >= 4:
            return "SANGAT URGENT - Pengendalian harus segera dilakukan"
        elif gulma["tingkat_bahaya"] >= 4 or attack_level >= 4:
            return "URGENT - Pengendalian dalam 1-2 minggu"
        elif gulma["tingkat_bahaya"] >= 3:
            return "PENTING - Pengendalian dalam 2-3 minggu"
        else:
            return "RUTIN - Pengendalian berkala"
    
    def _determine_urgency(self, gulma, attack_level):
        """Determine urgency level (1-5)"""
        urgency = min(5, max(1, gulma["tingkat_bahaya"] + (attack_level - 3) // 2))
        return urgency
    
    def compare_methods(self, gulma_name):
        """Compare different control methods"""
        gulma = self._find_gulma(gulma_name)
        if not gulma:
            return None
        
        comparison = {
            "gulma": gulma["nama"],
            "methods": [
                {
                    "metode": "Pengendalian Mekanis",
                    "deskripsi": gulma["pengendalian_mekanis"],
                    "efektivitas": "80-90%",
                    "biaya": "Sedang-Tinggi",
                    "waktu": "Panjang",
                    "ramah_lingkungan": "Ya"
                },
                {
                    "metode": "Pengendalian Biologis",
                    "deskripsi": gulma["pengendalian_biologis"],
                    "efektivitas": "60-70%",
                    "biaya": "Rendah-Sedang",
                    "waktu": "Panjang",
                    "ramah_lingkungan": "Ya"
                },
                {
                    "metode": "Pengendalian Kultur Teknis",
                    "deskripsi": gulma["pengendalian_kultur_teknis"],
                    "efektivitas": "70-85%",
                    "biaya": "Sedang",
                    "waktu": "Sedang",
                    "ramah_lingkungan": "Ya"
                },
                {
                    "metode": "Pengendalian Kimiawi",
                    "deskripsi": f"Herbisida: {', '.join(gulma['herbisida'])}",
                    "efektivitas": "90-95%",
                    "biaya": "Sedang",
                    "waktu": "Cepat",
                    "ramah_lingkungan": "Perlu Hati-hati"
                }
            ]
        }
        
        return comparison

# Create singleton instance
recommendation_engine = RecommendationEngine()
