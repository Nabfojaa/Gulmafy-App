"""
Image utilities for Gulmafy application
Handles automatic loading of weed images
"""
import os
from pathlib import Path
import streamlit as st

# Get the base directory
BASE_DIR = Path(__file__).parent.parent
IMAGE_DIR = BASE_DIR / "data" / "Gambar gulma"

SUPPORTED_FORMATS = [".jpg", ".jpeg", ".png", ".webp"]

def normalize_filename(text):
    """Normalize text for filename matching"""
    return text.strip().lower()

def find_weed_image(weed_name):
    """
    Find and return path to weed image
    
    Args:
        weed_name: Name of the weed (e.g., "Bandotan")
    
    Returns:
        Path object to image or None if not found
    """
    if not weed_name or not IMAGE_DIR.exists():
        return None
    
    # Normalize the search name
    search_name = normalize_filename(weed_name)
    
    # Try exact match first (case-insensitive)
    for ext in SUPPORTED_FORMATS:
        for file in IMAGE_DIR.glob(f"*{ext}"):
            if normalize_filename(file.stem) == search_name:
                return file
    
    # Try partial match if exact not found
    for file in IMAGE_DIR.glob("*"):
        if file.is_file() and file.suffix.lower() in SUPPORTED_FORMATS:
            if search_name in normalize_filename(file.stem):
                return file
    
    return None

def display_weed_image(weed_name, width=None, stretch=False):
    """
    Display weed image in Streamlit with modern styling
    
    Args:
        weed_name: Name of the weed
        width: Width of the image (optional, in pixels)
        stretch: Use full container width when True
    
    Returns:
        True if image displayed, False otherwise
    """
    image_path = find_weed_image(weed_name)
    
    if image_path and image_path.exists():
        try:
            # Add container wrapper styling
            st.markdown("""
            <style>
            .stImage { border-radius: 28px; overflow: hidden; }
            .stImage img { width: 100%; height: auto; object-fit: cover; }
            </style>
            """, unsafe_allow_html=True)
            
            if width is not None:
                st.image(str(image_path), width=width)
            elif stretch:
                st.image(str(image_path), width="stretch")
            else:
                st.image(str(image_path), width="stretch")
            return True
        except Exception as e:
            st.warning(f"⚠️ Tidak dapat menampilkan gambar: {str(e)}")
            return False
    
    return False

def get_all_weed_images():
    """
    Get list of all available weed images
    
    Returns:
        Dictionary with weed names as keys and image paths as values
    """
    images = {}
    
    if not IMAGE_DIR.exists():
        return images
    
    for file in IMAGE_DIR.glob("*"):
        if file.is_file() and file.suffix.lower() in SUPPORTED_FORMATS:
            weed_name = file.stem
            images[weed_name] = file
    
    return images

@st.cache_data
def get_cached_weed_images():
    """Get cached list of weed images for faster loading"""
    return get_all_weed_images()

def image_exists(weed_name):
    """Check if image exists for a weed"""
    return find_weed_image(weed_name) is not None
