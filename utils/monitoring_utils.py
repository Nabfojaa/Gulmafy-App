"""
Monitoring utilities for weed tracking
"""
import pandas as pd
from datetime import datetime
from utils.database_utils import load_monitoring_data, save_monitoring_data

class MonitoringSystem:
    """System for weed monitoring"""
    
    def __init__(self):
        self.data = load_monitoring_data()
    
    def save_monitoring_data(self, data=None):
        """Save monitoring data to CSV file"""
        if data is None:
            data = self.data
        return save_monitoring_data(data)
    
    def add_record(self, location, gulma, attack_level, notes=""):
        """Add a new monitoring record"""
        new_record = pd.DataFrame({
            "location": [location],
            "gulma": [gulma],
            "tingkat_serangan": [attack_level],
            "tanggal": [datetime.now().strftime("%Y-%m-%d")],
            "catatan": [notes]
        })
        
        self.data = pd.concat([self.data, new_record], ignore_index=True)
        return save_monitoring_data(self.data)
    
    def get_records(self, location=None, gulma=None):
        """Get monitoring records filtered by criteria"""
        result = self.data.copy()
        
        if location:
            result = result[result["location"].str.contains(location, case=False, na=False)]
        
        if gulma:
            result = result[result["gulma"].str.contains(gulma, case=False, na=False)]
        
        # Normalize datetime to handle mixed formats
        result["tanggal"] = pd.to_datetime(result["tanggal"], errors="coerce")
        result = result.dropna(subset=["tanggal"])
        
        return result.sort_values("tanggal", ascending=False)
    
    def get_statistics(self):
        """Get monitoring statistics"""
        if self.data.empty:
            return {
                "total_records": 0,
                "total_locations": 0,
                "total_weeds": 0,
                "average_attack": 0,
                "most_recorded_weed": "N/A"
            }
        
        # Count unique locations
        total_locations = self.data["location"].nunique()
        
        # Count unique weeds
        total_weeds = len(set([w.strip() for weed_str in self.data["gulma"] 
                               for w in weed_str.split(",")]))
        
        # Average attack level
        average_attack = self.data["tingkat_serangan"].mean()
        
        # Most recorded weed
        weed_counts = {}
        for weed_str in self.data["gulma"]:
            for weed in weed_str.split(","):
                weed = weed.strip()
                weed_counts[weed] = weed_counts.get(weed, 0) + 1
        
        most_recorded = max(weed_counts, key=weed_counts.get) if weed_counts else "N/A"
        
        stats = {
            "total_records": len(self.data),
            "total_locations": total_locations,
            "total_weeds": total_weeds,
            "average_attack": round(average_attack, 1),
            "most_recorded_weed": most_recorded,
            "most_recorded_count": weed_counts.get(most_recorded, 0) if most_recorded != "N/A" else 0
        }
        
        return stats
    
    def get_location_statistics(self):
        """Get statistics by location"""
        if self.data.empty:
            return pd.DataFrame()
        
        location_stats = self.data.groupby("location").agg({
            "tingkat_serangan": ["mean", "max", "min", "count"],
            "gulma": "first"
        }).round(1)
        
        location_stats.columns = ["Rata-rata", "Tertinggi", "Terendah", "Jumlah Record", "Gulma Utama"]
        
        return location_stats
    
    def get_weed_statistics(self):
        """Get statistics by weed"""
        if self.data.empty:
            return pd.DataFrame()
        
        # Parse weeds and attack levels
        weed_data = []
        
        for idx, row in self.data.iterrows():
            weeds = [w.strip() for w in str(row["gulma"]).split(",")]
            for weed in weeds:
                weed_data.append({
                    "gulma": weed,
                    "tingkat_serangan": row["tingkat_serangan"],
                    "lokasi": row["location"]
                })
        
        if not weed_data:
            return pd.DataFrame()
        
        weed_df = pd.DataFrame(weed_data)
        weed_stats = weed_df.groupby("gulma").agg({
            "tingkat_serangan": ["mean", "max", "min", "count"],
            "lokasi": lambda x: x.nunique()
        }).round(1)
        
        weed_stats.columns = ["Rata-rata", "Tertinggi", "Terendah", "Jumlah Record", "Lokasi Unik"]
        weed_stats = weed_stats.sort_values("Rata-rata", ascending=False)
        
        return weed_stats
    
    def get_trends(self):
        """Get monitoring trends over time"""
        if self.data.empty:
            return pd.DataFrame()
        
        # Create a copy and normalize datetime with error handling
        data_copy = self.data.copy()
        data_copy["tanggal"] = pd.to_datetime(data_copy["tanggal"], errors="coerce")
        data_copy = data_copy.dropna(subset=["tanggal"])
        
        if data_copy.empty:
            return pd.DataFrame()
        
        trends = data_copy.groupby("tanggal")["tingkat_serangan"].agg(["mean", "max", "count"])
        trends = trends.sort_index()
        
        return trends
    
    def delete_record(self, index):
        """Delete a monitoring record by index"""
        try:
            self.data = self.data.drop(index).reset_index(drop=True)
            return save_monitoring_data(self.data)
        except Exception as e:
            print(f"Error deleting record: {str(e)}")
            return False
    
    def update_record(self, original_index, location=None, gulma=None, 
                      tingkat_serangan=None, catatan=None):
        """Update a monitoring record"""
        try:
            if original_index < 0 or original_index >= len(self.data):
                return False
            
            if location is not None:
                self.data.loc[original_index, "location"] = location
            if gulma is not None:
                self.data.loc[original_index, "gulma"] = gulma
            if tingkat_serangan is not None:
                self.data.loc[original_index, "tingkat_serangan"] = tingkat_serangan
            if catatan is not None:
                self.data.loc[original_index, "catatan"] = catatan
            
            return save_monitoring_data(self.data)
        except Exception as e:
            print(f"Error updating record: {str(e)}")
            return False
    
    def export_data(self, format="csv"):
        """Export monitoring data"""
        if format == "csv":
            return self.data.to_csv(index=False)
        elif format == "json":
            return self.data.to_json(orient="records", indent=2)
        else:
            return self.data.to_excel(index=False)

# Create singleton instance
monitoring_system = MonitoringSystem()
