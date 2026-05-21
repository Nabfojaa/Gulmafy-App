"""
Database utilities for Gulmafy application
"""
import json
import pandas as pd
import streamlit as st
from pathlib import Path

# Get the base directory
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
MONITORING_DIR = BASE_DIR / "monitoring"

@st.cache_data
def load_gulma_database():
    """Load weed database from JSON file"""
    try:
        with open(DATA_DIR / "gulma_database.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data["gulma"]
    except Exception as e:
        st.error(f"Error loading gulma database: {e}")
        return []

@st.cache_data
def load_jurnal_database():
    """Load journal database from JSON file"""
    try:
        with open(DATA_DIR / "jurnal_database.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data["jurnal"]
    except Exception as e:
        st.error(f"Error loading jurnal database: {e}")
        return []

def load_monitoring_data():
    """Load monitoring data from CSV file"""
    try:
        df = pd.read_csv(MONITORING_DIR / "monitoring_data.csv")
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["location", "gulma", "tingkat_serangan", "tanggal", "catatan"])
    except Exception as e:
        st.error(f"Error loading monitoring data: {e}")
        return pd.DataFrame()

def save_monitoring_data(data):
    """Save monitoring data to CSV file"""
    try:
        data.to_csv(MONITORING_DIR / "monitoring_data.csv", index=False)
        return True
    except Exception as e:
        st.error(f"Error saving monitoring data: {e}")
        return False

def get_gulma_by_id(gulma_id, database=None):
    """Get weed data by ID"""
    if database is None:
        database = load_gulma_database()
    
    for gulma in database:
        if gulma["id"] == gulma_id:
            return gulma
    return None

def get_gulma_by_name(name, database=None):
    """Get weed data by name"""
    if database is None:
        database = load_gulma_database()
    
    for gulma in database:
        if gulma["nama"].lower() == name.lower():
            return gulma
    return None

def get_all_gulma_names(database=None):
    """Get all weed names"""
    if database is None:
        database = load_gulma_database()
    
    return [gulma["nama"] for gulma in database]

def get_all_famili(database=None):
    """Get all weed families"""
    if database is None:
        database = load_gulma_database()
    
    famili_set = set()
    for gulma in database:
        famili_set.add(gulma["famili"])
    
    return sorted(list(famili_set))

def get_all_habitat(database=None):
    """Get all habitats"""
    if database is None:
        database = load_gulma_database()
    
    habitat_set = set()
    for gulma in database:
        if isinstance(gulma["habitat"], list):
            habitat_set.update(gulma["habitat"])
        else:
            habitat_set.add(gulma["habitat"])
    
    return sorted(list(habitat_set))

def get_gulma_by_habitat(habitat, database=None):
    """Get weeds by habitat"""
    if database is None:
        database = load_gulma_database()
    
    result = []
    for gulma in database:
        if isinstance(gulma["habitat"], list):
            if habitat in gulma["habitat"]:
                result.append(gulma)
        elif gulma["habitat"] == habitat:
            result.append(gulma)
    
    return result

def get_gulma_by_famili(famili, database=None):
    """Get weeds by family"""
    if database is None:
        database = load_gulma_database()
    
    return [gulma for gulma in database if gulma["famili"] == famili]

def get_gulma_by_danger_level(level, database=None):
    """Get weeds by danger level"""
    if database is None:
        database = load_gulma_database()
    
    return [gulma for gulma in database if gulma["tingkat_bahaya"] == level]

def get_most_dangerous_gulma(limit=5, database=None):
    """Get most dangerous weeds"""
    if database is None:
        database = load_gulma_database()
    
    sorted_gulma = sorted(database, key=lambda x: x["tingkat_bahaya"], reverse=True)
    return sorted_gulma[:limit]

def get_database_statistics():
    """Get database statistics"""
    database = load_gulma_database()
    jurnal = load_jurnal_database()
    
    stats = {
        "total_gulma": len(database),
        "total_famili": len(set(g["famili"] for g in database)),
        "total_jurnal": len(jurnal),
        "total_habitat": len(set(h for g in database for h in (g["habitat"] if isinstance(g["habitat"], list) else [g["habitat"]]))),
        "most_dangerous": get_most_dangerous_gulma(1, database)[0]["nama"] if database else "N/A",
        "dangerous_count": len([g for g in database if g["tingkat_bahaya"] >= 4])
    }
    
    return stats

def search_gulma(query, database=None):
    """Search weeds by query"""
    if database is None:
        database = load_gulma_database()
    
    query = query.lower()
    results = []
    
    for gulma in database:
        if (query in gulma["nama"].lower() or 
            query in gulma["nama_ilmiah"].lower() or
            query in gulma["famili"].lower()):
            results.append(gulma)
    
    return results
